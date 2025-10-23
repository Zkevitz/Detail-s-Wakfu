import logging
from logging.handlers import RotatingFileHandler

infoLogger = logging.getLogger("Info")
infoLogger.setLevel(logging.INFO)
errorLogger = logging.getLogger("Error")
errorLogger.setLevel(logging.ERROR)

consoleErrorhandler = logging.StreamHandler()
consoleErrorhandler.setLevel(logging.ERROR)

consoleInfohandler = logging.StreamHandler()
consoleInfohandler.setLevel(logging.INFO)

fileHandler = RotatingFileHandler(
    "error.log",
    maxBytes=1024*1024*5,
    backupCount=5,
    encoding="utf-8"
)
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleErrorhandler.setFormatter(formatter)
consoleInfohandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

infoLogger.addHandler(consoleInfohandler)
infoLogger.addHandler(fileHandler)
errorLogger.addHandler(consoleErrorhandler)
errorLogger.addHandler(fileHandler)
