from models import Base
from sqlalchemy import DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime

class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, 
                                            nullable=False,
                                            autoincrement=True,
                                            primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DATETIME, 
                                                    nullable=False,
                                                    default=datetime.now())
