from repository.devices import (
    DevicesRepository, 
    DevicesRepositoryJSONFile,
    DevicesRepositoryINIFile,
    DevicesRepositoryYAMLFile
    )

def get_devices_repository() -> DevicesRepository:
    return DevicesRepositoryJSONFile()


# def get_device_repository() -> DeviceRepository:
#     return get_device_repository_db()
