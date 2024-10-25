from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, nome: str, sobrenome: str, email: str, senha: str):
        try:
            user = User(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
            self.repository.save_user(user)
            print("Usuário salvo!")
        except TypeError as erro:
            print(f"Erro ao salvar {erro}.")
        except Exception as erro:
            print(f"Erro inesperado {erro}.")

    def list_all_users(self):
        return self.repository.list_all_users()