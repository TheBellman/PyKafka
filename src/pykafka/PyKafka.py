import logging
import click
from pykafka.Config import Config
from pykafka.Producer import Producer
from pykafka.StringDataStream import StringDataStream

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--bootstrap-server', default='localhost:9092', help='Where to find kafka, assumed to be host:port')
@click.option('--topic', default='pykafka', help='The target topic to use')
@pass_config
def cli(config: Config, bootstrap_server: str, topic: str):
    """
    Simple demonstration of using Kafka producers/consumers.
    """
    config.bootstrap = bootstrap_server
    config.topic = topic


@cli.command()
@click.option('--count', default=100, help='Number of messages to produce')
@pass_config
def produce(config: Config, count: int):
    config.count = count
    datastream = StringDataStream()
    producer = Producer(config, datastream)
    producer.execute()


@cli.command()
@pass_config
def consume(config: Config):
    logging.info('Started')
    logging.info(f'Consuming with topic={config.topic}, bootstrap={config.bootstrap}')
    logging.info('Stopped')


if __name__ == "__main__":
    cli()
