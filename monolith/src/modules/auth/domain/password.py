"""
Password value object in the authentication domain
"""
import re
import bcrypt
from dataclasses import dataclass

@dataclass
class Password:
    """
    Value object representing a password with hashing functionality
    and validation rules
    """
    value: str
    hash_value: str = ""

    def __post_init__(self):
        """
        After initialization, if no hash is provided, generate one
        """
        if not self.hash_value:
            self.hash_value = self._hash_password(self.value)

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hash a password using bcrypt
        """
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')

    def verify(self, hashed_password: str) -> bool:
        """
        Verify if the password matches the given hash
        """
        password_bytes = self.value.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    @classmethod
    def from_plain_text(cls, plain_text: str) -> "Password":
        """
        Create a Password object from plain text, validating it first
        """
        if not cls.is_valid(plain_text):
            raise ValueError("Password does not meet security requirements")
        return cls(value=plain_text)

    @staticmethod
    def is_valid(password: str) -> bool:
        """
        Validate password against security requirements:
        - At least 8 characters
        - Contains at least one digit
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one special character
        """
        if len(password) < 8:
            return False
        
        # Check for at least one digit
        if not re.search(r"\d", password):
            return False
        
        # Check for at least one uppercase letter
        if not re.search(r"[A-Z]", password):
            return False
        
        # Check for at least one lowercase letter
        if not re.search(r"[a-z]", password):
            return False
        
        # Check for at least one special character
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        
        return True 