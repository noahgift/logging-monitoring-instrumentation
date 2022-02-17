#!/usr/bin/env python
from lib.randoFruit import fruity
import click

# LOGGING
import logging.config
logging.config.fileConfig("logging.conf")
LOGGER = logging.getLogger("simpleExample")

@click.command()
@click.option(
    "--time",
    default=2,
    help="How long to sleep",
)
@click.option(
    "--level",
    default=30,
    help="Sets log level",
)
def run(time, level):
    click.echo(click.style(f"Log Level {level}", fg="blue"))
    click.echo(click.style(f"Sleep {time}", fg="red"))
    LOGGER.setLevel(level)
    while True:
        LOGGER.debug("Debug level")
        LOGGER.info(fruity(interval=time))


if __name__ == '__main__':
    run()
