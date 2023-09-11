from models import Base, Pessoa
from sqlalchemy import VARCHAR, ForeignKey, TIMESTAMP, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime, date

