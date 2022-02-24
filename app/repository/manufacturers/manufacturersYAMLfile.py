import ipaddress
from pathlib import Path
from typing import List, Optional

import yaml
from model.manufacturer import Manufacturer
from repository.exceptions import (
    ManufacturerAlreadyExistsException,
    ManufacturerNotFoundException,
)

from .manufacturers import ManufacturersRepository


def ipv4_representer(dumper, data):
    return dumper.represent_scalar("!ipaddress.IPv4Address", str(data))


def ipv4_constructor(loader, node):
    value = loader.construct_scalar(node)
    return ipaddress.IPv4Address(value)


yaml.add_representer(ipaddress.IPv4Address, ipv4_representer)
yaml.add_constructor("!ipaddress.IPv4Address", ipv4_constructor)


class ManufacturersRepositoryYAMLFile(ManufacturersRepository):
    def __init__(self, file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._manufacturers = (
            self._get_manufacturers_from_yaml_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return (
            Path(__file__).parent.parent.parent / self._file_source / "manufacturers.yml"
        )

    def _get_manufacturers_from_yaml_file(self) -> List[Manufacturer]:
        with open(self._file_name) as file:
            manufacturers_raw = yaml.full_load(file)
            manufacturer_list = []
            for manufacturer in manufacturers_raw:
                d = list(manufacturer.values())[0]
                d.update({"name": list(manufacturer.keys())[0]})
                manufacturer_list.append(Manufacturer(**d))
            return manufacturer_list

    def _save_manufacturers_to_yaml_file(self) -> None:
        manufacturers_to_save = [p.dict() for p in self._manufacturers]
        manufacturers = []
        for manufacturer in manufacturers_to_save:
            dict_yaml_manufacturer = {}
            dict_yaml_manufacturer.update({manufacturer.pop("name"): manufacturer})
            manufacturers.append(dict_yaml_manufacturer)
        with open(self._file_name, mode="w") as f:
            f.write(yaml.dump(manufacturers, indent=10, default_flow_style=False))

    def get_manufacturer(self, id: int) -> Manufacturer:
        self._get_manufacturers_from_yaml_file()
        for manufacturer in self._manufacturers:
            if manufacturer.id == id:
                return manufacturer
        raise ManufacturerNotFoundException(id)

    def create_manufacturer(self, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            self._manufacturers.append(manufacturer)
            self._save_manufacturers_to_yaml_file()
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)

    def update_manufacturer(self, id: int, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            pass
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)
