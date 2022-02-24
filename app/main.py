from functools import lru_cache
import logging
from typing import List, Optional

from exception_handler.exception_handler import (
    default_exception_handler,
    exception_handler,
)
from fastapi import Depends, FastAPI, Request, Cookie
from model.device import Device
from model.interface import L3Interface
from model.manufacturer import Manufacturer
from repository.devices import get_devices_repository
from repository.devices.devices import DevicesRepository
from repository.exceptions import MyBaseException
from repository.interfaces import get_interfaces_repository
from repository.interfaces.interfaces import InterfacesRepository
from repository.manufacturers import get_manufacturers_repository
from repository.manufacturers.manufacturers import ManufacturersRepository

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logging.basicConfig(level=logging.DEBUG)


app = FastAPI()


@app.get("/")
def read_root():
    logging.debug(f"PyDevice GET /")
    return {"Hello": "This is the PyDevice API root dir "}

@app.get("/device")
def get_devices(repository: DevicesRepository = Depends(get_devices_repository),
            manufacturer: Optional[str] = None) -> List[Device]: 
    print("en get_devices main")
    print(repository)
    return repository.get_devices(manufacturer)

@app.get("/device/{device_id}")
def get_device(
    device_id: int,
    repository: DevicesRepository = Depends(get_devices_repository)
) -> List[Device]:
    logging.debug(f"'PyDevice GET /device'{device_id}")
    return repository.get_device(device_id)

@app.post("/device")
def create_device(
    device: Device,
    repository: DevicesRepository = Depends(get_devices_repository),
) -> Device:
    logging.debug(f"PyDevice POST /device")
    print("BBBBBBBBBBBBBBBBBBBBBB")
    
    return repository.create_device(device)




@app.get("/manufacturer")
def get_manufacturers(
    repository: ManufacturersRepository = Depends(
        get_manufacturers_repository)
        ) -> List[Manufacturer]:
    logging.debug(f"PyDevice GET /manufacturer")
    return repository.get_manufacturers()

@app.get("/manufacturer/{manufacturer_id}")
def get_manufacturer(
    manufacturer_id: int,
    repository: ManufacturersRepository = Depends(
        get_manufacturers_repository
    ),
) -> List[Manufacturer]:
    logging.debug(f"PyDevice GET /manufacturer/{manufacturer_id}")
    return repository.get_manufacturer(manufacturer_id)


@app.get("/interface")
def get_interfaces(
    repository: InterfacesRepository = Depends(
        get_interfaces_repository
    ),
    device_id: Optional[int] = None,
) -> List[L3Interface]:
    logging.debug(f"PyDevice GET /interface/?device_id={device_id}")
    return repository.get_interfaces()

@app.get("/interface/{interface_id}")
def get_interface(
    interface_id: int,
    repository: InterfacesRepository = Depends(
        get_interfaces_repository
    ),
    device_id: Optional[int] = None,
) -> List[L3Interface]:
    logging.debug(f"PyDevice GET /interface/?interface_id={interface_id}")
    return repository.get_interface(interface_id)





# @app.post("/manufacturer")
# def create_device(
#     manufacturer: Manufacturer,
#     repository: ManufacturersRepository = Depends(
#         get_manufacturers_repository(settings.inventory_source)
#     ),
# ) -> None:
#     logging.debug(f"PyDevice POST /manufacturer")
#     repository.create_manufacturer(manufacturer)


# # @app.put("/team/{team_id}")
# # def update_team(
# #     team_id: int,
# #     team: Team,
# #     repository: TeamsRepository = Depends(get_teams_repository),
# # ) -> None:
# #     repository.update_team(team_id, team)


# # @app.get("/player")
# # def get_players(
# #     repository: PlayersRepository = Depends(get_players_repository),
# # ) -> List[Team]:
# #     return repository.get_players()

# # @app.get("/player/{player_id}")
# # def get_player(
# #     player_id: int, repository: PlayersRepository = Depends(get_players_repository)
# # ) -> List[Player]:
# #     return repository.get_player(player_id)

# # @app.post("/player")
# # def create_player(
# #     player: Player, repository: PlayersRepository = Depends(get_players_repository)
# # ) -> None:
# #     repository.create_player(player)

# # Inyeccion de dependencias con FastAPI : https://fastapi.tiangolo.com/tutorial/dependencies/


@app.exception_handler(MyBaseException)
def unicorn_exception_handler(request: Request, exc: MyBaseException):
    return exception_handler(request, exc)


@app.exception_handler(Exception)
def unicorn_default_exception_handler(request: Request, exc: MyBaseException):
    return default_exception_handler(request, exc)


if __name__ == "__main__":  # pragma: no cover
    import uvicorn  # type: ignore

    uvicorn.run(app, host="0.0.0.0", port=8080, debug=DEBUG)
