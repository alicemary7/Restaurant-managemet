from db.database import sessionLocal

def connect_to_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

