from dataclasses import dataclass


@dataclass
class Config:
    """
    This class carries some configuration around
    """
    bootstrap: str = 'localhost:9092'
    topic: str = 'pykafka'
    count: int = 0
    schema_registry: str = 'http://localhost:8081'
