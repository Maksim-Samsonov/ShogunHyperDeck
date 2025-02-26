import asyncio
import logging
import argparse
from tkinter import *
import Window


def start(ip):
    logging.basicConfig(format='%(name)s %(levelname)s: %(message)s', level=logging.INFO)

    # Configure log level for the various modules.
    loggers = {
        'WebUI': logging.INFO,
        'HyperDeck': logging.INFO,
        'aiohttp': logging.ERROR,
    }
    for name, level in loggers.items():
        logger = logging.getLogger(name)
        logger.setLevel(level)

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("address", type=str, help="IP address of the HyperDeck to connect to")
    args = parser.parse_args({ip})
    return args
