from typing import Optional

from model.interface import L3Interface
from .interfaces import InterfacesRepository
from repository.exceptions import InterfaceNotFoundException
from sqlalchemy.orm import Session

from sqldb import models


class InterfacesRepositoryDatabase(InterfacesRepository):
    def __init__(
        self, db: Session, skip: Optional[int] = 0, limit: Optional[int] = 100
    ) -> None:
        self._session = db
        self._interfaces = (
            self._session.query(models.L3Interface).offset(skip).limit(limit).all()
        )

    # def get_devices(self, skip: int = 0, limit: int = 100) -> List[Team]:
    #     return self._session.query(models.Team).offset(skip).limit(limit).all()

    def get_interface(self, Interface_id: int) -> L3Interface:
        interface = (
            self._session.query(models.L3Interface)
            .filter(models.Interface.id == interface_id)
            .first()
        )
        if not interface:
            raise DeviceNotFoundException(interface_id)
        return interface

    def create_interface(self, interface: L3Interface) -> L3Interface:
        pass

    def update_interface(self, id: int, interface: L3Interface) -> L3Interface:
        pass

    # def create_team(self, team: Team) -> None:
    #     db_team = models.TeamDataBase(name=team.name, abbreviation=team.abbreviation, conference=team.conference, division=team.division)
    #     self._session.add(db_team)
    #     self._session.commit()
    #     self._session.refresh(db_team)
    #     return db_team

    # def update_team(self, id: int, team: Team) -> None:
    #     pass