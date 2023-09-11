from services.database import session
from models import ClientePessoa
from utils.database_utils import create_db

if __name__ == "__main__":
    print("Criando o Banco de Dados!!")
    create_db()
