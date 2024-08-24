from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from conf_secrest import configure


# Create engine with echo=True to see the SQL statements being executed
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
