from .devices import DevicesRepository
from .devicesINIfile import DevicesRepositoryINIFile
from .devicesJSONfile import DevicesRepositoryJSONFile
from .devicesYAMLfile import DevicesRepositoryYAMLFile
from .devicesDB import DevicesRepositoryDatabase
from sqldb import _get_db
from settings import Settings, get_settings
from typing import Optional


DEPENDENCY_RESOLVE_DICT = {
    "JSON": DevicesRepositoryJSONFile,
    "INI": DevicesRepositoryINIFile,
    "YAML": DevicesRepositoryYAMLFile,
    "MYSQL": DevicesRepositoryDatabase
}



def get_devices_repository() -> DevicesRepository:

    settings = get_settings()
    if settings.inventory_source == "MYSQL": return DevicesRepositoryDatabase(next(_get_db()))
    else:
        return DEPENDENCY_RESOLVE_DICT[settings.inventory_source](settings.inventory_file_source)
    
        
