from .devices import DevicesRepository
from .devicesINIfile import DevicesRepositoryINIFile
from .devicesJSONfile import DevicesRepositoryJSONFile
from .devicesYAMLfile import DevicesRepositoryYAMLFile
from settings import Settings, get_settings

from fastapi import Depends


DEPENDENCY_RESOLVE_DICT = {
    "JSON": DevicesRepositoryJSONFile,
    "INI": DevicesRepositoryINIFile,
    "YAML": DevicesRepositoryYAMLFile,
}


def get_devices_repository(settings: Settings = Depends(get_settings)) -> DevicesRepository:

    if settings.inventory_source == "JSON":
        return DevicesRepositoryJSONFile(settings.inventory_file_source)
    if settings.inventory_source == "INI":
        return DevicesRepositoryINIFile(settings.inventory_file_source)
    if settings.inventory_source == "YML":
        return DevicesRepositoryYAMLFile(settings.inventory_file_source)    
        
