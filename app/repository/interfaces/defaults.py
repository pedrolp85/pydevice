from .interfaces import InterfacesRepository
from .interfacesINIfile import InterfacesRepositoryINIFile
from .interfacesJSONfile import InterfacesRepositoryJSONFile
from .interfacesYAMLfile import InterfacesRepositoryYAMLFile

DEPENDENCY_RESOLVE_DICT = {
    "JSON": InterfacesRepositoryJSONFile,
    "INI": InterfacesRepositoryINIFile,
    "YAML": InterfacesRepositoryYAMLFile,
}


def get_interfaces_repository(env_var: str) -> InterfacesRepository:
    return DEPENDENCY_RESOLVE_DICT[env_var]
