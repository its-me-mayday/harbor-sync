from collections import namedtuple

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REGISTRY_SRC: str = Field(..., env="REGISTRY_SRC")
    USERNAME_SRC: str = Field(..., env="USERNAME_SRC")
    PASSWORD_SRC: str = Field(..., env="PASSWORD_SRC")
    PROJECT_NAME_SRC: str = Field(..., env="PROJECT_NAME_SRC")
    REGISTRY_DEST: str = Field(..., env="REGISTRY_DEST")
    USERNAME_DEST: str = Field(..., env="USERNAME_DEST")
    PASSWORD_DEST: str = Field(..., env="PASSWORD_DEST")
    PROJECT_NAME_DEST: str = Field(..., env="PROJECT_NAME_DEST")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


RegistrySettingsTuple = namedtuple(
    "RegistrySettings", ["host", "username", "project_name"]
)

RegistrySecretTuple = namedtuple(
    "RegistrySettings", ["password"]
)

source_secret = RegistrySecretTuple(
    password=Settings().PASSWORD_SRC,
) 
destination_secret = RegistrySecretTuple(
    password=Settings().PASSWORD_DEST,
) 

source_settings = RegistrySettingsTuple(
    host=Settings().REGISTRY_SRC,
    username=Settings().USERNAME_SRC,
    project_name=Settings().PROJECT_NAME_SRC,
)

destination_settings = RegistrySettingsTuple(
    host=Settings().REGISTRY_DEST,
    username=Settings().USERNAME_DEST,
    project_name=Settings().PROJECT_NAME_DEST,
)

