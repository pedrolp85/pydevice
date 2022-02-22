from repository.devices import DevicesRepository
from repository.manufacturers.manufacturers import ManufacturersRepository
from repository.mysqldb.database import SessionLocal
from repository.mysqldb.devices import DevicesRepositoryDatabase
from repository.mysqldb.manufacturers import ManufacturersRepositoryDatabase


def _get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_devices_repository() -> DevicesRepository:
    return DevicesRepositoryDatabase(next(_get_db()))


def get_manufacturers_repository() -> ManufacturersRepository:
    return ManufacturersRepositoryDatabase(next(_get_db()))
