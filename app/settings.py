import os

from pydantic import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):

    inventory_source: str = os.getenv('INVENTORY_SOURCE')
    manufacturers_source: str = os.getenv('MANUFACTURERS_SOURCE')
    interfaces_source: str = os.getenv('INTERFACES_SOURCE')
    inventory_file_source: str = os.getenv('INVENTORY_FILE_SOURCE')
    manufacturers_file_source: str = os.getenv('MANUFACTURERS_FILE_SOURCE')
    interfaces_file_source: str = os.getenv('INTERFACES_FILE_SOURCE')

    class Config:
        env_file = "test.env"




