import configparser
import json
from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import List, Optional

from model.manufacturer import Manufacturer
from pydantic.json import pydantic_encoder
from repository.exceptions import (
    ManufacturerAlreadyExistsException,
    ManufacturerNotFoundException,
)


class ManufacturersRepository(metaclass=ABCMeta):
    
    def __init__(self, file_source: Optional[str]):
        self._file_source = file_source    
    
    @abstractmethod
    def get_manufacturer(self, id: int) -> Manufacturer:
        pass

    @abstractmethod
    def create_manufacturer(self, manufacturer: Manufacturer) -> None:
        pass

    @abstractmethod
    def update_manufacturer(self, id: int, manufacturer: Manufacturer) -> None:
        pass

    def get_manufacturers(self) -> List[Manufacturer]:
        return self._manufacturers


class ManufacturersRepositoryJSONFile(ManufacturersRepository):
    def __init__(self, file_name: str = "manufacturers.json") -> None:
        self._file_name = file_name
        self._manufacturers = (
            self._get_manufacturers_from_json_file()
            if Path(file_name).is_file()
            else []
        )

    def _get_manufacturers_from_json_file(self) -> List[Manufacturer]:
        with open(self._file_name, mode="r") as f:
            raw_manufacturers = f.read()
            manufacturers = json.loads(raw_manufacturers)
            return [Manufacturer(**p) for p in manufacturers]
        return []

    def _save_manufacturers_to_json_file(self) -> None:
        manufacturers_to_save = [p.dict() for p in self._manufacturers]
        with open(self._file_name, mode="w") as f:
            data = json.dumps(manufacturers_to_save, indent=4, default=pydantic_encoder)
            f.write(data)

    def get_manufacturer(self, id: int) -> Manufacturer:
        self._get_manufacturers_from_json_file()
        for manufacturer in self._manufacturers:
            if manufacturer.id == id:
                return manufacturer
        raise ManufacturerNotFoundException(id)

    def create_manufacturer(self, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            self._manufacturers.append(manufacturer)
            self._save_manufacturers_to_json_file()
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)

    def update_manufacturer(self, id: int, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            pass
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)


class ManufacturersRepositoryINIFile(ManufacturersRepository):
    def __init__(self, file_name: str = "manufacturers.ini") -> None:
        self._file_name = file_name
        self._manufacturers = (
            self._get_manufacturers_from_ini_file() if Path(file_name).is_file() else []
        )

    def _get_manufacturers_from_ini_file(self) -> List[Manufacturer]:
        ini_parser = configparser.ConfigParser()
        ini_parser.read(self._file_name)
        manufacturer_list = []
        for section in ini_parser.sections():
            manufacturer_dictionary = {
                option: ini_parser.get(section, option)
                for option in ini_parser.options(section)
            }
            manufacturer_dictionary.update({"name": section})
            manufacturer_list.append(Manufacturer(**manufacturer_dictionary))
        return manufacturer_list

    def _save_manufacturers_to_ini_file(self) -> None:
        manufacturers_to_save = [p.dict() for p in self._manufacturers]
        parser = configparser.ConfigParser()
        for manufacturer in manufacturers_to_save:
            parser.add_section(manufacturer["name"])
            for k, v in manufacturer.items():
                if v and k != "name":
                    parser.set(manufacturer["name"], k, str(v))
        with open(self._file_name, "w") as configfile:
            parser.write(configfile)

    def get_manufacturer(self, id: int) -> Manufacturer:
        self._get_manufacturers_from_ini_file()
        for manufacturer in self._manufacturers:
            if manufacturer.id == id:
                return manufacturer
        raise ManufacturerNotFoundException(id)

    def create_manufacturer(self, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            self._manufacturers.append(manufacturer)
            self._save_manufacturers_to_ini_file()
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)

    def update_manufacturer(self, id: int, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            pass
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)
