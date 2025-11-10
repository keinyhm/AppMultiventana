from dataclasses import dataclass

@dataclass
class users:
    """Un modelo de datos para guardar la info de un usuario."""
    id: int
    username: str
    password: str