"""
User entity in the authentication domain
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
import uuid

from src.modules.auth.domain.password import Password

@dataclass
class User:
    """
    User entity represents an authenticated user in the system
    """
    id: str
    email: str
    password_hash: str
    is_active: bool
    role: str
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    @classmethod
    def create(cls, email: str, password: Password, role: str = "student") -> "User":
        """
        Create a new user with the given email and password
        """
        now = datetime.utcnow()
        return cls(
            id=str(uuid.uuid4()),
            email=email,
            password_hash=password.hash_value,
            is_active=True,
            role=role,
            created_at=now,
            updated_at=now
        )

    def verify_password(self, password: Password) -> bool:
        """
        Verify if the provided password matches the stored hash
        """
        return password.verify(self.password_hash)

    def update_password(self, new_password: Password) -> None:
        """
        Update the user's password hash
        """
        self.password_hash = new_password.hash_value
        self.updated_at = datetime.utcnow()

    def deactivate(self) -> None:
        """
        Deactivate the user account
        """
        self.is_active = False
        self.updated_at = datetime.utcnow()

    def reactivate(self) -> None:
        """
        Reactivate the user account
        """
        self.is_active = True
        self.updated_at = datetime.utcnow()

    def record_login(self) -> None:
        """
        Record a successful login
        """
        self.last_login = datetime.utcnow()
        self.updated_at = datetime.utcnow() 