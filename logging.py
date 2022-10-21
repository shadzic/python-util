# Extensive guide to logging: https://www.toptal.com/python/in-depth-python-logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

logger.info("This is a very informative message, have a great day!")
