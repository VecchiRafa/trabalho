from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,  sessionmaker
from urllib.parse import quote

password = "Brother25525&"
instance = f"mysql+pymysql://root:{quote(password)}@localhost:3306/Auunimal"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)
Session = sessionmaker(bind=engine)