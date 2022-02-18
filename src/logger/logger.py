import logging


def mount_message_log(msg: str, code: float) -> str:
    return str({
        'id': code,
        'message': msg
    })


def info(msg: str, code: float):
    logging.basicConfig(filename='app.log',
                        level=logging.INFO, encoding='utf-8')
    logging.info(mount_message_log(msg, code))


def error(msg: str, code: float):
    logging.basicConfig(filename='app.log',
                        level=logging.ERROR, encoding='utf-8')
    logging.error(mount_message_log(msg, code))
