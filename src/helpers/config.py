# BaseSettings from pydantic-settings is used to create a settings class that automatically reads environment variables.
from pydantic_settings import BaseSettings, SettingsConfigDict


# Define a Settings class using pydantic-settings to manage your application's configuration settings.  
# The class reads environment variables from a .env file and provides them to your application. 
# Settings inherits from BaseSettings, allowing it to read and validate environment variables.
class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    # The Config subclass specifies that environment variables should be loaded from a file named .env.
    class Config:
        env_file = ".env"

# This function creates & returns an instance of the Settings class. 
# It will be used as a dependency in FastAPI endpoints to provide the settings.
def get_settings():
    return Settings()
