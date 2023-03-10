import pytest
from pykafka.Config import Config


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def full_config():
    return Config(count=500, topic='test', bootstrap='localhost:9092',  schema_registry='http://localhost:8081')


def test_config_construct(config):
    assert config.count == 0
    assert config.bootstrap == 'localhost:9092'
    assert config.topic == 'pykafka'
    assert config.schema_registry == 'http://localhost:8081'


def test_full_config(full_config):
    assert full_config.count == 500
    assert full_config.bootstrap == 'localhost:9092'
    assert full_config.topic == 'test'
    assert full_config.schema_registry == 'http://localhost:8081'
    assert str(full_config)\
           == "Config(bootstrap='localhost:9092', topic='test', count=500, schema_registry='http://localhost:8081')"
