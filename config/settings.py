from collections import namedtuple

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REGISTRY_SRC: str = Field(..., env="REGISTRY_SRC")
    USERNAME_SRC: str = Field(..., env="USERNAME_SRC")
    PASSWORD_SRC: str = Field(..., env="PASSWORD_SRC")
    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


RegistrySettingsTuple = namedtuple(
    "RegistrySettings", ["host", "username", "secret", "project_name"]
)
registrySettings = RegistrySettingsTuple(
    host=Settings().REGISTRY_SRC,
    username=Settings().USERNAME_SRC,
    secret=Settings().PASSWORD_SRC,
    project_name=Settings().PROJECT_NAME,
)
