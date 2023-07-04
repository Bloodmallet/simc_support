import argparse
import json
import logging
import os
import pathlib
import subprocess
import typing

logger = logging.getLogger(__name__)

_LOCALES = [
    "en_US",
    "ko_KR",
    "fr_FR",
    "de_DE",
    "zh_CN",
    "es_ES",
    "ru_RU",
    "it_IT",
    "pt_PT",
]

DATA_PATH = "simc_support/game_data/data_files"

TABLE_ROW = typing.Dict[str, typing.Union[int, str, None, typing.List[int]]]
TABLE = typing.List[TABLE_ROW]
LOCALE_TABLES = typing.Dict[str, TABLE]
T = typing.TypeVar("T")


def safely_convert_to(
    input: typing.Any, target_type: typing.Callable[[typing.Any], T], default: T
) -> T:
    if input is None:
        return default
    return target_type(input)


def get_localized_spell_names(spells: TABLE, spell_id: int) -> typing.Dict[str, str]:
    """Get localization dictionary of `spell_id`.

    Raises:
        ValueError: If missing `spell_id` in `spells`

    Returns:
        typing.Dict[str, str]: translation dictionary
    """
    localized_fields = ["name", *[f"name_{locale}" for locale in _LOCALES]]
    for spell in spells:
        if spell_id == spell["id"]:
            return {k: str(v) for k, v in spell.items() if k in localized_fields}

    raise ValueError(f"No spell with id '{spell_id}' found.")


def _create_id_dict_from_table(table: typing.List[dict], column: str = "id") -> dict:
    """Create a new dictionary containing all rows, but now associated by the declared column value.

    Args:
        table (typing.List[dict]): [{"example": "hello"}, {"example", "world"}]
        column (str): _description_

    Returns:
        dict: {"hello": [{"example": "hello"}], "world": [{"example", "world"}]}
    """
    id_dict = {}
    for row in table:
        if row[column] and row[column] not in id_dict:
            id_dict[row[column]] = [row]
        elif row[column] and row[column] in id_dict:
            id_dict[row[column]].append(row)

    return id_dict


def collect_localizations(
    localized_tables: LOCALE_TABLES,
    *,
    filter_function: typing.Callable[[dict], bool] = any,
    match_field: str = "id",
    translation_field: str = "name",
) -> typing.List[dict]:
    """Collect localized `translation_field` via matching `match_field`.

    Special Args:
        filter_function (callable, optional): Evaluates to True for Rows that should be in the result. Defaults to `any`.

    Returns:
        TABLE: single table containing additional columns with localized `translation_field`
    """

    logger.debug("Merging")
    result = []
    logger.debug("Creating dictionaries for item tables.")

    dict_locales = {}
    for locale in _LOCALES:
        logger.debug(f"Creating {locale} dictionary.")
        dict_locales[locale] = _create_id_dict_from_table(
            localized_tables[locale], match_field
        )

    logger.debug("Created all locale tables.")
    # raise ValueError

    logger.debug("Building table with all translations")
    for i, locale in enumerate(_LOCALES):
        logger.debug(f"  {locale}")
        # prepare
        if i == 0:
            information: dict
            for information in localized_tables[locale]:
                if not filter_function(information):
                    continue

                if translation_field:
                    information[f"{translation_field}_{locale}"] = information[
                        translation_field
                    ]

                result.append(information)

        # enrich
        else:
            if not translation_field:
                continue
            for information in result:
                translated_row = dict_locales[locale].get(information[match_field])
                information[f"{translation_field}_{locale}"] = (
                    translated_row[0][translation_field]
                    if translated_row
                    else information[translation_field]
                )

    return result


class ArgsObject:
    simc: str
    output: str
    wow: str
    no_load: bool
    no_extract: bool
    ptr: bool
    alpha: bool
    beta: bool
    debug: bool
    env: str


