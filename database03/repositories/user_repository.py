from models.user import User
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh()

    def search_user_by_email(self, email: str):
        return self.session.query(User).filter_by(email=email).first()
    
    def delete_user(self, user: User):
        self.session.delete(user)
        self.session.commit()
        self.session.refresh()

    def list_all_users(self):
        return self.session.query(User).all()