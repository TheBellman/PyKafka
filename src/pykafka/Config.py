"""
This class carries some configuration around
"""


class Config(object):

    def __init__(self, bootstrap='', topic='', count=0):
        self.bootstrap = bootstrap
        self.topic = topic
        self.count = count
