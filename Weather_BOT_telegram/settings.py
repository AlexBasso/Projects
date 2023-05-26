import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()


class SiteSettings(BaseSettings):
    """ Class inhereting from pydantic BaseSettings. Its function is to retrive tokens and make them not visable in
    logging or tracebacks via SecretStr. Provides only surface level protection.
    Attrs:
        bot_api: via getenv receive bot token.
    """
    bot_api: SecretStr = os.getenv("BOT_API", None)



