import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
#logging.warn("Waring")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")
