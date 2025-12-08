from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db_url="postgresql+psycopg2://postgres:AcademyRootPassword@localhost:5432/empty_db"

engine=create_engine(db_url)

sessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()