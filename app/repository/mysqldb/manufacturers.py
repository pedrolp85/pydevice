from typing import Optional

from model.manufacturer import Manufacturer
from repository.exceptions import ManufacturerNotFoundException
from repository.manufacturers.manufacturers import ManufacturersRepository
from sqlalchemy.orm import Session

from . import models


class ManufacturersRepositoryDatabase(ManufacturersRepository):
    def __init__(
        self, db: Session, skip: Optional[int] = 0, limit: Optional[int] = 100
    ) -> None:
        self._session = db
        self._manufacturers = (
            self._session.query(models.Manufacturer).offset(skip).limit(limit).all()
        )

    # def get_devices(self, skip: int = 0, limit: int = 100) -> List[Team]:
    #     return self._session.query(models.Team).offset(skip).limit(limit).all()

    def get_manufacturer(self, manufacturer_id: int) -> Manufacturer:
        manufacturer = (
            self._session.query(models.Manufacturer)
            .filter(models.Manufacturer.id == manufacturer_id)
            .first()
        )
        if not manufacturer:
            raise ManufacturerNotFoundException(manufacturer_id)
        return manufacturer

    def create_manufacturer(self, manufacturer: Manufacturer) -> None:
        pass

    def update_manufacturer(self, id: int, manufacturer: Manufacturer) -> None:
        pass

    # def create_team(self, team: Team) -> None:
    #     db_team = models.TeamDataBase(name=team.name, abbreviation=team.abbreviation, conference=team.conference, division=team.division)
    #     self._session.add(db_team)
    #     self._session.commit()
    #     self._session.refresh(db_team)
    #     return db_team

    # def update_team(self, id: int, team: Team) -> None:
    #     pass
