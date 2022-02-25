from .manufacturers import ManufacturersRepository
from .manufacturersINIfile import ManufacturersRepositoryINIFile
from .manufacturersJSONfile import ManufacturersRepositoryJSONFile
from .manufacturersYAMLfile import ManufacturersRepositoryYAMLFile
from settings import Settings, get_settings


from fastapi import Depends

DEPENDENCY_RESOLVE_DICT = {
    "JSON": ManufacturersRepositoryJSONFile,
    "INI": ManufacturersRepositoryINIFile,
    "YAML": ManufacturersRepositoryYAMLFile,
}

def get_manufacturers_repository() -> ManufacturersRepository:

    settings = get_settings()
    return DEPENDENCY_RESOLVE_DICT[settings.manufacturers_source](settings.manufacturers_file_source) 