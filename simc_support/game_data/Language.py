import enum


class Language(enum.Enum):
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
        cn_CN: str = None,
        de_DE: str = None,
        es_ES: str = None,
        fr_FR: str = None,
        it_IT: str = None,
        ko_KR: str = None,
        ru_RU: str = None,
        en_US: str = None,
        translations: dict = None,
        *args,
        **kwargs,
    ):
        super().__init__()

        languages = [language.name for language in Language]

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
                    f"translations dictionary didn't contain expected keys. Got: {sorted(list(translations))} Expected keys: {languages}"
                )
        elif (
            cn_CN and de_DE and es_ES and fr_FR and it_IT and ko_KR and ru_RU and en_US
        ):
            self.CN = cn_CN
            self.DE = de_DE
            self.ES = es_ES
            self.FR = fr_FR
            self.IT = it_IT
            self.KR = ko_KR
            self.RU = ru_RU
            self.US = en_US
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
