from database04.models.aluno import Aluno
from sqlalchemy.orm import Session

class AlunoRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save_aluno(self, aluno: Aluno):
        self.session.add(aluno)
        self.session.commit()
        self.session.refresh()

    def search_aluno_by_email(self, email: str):
        return self.session.query(Aluno).filter_by(email=email).first()
    
    def delete_user(self, user: Aluno):
        self.session.delete(aluno)
        self.session.commit()
        self.session.refresh()

    def list_all_users(self):
        return self.session.query(Aluno).all()