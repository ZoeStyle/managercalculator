import logging


def info(msg: str):
    logging.basicConfig(filename='info.log', level=logging.INFO)
    logging.info(msg)


def error(msg: str):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(msg)


def warning(msg: str):
    logging.basicConfig(filename='warning.log', level=logging.WARNING)
    logging.warning(msg)
