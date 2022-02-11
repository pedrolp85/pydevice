import json
import yaml
import configparser
from pydantic.json import pydantic_encoder
from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import List, Any, Dict

from model.device import Device, Device_State
from repository.exceptions import (
    DeviceAlreadyExistsException,
    DeviceNotFoundException)


class DevicesRepository(metaclass=ABCMeta):
    
    @abstractmethod
    def get_device(self, id: int) -> Device:
        pass

    @abstractmethod
    def create_device(self, device: Device) -> None:
        pass

    @abstractmethod
    def update_device(self, id: int, device: Device) -> None:
        pass
    
    def get_devices(self) -> List[Device]:
        return self._devices

class DevicesRepositoryJSONFile(DevicesRepository):
    def __init__(self, file_name: str = "inventory.json") -> None:
        self._file_name = file_name
        self._devices = (
            self._get_devices_from_json_file() if Path(file_name).is_file()
            else [])

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

    # def get_devices(self) -> List[Device]:
    #     return self._devices

    def get_device(self, id: int) -> Device:
        self._get_devices_from_json_file()
        for device in self._devices:
            if device.id == id:
                return device
        raise DeviceNotFoundException(id)

    def create_device(self, device: Device) -> None:
        for dev in self._devices:
            if dev.id == id:
                raise DeviceAlreadyExistsException(device.id)
        else:
            self._devices.append(device)
            self._save_devices_to_json_file()

    def update_device(self, id: int, device: Device) -> None:
        if not self.get_device(id):
            raise DeviceNotFoundException(id)
        else:
            pass

class DevicesRepositoryINIFile(DevicesRepository):
    
    def __init__(self, file_name: str = "inventory.ini") -> None:
        self._file_name = file_name
        self._devices = (
            self._get_devices_from_ini_file() if Path(file_name).is_file()
            else [])

    def _get_devices_from_ini_file(self) -> List[Device]:
        ini_parser = configparser.ConfigParser()
        ini_parser.read(self._file_name)
        device_list = []
        for section in ini_parser.sections():
            device_dictionary = { option : ini_parser.get(section,option) for option in ini_parser.options(section) if option != 'mgmt_interface' and option != 'state'}
            device_dictionary.update({ "name": section})
            mgmt_values = ini_parser.get(section,"mgmt_interface").split(',')
            mgmt_interface_dict = {"id": mgmt_values[0], "name": mgmt_values[1], "ip_address": mgmt_values[2]}   
            device_dictionary.update({ "mgmt_interface": mgmt_interface_dict })
            #device_dictionary.update({ "state": Device_State((ini_parser.get(section,"state"))) })
            device_list.append(Device(**device_dictionary))
        
        return device_list
                        
    def _save_devices_to_ini_file(self) -> None:
        devices_to_save = [p.dict() for p in self._devices]
        parser = configparser.ConfigParser()
        for device in devices_to_save:
            parser.add_section(device['name'])
            for k,v in device.items():
                if v and k != 'name':
                    if k != 'mgmt_interface':
                        parser.set(device['name'],k,str(v))
                    else:
                        parser.set(device['name'],k,",".join([ str(e) for e in v.values() ]))
        
        with open('inventory.ini', 'w') as configfile:
            parser.write(configfile)       

    def get_device(self, id: int) -> Device:
        for device in self._devices:
            if device.id == id:
                return device
        raise DeviceNotFoundException(id)        

    def create_device(self, device: Device) -> None:
        for dev in self._devices:
            if dev.id == id:
                raise DeviceAlreadyExistsException(device.id)
        self._devices.append(device)                
        self._save_devices_to_ini_file()

        # Así estaba el código original, no fucniona el if porque se hace un raise y se detiene
        # Hay 2 formas de hacerlo, una es no llamando a get_device, la otra es llamando con un catch
        # de la excepcion y continuar
        # if self.get_device(device.id):
        #     print("obtuvimps device")
        #     raise DeviceAlreadyExistsException(device.id)
        # else:
        #     print("no obtuvimos ningun device")
        #     print(device)

    def update_device(self, id: int, device: Device) -> None:
        pass

class DevicesRepositoryYAMLFile(DevicesRepository):
    
    def __init__(self, file_name: str = "inventory.yml") -> None:
        self._file_name = file_name
        self._devices = (
            self._get_devices_from_yaml_file() if Path(file_name).is_file()
            else [])

    def _get_devices_from_yaml_file(self) -> List[Device]:
        with open(self._file_name) as file:
            devices_raw = yaml.full_load(file)
            device_list = []
            for device in devices_raw:
                d = list(device.values())[0]
                d.update({"name": list(device.keys())[0]})
                device_list.append(Device(**d))
            return device_list
    
    def _build_type_dump(element: Dict[str,Any]) -> Dict[str,Any]:
        return_dict = {}
        if isinstance(v, dict):
            pass
        else:
            for k,v in element.values():
                if isinstance(v,ipaddress.IPV4Adress):
                    return_dict[k] = str(v)
                else:
                    return_dict[k] = values
        return return_dict            
                
            

    
    def _save_devices_to_yaml_file(self) -> None:
        devices_to_save = [p.dict() for p in self._devices]
        for device in devices_to_save:
            pass
        # for p in self._devices:
        #     d = dict({})
        #     dic = dict({})
        #     for k,v in p.dict().items():
        #         print(k)
        #         if k == "ip_address":
        #             print("Esto es una IP")
        #             d[k] = str(v)
        #         elif k == "name":
        #             pass
        #         else:
        #             d[k] = v
        #     dic[p.name] = d
        #     print(dic)
        #     devices_to_save.append(dic)
            
            # device_dict = p.dict()
            # yaml_object = dict({})
            # yaml_object.update({device_dict["name"]: None})
            # device_dict.pop("name")
            # yaml_object.update({p.name: device_dict})
            # devices_to_save.append(yaml_object)
            # print(yaml_object)
        with open('inventory.yml', 'w') as file:
            write = yaml.dump(devices_to_save, file)        

    def get_device(self, id: int) -> Device:
        for device in self._devices:
            if device.id == id:
                return device
        raise DeviceNotFoundException(id)        

    def create_device(self, device: Device) -> None:
        for dev in self._devices:
            if dev.id == id:
                raise DeviceAlreadyExistsException(device.id)
        self._devices.append(device)                
        self._save_devices_to_yaml_file()

        # Así estaba el código original, no fucniona el if porque se hace un raise y se detiene
        # Hay 2 formas de hacerlo, una es no llamando a get_device, la otra es llamando con un catch
        # de la excepcion y continuar
        # if self.get_device(device.id):
        #     print("obtuvimps device")
        #     raise DeviceAlreadyExistsException(device.id)
        # else:
        #     print("no obtuvimos ningun device")
        #     print(device)

    def update_device(self, id: int, device: Device) -> None:
        pass