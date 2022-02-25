from .devices import DevicesRepository
from .devicesINIfile import DevicesRepositoryINIFile
from .devicesJSONfile import DevicesRepositoryJSONFile
from .devicesYAMLfile import DevicesRepositoryYAMLFile
from settings import Settings, get_settings
from typing import Optional


DEPENDENCY_RESOLVE_DICT = {
    "JSON": DevicesRepositoryJSONFile,
    "INI": DevicesRepositoryINIFile,
    "YAML": DevicesRepositoryYAMLFile,
}

def get_devices_repository() -> DevicesRepository:

    settings = get_settings()
    return DEPENDENCY_RESOLVE_DICT[settings.inventory_source](settings.inventory_file_source)
    
        
