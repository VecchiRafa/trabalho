from models import Base, Person
from sqlalchemy import DATETIME, DATE,VARCHAR, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime, date

class NaturalPerson(Base):
    __tablename__ = "natural_person"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, 
                                            ForeignKey(Person.id),
                                            nullable=False,
                                            autoincrement=True,
                                            primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(200),nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    birth_date: Mapped[date] = mapped_column(DATE, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, 
                                                    nullable=False,
                                                    default=datetime.now())
 