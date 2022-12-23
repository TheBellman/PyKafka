import pytest
from pykafka.Config import Config


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def full_config():
    return Config(count=500, topic='test', bootstrap='localhost:9092')


def test_config_construct(config):
    assert config.count is not None
    assert config.bootstrap is not None
    assert config.topic is not None


def test_full_config(full_config):
    assert full_config.count == 500
    assert full_config.bootstrap == 'localhost:9092'
    assert full_config.topic == 'test'
