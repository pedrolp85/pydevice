from .manufacturers import ManufacturersRepository
from .manufacturersINIfile import ManufacturersRepositoryINIFile
from .manufacturersJSONfile import ManufacturersRepositoryJSONFile
from .manufacturersYAMLfile import ManufacturersRepositoryYAMLFile
from settings import Settings, get_settings


from fastapi import Depends

DEPENDENCY_RESOLVE_DICT = {
    "JSON": ManufacturersRepositoryJSONFile,
    "INI": ManufacturersRepositoryINIFile,
    "YAML": ManufacturersRepositoryYAMLFile,
}

def get_manufacturers_repository(settings: Settings = Depends(get_settings)) -> ManufacturersRepository:
    #print(DEPENDENCY_RESOLVE_DICT[sett.inventory_source])
    print("settings in get man", settings)
    if settings.manufacturers_source == "JSON":
        return ManufacturersRepositoryJSONFile(settings.manufacturers_file_source)
    if settings.manufacturers_source == "INI":
        return ManufacturersRepositoryINIFile(settings.manufacturers_file_source)
    if settings.manufacturers_source == "YML":
        print("devolvemos objeto YAML")
        print(settings.manufacturers_file_source)
        return ManufacturersRepositoryYAMLFile(settings.manufacturers_file_source)  