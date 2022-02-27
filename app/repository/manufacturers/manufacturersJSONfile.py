import json
from pathlib import Path
from typing import List, Optional, Any

from model.manufacturer import Manufacturer
from pydantic.json import pydantic_encoder
from repository.exceptions import (
    ManufacturerAlreadyExistsException,
    ManufacturerNotFoundException,
)

from .manufacturers import ManufacturersRepository


class ManufacturersRepositoryJSONFile(ManufacturersRepository):
    def __init__(self, file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._manufacturers = (
            self._get_manufacturers_from_json_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return (
            Path(__file__).parent.parent.parent / self._file_source / "manufacturers.json"
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

    def create_manufacturer(self, manufacturer: Manufacturer) -> Any:
        try:
            self.get_manufacturer(manufacturer.id)
        except ManufacturerNotFoundException:
            self._manufacturers.append(manufacturer)
            self._save_manufacturers_to_json_file()
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
