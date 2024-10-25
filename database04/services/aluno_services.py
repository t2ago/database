from database04.models.aluno import Aluno
from database04.repositories.aluno_repository import AlunoRepository

class AlunoService:
    def __init__(self, repository: AlunoRepository) -> None:
        self.repository = repository

    def create_aluno(self, ra: str, nome: str, sobrenome: str, email: str, senha: str):
        try:
            aluno = Aluno(ra=ra, nome=nome, sobrenome=sobrenome, email=email, senha=senha)
            self.repository.save_aluno(aluno)
            print("Aluno salvo!")
        except TypeError as erro:
            print(f"Erro ao salvar {erro}.")
        except Exception as erro:
            print(f"Erro inesperado {erro}.")
    
    def list_all_alunos(self):
        return self.repository.list_all_alunos()