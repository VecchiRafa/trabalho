from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote

# Configurações de conexão
db_user = "root"
db_password = "Brother25525&"
db_host = "localhost"
db_port = "3306"
db_name = "aunimal_hotel_pettt"
db_url = f"mysql+pymysql://{db_user}:{quote(db_password)}@{db_host}:{db_port}/{db_name}"

# Função para criar ou verificar a existência do banco de dados
def create_or_check_database(url):
    if not database_exists(url):
        create_database(url)

# Chamar a função para verificar ou criar o banco de dados
create_or_check_database(db_url)

# Crie uma instância do mecanismo e uma fábrica de sessões
engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()
Base.metadata.create_all(engine)