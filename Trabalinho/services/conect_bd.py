from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:Brother25525&@localhost/aunimal_hotel_pettt')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()