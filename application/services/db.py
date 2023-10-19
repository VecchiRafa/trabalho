from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,  sessionmaker
from urllib.parse import quote

# Configurações de conexão
db_url = f"mysql+pymysql://root:{quote('Brother25525&')}@localhost:3306/aunimal_hotel_pettt"

# Verifique se o banco de dados já existe
if not database_exists(db_url):
    create_database(db_url)

# Crie uma instância do mecanismo e uma fábrica de sessões
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)

# Inicie a sessão
session = Session()


