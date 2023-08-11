import logging
from enum import Enum

from pydantic import BaseModel

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(asctime)s - %(message)s",
    datefmt='%H:%M:%S'
)


class Defaults:
    timeout = 5


class AvailableColors(Enum):
    GREEEN = 'GREEN'
    AMBER = 'AMBER'

    def __call__(self, *args, **kwargs):
        return self.value

    def __get__(self, instance, owner):
        return self.value.lower()


class MainSchema(BaseModel):
    color: AvailableColors
    timeout: int = Defaults.timeout
