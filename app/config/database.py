from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:somepassword@contenedor-sql:3306/codigo_postal'
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
# )

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app/config/database.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()