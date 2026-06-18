from dataclasses import dataclass


@dataclass(frozen=True)
class UserTestData:
    NAME: str = "Сергей"
    EMAIL: str = "SergeyKulikov42123@ya.ru"
    PASSWORD: str = "SergeyKulikov42123"