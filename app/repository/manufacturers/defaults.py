from .manufacturers import ManufacturersRepository
from .manufacturersINIfile import ManufacturersRepositoryINIFile
from .manufacturersJSONfile import ManufacturersRepositoryJSONFile
from .manufacturersYAMLfile import ManufacturersRepositoryYAMLFile

DEPENDENCY_RESOLVE_DICT = {
    "JSON": ManufacturersRepositoryJSONFile,
    "INI": ManufacturersRepositoryINIFile,
    "YAML": ManufacturersRepositoryYAMLFile,
}


def get_manufacturers_repository(env_var: str) -> ManufacturersRepository:
    return DEPENDENCY_RESOLVE_DICT[env_var]
