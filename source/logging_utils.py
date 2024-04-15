import logging

logger = logging.getLogger("my-logger")
FORMAT = "[%(asctime)s] [%(filename)s:%(lineno)s - %(funcName)27s()] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.INFO)


def get_logger():
    return logger


def log_start_and_end(func):
    def inner():
        logger.info("Started")
        func()
        logger.info("Completed")

    return inner
