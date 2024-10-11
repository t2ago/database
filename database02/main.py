import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///mydb.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ra = Column("ra", String)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    email = Column ("email", String)

    def __init__(self, ra: str, nome: str, idade: int, email: str):
        self.ra = ra
        self.nome = nome
        self.idade = idade
        self.email = email

Base.metadata.create_all(bind=db)

for i in range(2):
    os.system ("cls || clear")
    ra = input("Digite sua RA: ")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")

    aluno = Aluno(ra=ra, nome=nome, idade=idade, email=email)
    session.add(aluno)
    session.commit()

aluno = session.query(Aluno).filter_by(ra="99").first()
os.system ("cls || clear")

if aluno:
    session.delete(aluno)
    session.commit()
    print("Aluno deletado")
else:
    print("RA não encontrado.")

lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.email}")

print("\nAtualizando dados.")
ra_aluno = input("\nInforme o RA: ")

aluno = session.query(Aluno).filter_by(ra = ra_aluno).first()
os.system ("cls || clear")

if aluno:
    aluno.ra = input("Digite sua RA: ")
    aluno.nome = input("Digite seu nome: ")
    aluno.idade = input("Digite sua idade: ")
    aluno.email = input("Digite seu email: ")
    session.commit()
else:
    print("RA não encontrado.")

print("\nPesquisando dados.")
ra_aluno = input("\nInforme o RA: ")

aluno = session.query(Aluno).filter_by(ra = ra_aluno).first()
os.system ("cls || clear")

if aluno:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.email}")
else:
    print("RA não encontrado.")

session.close()