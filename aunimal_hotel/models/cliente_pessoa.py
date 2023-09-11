from models import Base, Pessoa
from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime, date

class ClientePessoa(Base):
    __tablename__ = "cliente_pessoa"
    id: Mapped[int] = mapped_column("id", MEDIUMINT,
                                            ForeignKey(Pessoa.id),
                                            nullable=False,
                                            autoincrement=True,
                                            primary_key=True)
                                            
    created_at: Mapped[datetime] = mapped_column(DATETIME, 
                                                    nullable=False,
                                                    default=datetime.now())
 