"""Bot starts up through this launcher module."""
import click
import logging
import asyncio
import contextlib
from bot import DNDBot


@contextlib.contextmanager
def setup_logging():
    # __enter__
    logging.getLogger('discord').setLevel(logging.INFO)
    logging.getLogger('discord.http').setLevel(logging.WARNING)


def run_bot():
    bot = DNDBot()
    bot.run()


@click.group(invoke_without_command=True, options_metavar='[options]')
@click.pass_context
def main(ctx):
    """Launches the bot."""
    if ctx.invoked_subcommand is None:
        loop = asyncio.get_event_loop()
        with setup_logging():
            run_bot(loop)


if __name__ == '__main__':
    main()
