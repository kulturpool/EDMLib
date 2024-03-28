from logging import getLogger, Handler, WARNING


logger = getLogger("edm-logger")
logger.setLevel(WARNING)

stoudHandler = Handler()
fileHandler = Handler()
dbHandler = Handler()
