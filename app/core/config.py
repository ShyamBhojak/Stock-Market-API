from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    # SECRET_KEY:str
    # MARKET_API_KEY:str

    class Config:
        env_file = ".env"


settings = Settings()

if __name__ == "__main__":
    print(settings.DATABASE_URL)