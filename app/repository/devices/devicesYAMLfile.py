import ipaddress
from pathlib import Path
from typing import List, Optional

import yaml
from model.device import Device
from repository.exceptions import DeviceAlreadyExistsException, DeviceNotFoundException

from .devices import DevicesRepository


def ipv4_representer(dumper, data):
    return dumper.represent_scalar("!ipaddress.IPv4Address", str(data))


def ipv4_constructor(loader, node):
    value = loader.construct_scalar(node)
    return ipaddress.IPv4Address(value)


yaml.add_representer(ipaddress.IPv4Address, ipv4_representer)
yaml.add_constructor("!ipaddress.IPv4Address", ipv4_constructor)


class DevicesRepositoryYAMLFile(DevicesRepository):
    def __init__(self,file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._devices = (
            self._get_devices_from_yaml_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return Path(__file__).parent.parent.parent / self._file_source / "inventory.yml"

    def _get_devices_from_yaml_file(self) -> List[Device]:
        with open(self._file_name) as file:
            devices_raw = yaml.full_load(file)
            device_list = []
            for device in devices_raw:
                d = list(device.values())[0]
                d.update({"name": list(device.keys())[0]})
                device_list.append(Device(**d))
            return device_list

    def _save_devices_to_yaml_file(self) -> None:
        devices_to_save = [p.dict() for p in self._devices]
        devices = []
        for device in devices_to_save:
            dict_yaml_device = {}
            dict_yaml_device.update({device.pop("name"): device})
            devices.append(dict_yaml_device)
        with open(self._file_name, mode="w") as f:
            f.write(yaml.dump(devices, indent=10, default_flow_style=False))

    def get_device(self, id: int) -> Device:
        self._get_devices_from_yaml_file()
        for device in self._devices:
            if device.id == id:
                return device
        raise DeviceNotFoundException(id)

    def create_device(self, device: Device) -> None:
        try:
            self.get_device(device.id)
        except DeviceNotFoundException:
            self._devices.append(device)
            self._save_devices_to_yaml_file()
        else:
            raise DeviceAlreadyExistsException(device.id)

    def update_device(self, id: int, device: Device) -> None:
        try:
            self.get_device(device.id)
        except DeviceNotFoundException:
            pass
        else:
            raise DeviceAlreadyExistsException(manufacturer.id)
