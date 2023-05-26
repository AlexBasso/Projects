import os

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


class SiteSettings(BaseSettings):
    """ Class inhereting from pydantic BaseSettings. Its function is to retrive tokens and make them not visable in
    logging or tracebacks via SecretStr. Provides only surface level protection.
    Attrs:
        bot_api: via getenv receive bot token.
    """
    bot_api: SecretStr = os.getenv("BOT_API", None)
    site_api: SecretStr = os.getenv("SITE_API", None)
    host_api: StrictStr = os.getenv("HOST_API", None)
    host_url: StrictStr = os.getenv("URL", None)
