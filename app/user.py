from dataclasses import dataclass

@dataclass(slots=True)
class User:
    name: str
    password: str
    registration: str
    
    def __repr__(self) -> str:
        return f'User name: {self.name}, Password: {self.password}, Registered at: {self.registration}'