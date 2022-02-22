import ipaddress
from pathlib import Path
from typing import List

import yaml
from model.interface import L3Interface
from repository.exceptions import (
    InterfaceAlreadyExistsException,
    InterfaceNotFoundException,
)

from .interfaces import InterfacesRepository


def ipv4_representer(dumper, data):
    return dumper.represent_scalar("!ipaddress.IPv4Address", str(data))


def ipv4_constructor(loader, node):
    value = loader.construct_scalar(node)
    return ipaddress.IPv4Address(value)


yaml.add_representer(ipaddress.IPv4Address, ipv4_representer)
yaml.add_constructor("!ipaddress.IPv4Address", ipv4_constructor)


class InterfacesRepositoryYAMLFile(InterfacesRepository):
    def __init__(self, file_name: str = "interfaces.yml") -> None:
        self._file_name = file_name
        self._interfaces = (
            self._get_interfaces_from_yaml_file() if Path(file_name).is_file() else []
        )

    def _get_interfaces_from_yaml_file(self) -> List[L3Interface]:
        with open(self._file_name) as file:
            interfaces_raw = yaml.full_load(file)
            interface_list = []
            for interface in interfaces_raw:
                d = list(interface.values())[0]
                d.update({"name": list(interface.keys())[0]})
                interface_list.append(L3Interface(**d))
            return interface_list

    def _save_interfaces_to_yaml_file(self) -> None:
        interfaces_to_save = [p.dict() for p in self._interfaces]
        interfaces = []
        for interface in interfaces_to_save:
            dict_yaml_interface = {}
            dict_yaml_interface.update({interface.pop("name"): interface})
            interfaces.append(dict_yaml_interface)
        with open(self._file_name, mode="w") as f:
            f.write(yaml.dump(interfaces, indent=10, default_flow_style=False))

    def get_interface(self, id: int) -> L3Interface:
        self._get_interfaces_from_yaml_file()
        for interface in self._interfaces:
            if interface.id == id:
                return interface
        raise InterfaceNotFoundException(id)

    def create_interface(self, interface: L3Interface) -> None:
        try:
            self.get_interface(interface.id)
        except InterfaceNotFoundException:
            self._interfaces.append(device)
            self._save_interfaces_to_yaml_file()
        else:
            raise InterfaceAlreadyExistsException(device.id)

    def update_interface(self, id: int, interface: L3Interface) -> None:
        try:
            self.get_interface(interface.id)
        except InterfaceNotFoundException:
            pass
        else:
            raise InterfaceAlreadyExistsException(manufacturer.id)