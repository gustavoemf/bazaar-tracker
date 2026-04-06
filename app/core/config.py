import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "App")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.0.1")
    APP_ENV: str = os.getenv("APP_ENV", "dev")


settings = Settings()