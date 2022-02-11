import ipaddress
import json
from typing import Any, Dict

def build_type_dump(element: Dict[str,Any]) -> Dict[str,Any]:
    return_dict = {}
    for ke,va in element.items():
        print("esto es clave-valor")
        print(ke,va)
        if isinstance(va, dict):
            print("is nested")
            build_type_dump(va)
    else:
        for k,v in element.items():
            if isinstance(v,ipaddress.IPv4Address):
                print('es ip')
                return_dict[k] = str(v)
            else:
                return_dict[k] = v
    return return_dict

ip = ipaddress.IPv4Address('192.168.0.1')
dictionary = {"name": "yoyo", "ip_addres":ip}
dictionary_nested = {"name": "yoyo", "interface": {"ip_address": ip}}
data = json.loads.dumps(dictionary_nested, indent=4)
print(data)

#print(build_type_dump(dictionary))
#print(build_type_dump(dictionary_nested))