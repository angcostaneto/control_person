
from dataclasses import dataclass


@dataclass
class PersonDto:
    id: str
    first_name: str
    last_name: str
    rg : str
    cpf: str