def handle_arguments() -> ArgsObject:
    """Scan user provided arguments and provide the corresponding argparse ArgumentParser.

    Returns:
        argparse.ArgumentParser: [description]
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-s",
        "--simc",
        nargs="?",
        default=None,
        help="Absolute path to your local SimulationCraft version.",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        default=os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "tmp"),
        help="Absolute path to the save location of DB files.",
    )
    parser.add_argument(
        "-w",
        "--wow",
        nargs="?",
        default=None,
        help=r"Absolute path to your World of Warcraft installation to get hotfixes. E.g. /games/World\ of\ Warcraft/_beta_",
    )
    parser.add_argument(
        "--no-load",
        action="store_true",
        help="Flag disables download from CDN. Instead only already present local files are used.",
    )
    parser.add_argument(
        "--no-extract",
        action="store_true",
        help="Flag disables extracting from db2 files. Instead only already present local files are used.",
    )
    parser.add_argument(
        "--ptr",
        action="store_true",
        help="Download PTR files",
    )
    parser.add_argument(
        "--beta",
        action="store_true",
        help="Download BETA files",
    )
    parser.add_argument(
        "--alpha",
        action="store_true",
        help="Download ALPHA files",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output",
    )
    parser.add_argument(
        "--env",
        nargs="?",
        default=None,
        help="Absolute path to the executable python-env file.",
    )
    return parser.parse_args()  # type: ignore


def get_python(env: typing.Optional[str] = None) -> str:
    """Find and return the appropriate command line input to use Python 3+

    Returns:
        str: Either "python" or "python3"
    """

    if env:
        return env

    def is_python() -> bool:
        cmd = ["python", "--version"]
        logger.debug(cmd)
        output = subprocess.run(cmd, stdout=subprocess.PIPE)
        return output.stdout.split()[1].startswith(b"3")

    def is_python3() -> bool:
        cmd = ["python3", "--version"]
        logger.debug(cmd)
        output = subprocess.run(cmd, stdout=subprocess.PIPE)
        return output.stdout.split()[1].startswith(b"3")

    if not (is_python() or is_python3()):
        raise SystemError("Python 3 is required.")

    return "python" if is_python() else "python3"


def casc(args: ArgsObject) -> None:
    """Download all db2 files of all locales described in _LOCALES.

    Args:
        args (object): [description]

    Raises:
        SystemError: If Python 3+ is not available in commandline neither via 'python' nor 'python3'.
    """
    if args.no_load:
        logger.info("Skipping download")
        return
    logger.info("Downloading files (casc)")

    python = get_python(args.env)

    command = [
        python,
        "casc_extract.py",
        "--cdn",
        "-m",
        "batch",
    ]
    if args.ptr:
        # command.append("--ptr")
        arg = "--product=wowxptr"
        logger.warning(
            f"Using {arg}. make sure this is still the correct ptr for your usecase."
        )
        command.append(arg)
    elif args.beta:
        command.append("--beta")
    elif args.alpha:
        command.append("--alpha")

    for locale in _LOCALES:
        logger.info(locale)
        full_command = command + [
            "--locale",
            locale,
            "-o",
            os.path.join(args.output, locale),
        ]
        logger.debug(full_command)
        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.join(str(args.simc), "casc_extract"),
        )
        # ['python', 'casc_extract.py', '--cdn', '-m', 'batch', '--locale', 'pt_PT', '-o', 'D:\\Programme\\simc_support\\simc_support\\tmp\\pt_PT']
        while True:
            if not process.stdout:
                raise ValueError("Process somehow has no output")

            output = process.stdout.readline()
            if output == b"" and process.poll() is not None:
                break
            if output:
                logger.debug(output.strip().decode("ascii"))
        rc = process.poll()
        if rc != 0:
            logger.error(
                f"Error occurred while loading {locale}. {process.communicate()[1]}"  # type: ignore
            )

    logger.info("Downloaded files")


def get_compiled_data_path(args: ArgsObject, locale: str) -> str:
    return os.path.join(args.output, "compiled", locale)


def dbc(args: ArgsObject, files: typing.List[str]) -> typing.Dict[str, LOCALE_TABLES]:
    """Extract and transforms files into JSON format.
    TODO: parallelize this

    Args:
        args (object): [description]
        files (typing.List[str]): [description]
    """
    data: typing.Dict[str, LOCALE_TABLES] = {}

    if args.no_extract:
        logger.info("Skipping extraction")

        for file in files:
            data[file] = {}
            for locale in _LOCALES:
                with open(
                    os.path.join(get_compiled_data_path(args, locale), f"{file}.json"),
                    "r",
                ) as f:
                    data[file][locale] = json.load(f)
        return data

    logger.info("Extracting files (dbc)")

    python = get_python(args.env)

    wow_versions = os.listdir(os.path.join(args.output, _LOCALES[0]))
    logger.debug(f" Detected wow versions: {wow_versions}")
    wow_version = wow_versions[-1]

    command = [
        python,
        "dbc_extract.py",
        "-b",
        wow_version,
        "-t",
        "json",
    ]
    if args.wow:
        command.append("--hotfix")
        command.append(os.path.join(args.wow, "Cache/ADB/enUS/DBCache.bin"))

    for file in files:
        data[file] = {}
        for locale in _LOCALES:
            logger.info(f"{file} {locale}")

            cmd = command + [
                "-p",
                os.path.join(args.output, locale, wow_version, "DBFilesClient"),
                file,
            ]

            pathlib.Path(os.path.join(get_compiled_data_path(args, locale))).mkdir(
                parents=True, exist_ok=True
            )

            logger.debug(cmd)
            process = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=os.path.join(args.simc, "dbc_extract3"),
            )
            if process.returncode != 0:
                logger.error(
                    f"Error occurred while extracting {file} {locale}. {process.stderr.decode()}"
                )
            else:
                with open(
                    os.path.join(get_compiled_data_path(args, locale), f"{file}.json"),
                    "wb",
                ) as f:
                    f.write(process.stdout)

                data[file][locale] = json.loads(process.stdout)

    return data
