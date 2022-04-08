import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.INFO,
    filename='logs.log')

logger = logging.getLogger()

def log_error(text):
    logger.error(text)

def log_info(text):
    logger.info(text)
