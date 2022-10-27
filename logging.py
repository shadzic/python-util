# Extensive guide to logging: https://www.toptal.com/python/in-depth-python-logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

logger.info("This is a very informative message, have a great day!")


# we can put this in a function and then import in the rest of the files:
def get_logger(name):

	logger = logging.getLogger(name)
	console_handler = logging.StreamHandler()
	logger.addHandler(console_handler)
	logger.setLevel(logging.DEBUG)

	return logger

# in the other files: 
logger = get_logger(__name__)
