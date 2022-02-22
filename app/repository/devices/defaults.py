from .devices import DevicesRepository
from .devicesINIfile import DevicesRepositoryINIFile
from .devicesJSONfile import DevicesRepositoryJSONFile
from .devicesYAMLfile import DevicesRepositoryYAMLFile

DEPENDENCY_RESOLVE_DICT = {
    "JSON": DevicesRepositoryJSONFile,
    "INI": DevicesRepositoryINIFile,
    "YAML": DevicesRepositoryYAMLFile,
}


def get_devices_repository(env_var: str) -> DevicesRepository:
    return DEPENDENCY_RESOLVE_DICT[env_var]
