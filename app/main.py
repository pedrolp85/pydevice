from typing import List

from exception_handler.exception_handler import exception_handler
from fastapi import Depends, FastAPI, Request
from model.device import Device
from repository import get_devices_repository
from repository.devices import DevicesRepository
from repository.exceptions import MyBaseException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "This is the PyDevice API root dir "}


@app.get("/device")
def get_devices(
    repository: DevicesRepository = Depends(get_devices_repository),
) -> List[Device]:
    return repository.get_devices()


@app.get("/device/{device_id}")
def get_device(
    device_id: int, repository: DevicesRepository = Depends(get_devices_repository)
) -> List[Device]:
    return repository.get_device(device_id)


@app.post("/device")
def create_device(
    device: Device, repository: DevicesRepository = Depends(get_devices_repository)
) -> None:
    print("create device")
    print("Entrypoint")
    repository.create_device(device)

# @app.put("/team/{team_id}")
# def update_team(
#     team_id: int,
#     team: Team,
#     repository: TeamsRepository = Depends(get_teams_repository),
# ) -> None:
#     repository.update_team(team_id, team)


# @app.get("/player")
# def get_players(
#     repository: PlayersRepository = Depends(get_players_repository),
# ) -> List[Team]:
#     return repository.get_players()

# @app.get("/player/{player_id}")
# def get_player(
#     player_id: int, repository: PlayersRepository = Depends(get_players_repository)
# ) -> List[Player]:
#     return repository.get_player(player_id)

# @app.post("/player")
# def create_player(
#     player: Player, repository: PlayersRepository = Depends(get_players_repository)
# ) -> None:
#     repository.create_player(player)

# Inyeccion de dependencias con FastAPI : https://fastapi.tiangolo.com/tutorial/dependencies/


@app.exception_handler(MyBaseException)
def unicorn_exception_handler(request: Request, exc: MyBaseException):
    return exception_handler(request, exc)


if __name__ == "__main__":  # pragma: no cover
    import uvicorn  # type: ignore

    uvicorn.run(app, host="0.0.0.0", port=8080, debug=DEBUG)
