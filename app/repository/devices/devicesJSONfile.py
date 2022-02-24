import json
from pathlib import Path
from typing import List, Optional

from model.device import Device
from pydantic.json import pydantic_encoder
from repository.exceptions import DeviceAlreadyExistsException, DeviceNotFoundException

from .devices import DevicesRepository


class DevicesRepositoryJSONFile(DevicesRepository):
    def __init__(self, file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._devices = (
            self._get_devices_from_json_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return Path(__file__).parent.parent.parent / self._file_source / "inventory.json"

    def _get_devices_from_json_file(self) -> List[Device]:
        with open(self._file_name, mode="r") as f:
            raw_devices = f.read()
            devices = json.loads(raw_devices)
            return [Device(**p) for p in devices]
        return []

    def _save_devices_to_json_file(self) -> None:
        devices_to_save = [p.dict() for p in self._devices]
        with open(self._file_name, mode="w") as f:
            data = json.dumps(devices_to_save, indent=4, default=pydantic_encoder)
            f.write(data)

    def get_device(self, id: int) -> Device:
        self._get_devices_from_json_file()
        for device in self._devices:
            if device.id == id:
                return device
        raise DeviceNotFoundException(id)

    def create_device(self, device: Device) -> None:
        try:
            self.get_device(device.id)
        except DeviceNotFoundException:
            self._devices.append(device)
            self._save_devices_to_json_file()
        else:
            raise DeviceAlreadyExistsException(device.id)

    def update_device(self, id: int, device: Device) -> None:
        if not self.get_device(id):
            raise DeviceNotFoundException(id)
        else:
            pass
