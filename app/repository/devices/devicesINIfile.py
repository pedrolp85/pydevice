import configparser
from pathlib import Path
from typing import List

from model.device import Device
from repository.exceptions import DeviceAlreadyExistsException, DeviceNotFoundException
from settings import *

from .devices import DevicesRepository


class DevicesRepositoryINIFile(DevicesRepository):
    def __init__(self, file_name: str = "inventory.ini") -> None:
        self._file_name = self._get_dir(file_name)
        self._devices = (
            self._get_devices_from_ini_file() if Path(self._file_name).is_file() else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return Path(__file__).parent.parent.parent / INVENTORY_FILE_SOURCE / file_name

    def _get_devices_from_ini_file(self) -> List[Device]:
        ini_parser = configparser.ConfigParser()
        ini_parser.read(self._file_name)
        device_list = []
        for section in ini_parser.sections():
            print(section)
            device_dictionary = {
                option: ini_parser.get(section, option)
                for option in ini_parser.options(section)
            }
            device_dictionary.update({"name": section})
            device_list.append(Device(**device_dictionary))

        return device_list

    def _save_devices_to_ini_file(self) -> None:
        devices_to_save = [p.dict() for p in self._devices]
        parser = configparser.ConfigParser()
        for device in devices_to_save:
            parser.add_section(device["name"])
            for k, v in device.items():
                parser.set(device["name"], k, str(v))
        with open("inventory.ini", "w") as configfile:
            parser.write(configfile)

    def get_device(self, id: int) -> Device:
        self._get_devices_from_ini_file()
        for device in self._devices:
            if device.id == id:
                return device
        raise DeviceNotFoundException(id)

    def create_device(self, device: Device) -> None:
        try:
            self.get_device(device.id)
        except DeviceNotFoundException:
            self._devices.append(device)
            self._save_devices_to_ini_file()
        else:
            raise DeviceAlreadyExistsException(device.id)

    def update_device(self, id: int, device: Device) -> None:
        try:
            self.get_device(device.id)
        except DeviceNotFoundException:
            pass
        else:
            raise DeviceAlreadyExistsException(manufacturer.id)