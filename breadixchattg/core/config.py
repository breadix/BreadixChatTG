from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class MainDBConfig(BaseModel):
    echo: bool
    user: str
    password: str
    host: str
    port: int

    @property
    def url(self) -> str:
        return f'{self.user}:{self.password}@{self.host}:{self.port}'

    naming_convention: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class TelegramKeysConfig(BaseModel):
    bot_api_key: str


class TelegramAppConfig(BaseModel):
    id: int
    hash: str


class Links(BaseModel):
    commands_documentation: str
    vk_bot: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file='.env',
        env_nested_delimiter='__',
        extra='ignore'
    )

    main_db: MainDBConfig
    tg_api_keys: TelegramKeysConfig
    tg_app: TelegramAppConfig
    link: Links
    mode: str


settings = Settings()
