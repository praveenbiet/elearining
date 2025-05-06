"""
Repository for User persistence operations
"""
from typing import Optional, List
from sqlalchemy.orm import Session

from src.modules.auth.domain.user import User
from src.modules.auth.models.user import UserModel

class UserRepository:
    """
    Repository for User entities in the database
    """
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: User) -> UserModel:
        """
        Create a new user in the database
        """
        db_user = UserModel(
            id=user.id,
            email=user.email,
            password_hash=user.password_hash,
            is_active=user.is_active,
            role=user.role,
            created_at=user.created_at,
            updated_at=user.updated_at,
            last_login=user.last_login
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_by_id(self, user_id: str) -> Optional[UserModel]:
        """
        Get a user by ID
        """
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def get_by_email(self, email: str) -> Optional[UserModel]:
        """
        Get a user by email
        """
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def list_users(self, skip: int = 0, limit: int = 100) -> List[UserModel]:
        """
        Get a list of users
        """
        return self.db.query(UserModel).offset(skip).limit(limit).all()
    
    def update(self, user: User) -> UserModel:
        """
        Update a user in the database
        """
        db_user = self.get_by_id(user.id)
        if not db_user:
            raise ValueError(f"User with ID {user.id} not found")
        
        # Update fields
        db_user.email = user.email
        db_user.password_hash = user.password_hash
        db_user.is_active = user.is_active
        db_user.role = user.role
        db_user.updated_at = user.updated_at
        db_user.last_login = user.last_login
        
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def delete(self, user_id: str) -> None:
        """
        Delete a user from the database
        """
        db_user = self.get_by_id(user_id)
        if not db_user:
            raise ValueError(f"User with ID {user_id} not found")
        
        self.db.delete(db_user)
        self.db.commit()

    def to_domain(self, db_user: UserModel) -> User:
        """
        Convert a database model to a domain entity
        """
        return User(
            id=db_user.id,
            email=db_user.email,
            password_hash=db_user.password_hash,
            is_active=db_user.is_active,
            role=db_user.role,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
            last_login=db_user.last_login
        ) 