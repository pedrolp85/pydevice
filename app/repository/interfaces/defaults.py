from .interfaces import InterfacesRepository
from .interfacesINIfile import InterfacesRepositoryINIFile
from .interfacesJSONfile import InterfacesRepositoryJSONFile
from .interfacesYAMLfile import InterfacesRepositoryYAMLFile
from settings import Settings, get_settings




DEPENDENCY_RESOLVE_DICT = {
    "JSON": InterfacesRepositoryJSONFile,
    "INI": InterfacesRepositoryINIFile,
    "YAML": InterfacesRepositoryYAMLFile,
}


def get_interfaces_repository() -> InterfacesRepository:

    settings = get_settings()
    return DEPENDENCY_RESOLVE_DICT[settings.interfaces_source](settings.interfaces_file_source)
