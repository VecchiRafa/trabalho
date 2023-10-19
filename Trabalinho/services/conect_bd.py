from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:Brother25525&@localhost/aunimal_hotel_pettt')
Session = sessionmaker(bind=engine)
