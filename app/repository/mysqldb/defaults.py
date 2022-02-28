from repository.mysqldb.database import SessionLocal


def _get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

