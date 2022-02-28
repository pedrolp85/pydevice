from .manufacturers import ManufacturersRepository
from .manufacturersINIfile import ManufacturersRepositoryINIFile
from .manufacturersJSONfile import ManufacturersRepositoryJSONFile
from .manufacturersYAMLfile import ManufacturersRepositoryYAMLFile
from .manufacturersDB import ManufacturersRepositoryDatabase
from settings import Settings, get_settings
from sqldb import _get_db



DEPENDENCY_RESOLVE_DICT = {
    "JSON": ManufacturersRepositoryJSONFile,
    "INI": ManufacturersRepositoryINIFile,
    "YAML": ManufacturersRepositoryYAMLFile,
    "MYSQL": ManufacturersRepositoryDatabase
}



def get_manufacturers_repository() -> ManufacturersRepository:

    settings = get_settings()
    
    if settings.manufacturers_source == "MYSQL": return ManufacturersRepositoryDatabase(next(_get_db()))
    else:
        return DEPENDENCY_RESOLVE_DICT[settings.manufacturers_source]()