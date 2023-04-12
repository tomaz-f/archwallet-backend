from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DateTime, Float

Base = declarative_base()


class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    despesa = relationship('despesa', back_populates='categoria')
    receita = relationship('receita', back_populates='categoria')


class despesa(Base):
    __tablename__ = 'despesa'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship('categoria', back_populates='despesa')


class receita(Base):
    __tablename__ = 'receita'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship('categoria', back_populates='receita')


class usuario(Base):
    __tablename__ = 'usuario'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    usuario = Column('usuario', String, nullable=False, unique=True)
    senha = Column('senha', String, nullable=False)


class conta(Base):
    __tablename__ = 'conta'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    descricao = Column('descricao', String, nullable=False)
    saldo = Column('saldo', Float, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship('usuario', back_populates='conta')
