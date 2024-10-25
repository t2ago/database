from services.user_services import UserService
from repositories.user_repository import UserRepository
from config.connection import Session

def main():
    session = Session()
    repository = UserRepository(session)
    service = UserService(repository)

    service.create_user("Ana", "Ana", "ana@gmail.com", "123")

    print("\nListando dados.")
    users = service.list_all_users()

    for user in users:
        print(f"{user.nome} - {user.sobrenome} - {user.email} - {user.senha}")

if __name__ == "__main__":
    main()