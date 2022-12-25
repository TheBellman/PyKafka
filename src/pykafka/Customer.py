from dataclasses import dataclass


@dataclass
class Customer:
    """
    data object representing our Customer record
    """
    id: str
    name: str
