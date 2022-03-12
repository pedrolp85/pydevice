from abc import ABCMeta, abstractmethod
from typing import List, Optional, Dict, Any

from .model.device import Device
from .model.manufacturer import Manufacturer
from .model.interface import  L3Interface


import requests

class FetchData(metaclass=ABCMeta):
    @abstractmethod
    def get_device(self, device_id: int) -> List[Device]:
        pass
    
    # @abstractmethod
    # def get_manufacturer(manufacturer_id: Optional[int]) -> List[Manufacturer]:
    #     pass

    # @abstractmethod
    # def get_interface(interface_id: Optional[int]) -> List[L3Interface]:
    #     pass

class FetchDataFromAPI(FetchData):

    _URL = "http://app"

    def _fetch_from_api(self, uri_path: str, constrains: Optional[str] = None ) -> List[Dict[str, Any]]:
        r = requests.get(
            f"{self._URL}/{uri_path}")
        
        data_fetched = r.json()
        return data_fetched

    def get_device(self, device_id: int) -> Device:
        pass

    def get_devices(self, manufacturer: Optional[str] = None) -> List[Device]:
        if manufacturer:
            devices_raw = self._fetch_from_api("device", f"manufacturer={manufacturer}" )
        else:    
            devices_raw = self._fetch_from_api("device")
        devices = [ Device(**p) for p in devices_raw ]
        return devices

def get_fetchdata() -> FetchData:
    return FetchDataFromAPI()

# current_time = 2022-03-05 10:26 -> 
  
# https://my-app.com/devices?expire_less="2022-03-05 10:31"&manufacturer=<manufacturer_id>

# $ scheduler --expire_less "" --manufacturer "cisco"
# $ scheduler --expire_less "" --manufacturer "paloalto"
# $ scheduler --expire_less "" --manufacturer "f5"

        
            