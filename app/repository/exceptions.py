from abc import ABCMeta, abstractmethod
from typing import Any


class MyBaseException(Exception, metaclass=ABCMeta):
    @abstractmethod
    def error_description(self) -> str:
        pass


class ResourceException(MyBaseException):
    def __init__(self, id: Any) -> None:
        super().__init__()
        self._id = id


class ResourceAlreadyExistsException(ResourceException):
    def error_description(self):
        return f"Resource '{self._id}' already exists."


class DeviceAlreadyExistsException(ResourceAlreadyExistsException):
    def error_description(self):
        return f"Device '{self._id}' already exists."


class ManufacturerAlreadyExistsException(ResourceAlreadyExistsException):
    def error_description(self):
        return f"Manufacturer '{self._id}' already exists."


class InterfaceAlreadyExistsException(ResourceAlreadyExistsException):
    def error_description(self):
        return f"Interface '{self._id}' already exists."


class ResourceNotFoundException(ResourceException):
    def error_description(self):
        return f"Resource '{self._id}' does not exist."


class DeviceNotFoundException(ResourceNotFoundException):
    def error_description(self):
        return f"Resource '{self._id}' does not exist."


class ManufacturerNotFoundException(ResourceNotFoundException):
    def error_description(self):
        return f"Manufacturer '{self._id}' does not exist."


class InterfaceNotFoundException(ResourceNotFoundException):
    def error_description(self):
        return f"Interface '{self._id}' does not exist."
