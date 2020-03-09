class Language(object):
    """A language name.
    """

    def __init__(self, abbreviation: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        return self.abbreviation

    def __repr__(self) -> str:
        return self.abbreviation


CN = Language('cn_CN')
DE = Language('de_DE')
ES = Language('es_ES')
FR = Language('fr_FR')
IT = Language('it_IT')
KR = Language('ko_KR')
RU = Language('ru_RU')
US = Language('en_US')

LANGUAGES = [
    CN,
    DE,
    ES,
    FR,
    IT,
    KR,
    RU,
    US,
]


class Translation(object):
    """Full translation information. All languages are present.
    """

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
        super().__init__(*args, **kwargs)
        if len(set(translations.keys()).intersection(LANGUAGES)) == len(LANGUAGES):
            for language in translations:
                self.language = translations[language]
        elif cn_CN and de_DE and es_ES and fr_FR and it_IT and ko_KR and ru_RU and en_US:
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
                'Expected more information. Please make sure you have translations for all languages.'
            )
