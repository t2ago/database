import os
import sys
sys.path.append('/workspaces/database')

from models.aluno import Aluno
from services.aluno_services import AlunoService
from repositories.aluno_repository import AlunoRepository
from config.connection import Session

def main():
    session = Session()
    repository = AlunoRepository(session)
    service = AlunoService(repository)

    for i in range(1):
        os.system ("cls || clear")
        ra = input("Digite sua RA: ")
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        aluno = Aluno(ra=ra, nome=nome, sobrenome=sobrenome, email=email, senha=senha)
        session.add(aluno)
        session.commit()

    print("\nListando dados.")
    alunos = service.list_all_alunos()

    for aluno in alunos:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

if __name__ == "__main__":
    main()