import logging
import click
from pykafka.Config import Config

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
def cli(config, bootstrap_server, topic):
    """
    Simple demonstration of using Kafka producers/consumers.
    """
    config.bootstrap = bootstrap_server
    config.topic = topic


@cli.command()
@click.option('--count', default=100, help='Number of messages to produce')
@pass_config
def produce(config, count):
    config.count = count
    logging.info('Started')
    logging.info(f'Executing with count={config. count}, topic={config.topic}, bootstrap={config.bootstrap}')
    logging.info('Stopped')


@cli.command()
@pass_config
def consume(config):
    logging.info('Started')
    logging.info(f'Consuming with topic={config.topic}, bootstrap={config.bootstrap}')
    logging.info('Stopped')


if __name__ == "__main__":
    cli()
