from .interfaces import InterfacesRepository
from .interfacesINIfile import InterfacesRepositoryINIFile
from .interfacesJSONfile import InterfacesRepositoryJSONFile
from .interfacesYAMLfile import InterfacesRepositoryYAMLFile
from settings import Settings, get_settings


from fastapi import Depends

DEPENDENCY_RESOLVE_DICT = {
    "JSON": InterfacesRepositoryJSONFile,
    "INI": InterfacesRepositoryINIFile,
    "YAML": InterfacesRepositoryYAMLFile,
}


def get_interfaces_repository(settings: Settings = Depends(get_settings)) -> InterfacesRepository:

    if settings.interfaces_source == "JSON":
        return InterfacesRepositoryJSONFile(settings.interfaces_file_source)
    if settings.interfaces_source == "INI":
        return InterfacesRepositoryINIFile(settings.interfaces_file_source)
    if settings.interfaces_source == "YML":
        return InterfacesRepositoryYAMLFile(settings.interfaces_file_source)
