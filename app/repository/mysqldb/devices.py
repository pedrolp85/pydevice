from typing import Optional

from model.device import Device
from repository.devices import DevicesRepository
from repository.exceptions import DeviceNotFoundException
from sqlalchemy.orm import Session

from . import models


class DevicesRepositoryDatabase(DevicesRepository):
    def __init__(
        self, db: Session, skip: Optional[int] = 0, limit: Optional[int] = 100
    ) -> None:
        self._session = db
        self._devices = (
            self._session.query(models.Device).offset(skip).limit(limit).all()
        )

    # def get_devices(self, skip: int = 0, limit: int = 100) -> List[Team]:
    #     return self._session.query(models.Team).offset(skip).limit(limit).all()

    def get_device(self, device_id: int) -> Device:
        device = (
            self._session.query(models.Device)
            .filter(models.Device.id == device_id)
            .first()
        )
        if not device:
            raise DeviceNotFoundException(team_id)
        return device

    def create_device(self, device: Device) -> None:
        pass

    def update_device(self, id: int, device: Device) -> None:
        pass

    # def create_team(self, team: Team) -> None:
    #     db_team = models.TeamDataBase(name=team.name, abbreviation=team.abbreviation, conference=team.conference, division=team.division)
    #     self._session.add(db_team)
    #     self._session.commit()
    #     self._session.refresh(db_team)
    #     return db_team

    # def update_team(self, id: int, team: Team) -> None:
    #     pass
