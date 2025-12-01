from sqlalchemy import String, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

engine = create_engine("sqlite:///banco.db", echo=True)
db = Session(engine)


class Base(DeclarativeBase):
    pass


class Veiculo(Base):
    __tablename__ = "veiculos"

    id: Mapped[int] = mapped_column(primary_key=True)
    placa: Mapped[str] = mapped_column(String(7), unique=True)
    frota_id: Mapped[int] = mapped_column(ForeignKey("frotas.id"))

    frota: Mapped["Frota"] = relationship(back_populates="veiculos")
    # o resto das colunas


class Frota(Base):
    __tablename__ = "frotas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(255))
    lista_veiculos: Mapped[Optional[List[int]]] = mapped_column(
        ForeignKey("veiculos.id")
    )

    veiculos: Mapped[Optional[List["Veiculo"]]] = relationship(
        back_populates="frota", cascade="all, delete-orphan"
    )
