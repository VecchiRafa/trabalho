
from services.database import session
from models import NaturalPerson
from utils.database_utils import create_db
# python -m pip install pymysql sqlalchemy sqlalchemy-utils

if __name__ == "__main__":
    print("Criando o Banco de Dados!!")
    create_db()
    
    
    #person_list: list[NaturalPerson] = session.query(NaturalPerson).all()