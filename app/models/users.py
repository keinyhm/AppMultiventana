from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    password: str #contraseña con el hash ya aplicado