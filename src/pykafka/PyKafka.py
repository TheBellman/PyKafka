import click
from pykafka.Config import Config
from pykafka.KafkaConsumer import KafkaConsumer
from pykafka.KafkaProducer import KafkaProducer
from pykafka.CustomerDataStream import CustomerDataStream

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--bootstrap-server', default='localhost:9092', help='Where to find kafka, assumed to be host:port'
                                                                   ' (defaults to locahost:9092)')
@click.option('--topic', default='pykafka', help='The target topic to use (defaults to pykafka)')
@click.option('--registry', default='http://localhost:8081', help='Location of schema registry '
                                                                  '(defaults to http://localhost:8081')
@pass_config
def cli(config: Config, bootstrap_server: str, topic: str, registry: str):
    """
    Simple demonstration of using Kafka producers/consumers.
    """
    config.bootstrap = bootstrap_server
    config.topic = topic
    config.schema_registry = registry


@cli.command()
@click.option('--count', default=100, help='Number of messages to produce (default 100)')
@pass_config
def produce(config: Config, count: int):
    config.count = count
    producer = KafkaProducer(config, CustomerDataStream())
    producer.execute()


@cli.command()
@pass_config
def consume(config: Config):
    consumer = KafkaConsumer(config)
    consumer.execute()


if __name__ == '__main__':
    cli()
