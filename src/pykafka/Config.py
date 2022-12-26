class Config:
    """
    This class carries some configuration around
    """
    def __init__(self,
                 bootstrap: str = 'localhost:9092',
                 topic: str = 'pykafka',
                 count: int = 0,
                 schema_registry: str = 'http://localhost:8081'):
        self.bootstrap = bootstrap
        self.topic = topic
        self.count = count
        self.schema_registry = schema_registry
