from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimal_hotel_pettt')
Session = sessionmaker(bind=engine)
