import logging
import os
import time
import click

LOGS_DIR = os.getenv('LOGS_DIR', './logs')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


@click.command()
@click.option('--count', default=100, help='Number of messages to produce')
@click.option('--topic', default='pykafka', help='The target topic to use')
@click.option('--bootstrap-server', default='localhost:9092', help='Where to find kafka, assumed to be host:port')
def main(bootstrap_server, topic, count):
    """
    Simple demonstration of using Kafka producers/consumers.
    """
    logging.info('Started')
    logging.info(f'Executing with count={count}, topic={topic}, bootstrap={bootstrap_server}')
    logging.info('Stopped')


if __name__ == "__main__":
    main()
