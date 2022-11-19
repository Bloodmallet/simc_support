import enum
import typing


class Language(enum.Enum):
    BR = "pt_BR"
    CN = "cn_CN"
    DE = "de_DE"
    ES = "es_ES"
    FR = "fr_FR"
    IT = "it_IT"
    KR = "ko_KR"
    RU = "ru_RU"
    US = "en_US"


class Translation(object):
    """Full translation information. All languages are present."""

    def __init__(
        self,
        pt_BR: typing.Optional[str] = None,
        cn_CN: typing.Optional[str] = None,
        de_DE: typing.Optional[str] = None,
        es_ES: typing.Optional[str] = None,
        fr_FR: typing.Optional[str] = None,
        it_IT: typing.Optional[str] = None,
        ko_KR: typing.Optional[str] = None,
        ru_RU: typing.Optional[str] = None,
        en_US: typing.Optional[str] = None,
        translations: typing.Optional[dict] = None,
        *args,
        **kwargs,
    ):
        super().__init__()

        languages: typing.List[str] = [language.name for language in Language]

        if translations:
            if len(set(translations.keys()).intersection(languages)) == len(languages):
                for language in translations:
                    setattr(self, language, translations[language])
            elif isinstance(list(translations)[0], Language):
                if len(
                    set([key.name for key in list(translations)]).intersection(
                        languages
                    )
                ) == len(languages):
                    for language in translations:
                        setattr(self, language.name, translations[language])
            else:
                raise ValueError(
                    f"'translations'-dictionary didn't contain expected keys. Got: {sorted(list(translations))} Expected keys: {sorted(languages)}"
                )
        elif (
            cn_CN
            and de_DE
            and es_ES
            and fr_FR
            and it_IT
            and ko_KR
            and ru_RU
            and en_US
            and pt_BR
        ):
            self.CN = cn_CN
            self.DE = de_DE
            self.ES = es_ES
            self.FR = fr_FR
            self.IT = it_IT
            self.KR = ko_KR
            self.RU = ru_RU
            self.US = en_US
            self.BR = pt_BR
        else:
            raise ValueError(
                "Expected more information. Please make sure you have translations for all languages."
            )

    def get_dict(self) -> dict:
        response = {}
        for lang in Language:
            response[lang.value] = getattr(self, lang.name)

        return response


class EmptyTranslation(Translation):
    """If you don't have translations handy, but need to provide a translations object."""

    def __init__(self):
        languages = {language.name: "" for language in Language}
        super().__init__(self, translations=languages)


def _get_translations(item: dict, unified_key: str = "name") -> Translation:
    keys = [
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
    d = {}
    for key in keys:
        d[key.split("_")[1]] = item[f"{unified_key}_{key}"]

    d["BR"] = d["PT"]
    d.pop("PT")

    return Translation(translations=d)
