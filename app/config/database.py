import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:somepassword@contenedor-sql:3306/codigo_postal'
# engine = _sql.create_engine(
#     SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
# )

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app/config/database.db'
engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}
)


SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()