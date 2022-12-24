class Config:
    """
    This class carries some configuration around
    """
    def __init__(self, bootstrap: str = '', topic: str = '', count: int = 0):
        self.bootstrap = bootstrap
        self.topic = topic
        self.count = count
