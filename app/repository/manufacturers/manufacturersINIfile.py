import configparser
from pathlib import Path
from typing import List, Optional, Any

from model.manufacturer import Manufacturer
from repository.exceptions import (
    ManufacturerAlreadyExistsException,
    ManufacturerNotFoundException,
)

from .manufacturers import ManufacturersRepository


class ManufacturersRepositoryINIFile(ManufacturersRepository):
    def __init__(self, file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._manufacturers = (
            self._get_manufacturers_from_ini_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return (
            Path(__file__).parent.parent.parent / self._file_source / "manufacturers.ini"
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

    def create_manufacturer(self, manufacturer: Manufacturer) -> Any:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            self._manufacturers.append(manufacturer)
            self._save_manufacturers_to_ini_file()
            return manufacturer
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)

    def update_manufacturer(self, id: int, manufacturer: Manufacturer) -> None:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            pass
        else:
            raise ManufacturerAlreadyExistsException(manufacturer.id)
