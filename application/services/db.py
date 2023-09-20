from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

instance = f"mysql+pymysql://root:{quote('2n#*uB?w!r_O')}@localhost:3306/aunimal_hotel_Pet"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)

#engine = create_engine('mysql://root:Brother25525&@localhost/aunimalhotel')
#Session = sessionmaker(bind=engine)