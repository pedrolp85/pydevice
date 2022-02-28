from .interfaces import InterfacesRepository
from .interfacesINIfile import InterfacesRepositoryINIFile
from .interfacesJSONfile import InterfacesRepositoryJSONFile
from .interfacesYAMLfile import InterfacesRepositoryYAMLFile
from . interfacesDB import InterfacesRepositoryDatabase
from settings import Settings, get_settings
from sqldb import _get_db



DEPENDENCY_RESOLVE_DICT = {
    "JSON": InterfacesRepositoryJSONFile,
    "INI": InterfacesRepositoryINIFile,
    "YAML": InterfacesRepositoryYAMLFile,
    "MYSQL": InterfacesRepositoryDatabase
}



def get_interfaces_repository() -> InterfacesRepository:

    settings = get_settings()
    
    if settings.interfaces_source == "MYSQL": return InterfacesRepositoryDatabase(next(_get_db()))
    else:
        return DEPENDENCY_RESOLVE_DICT[settings.interfaces_source]()
