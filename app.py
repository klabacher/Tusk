'<cross-domain-policy><allow-access-from domain="*" to-ports="*" /></cross-domain-policy>'
import logging, sys, json, os, signal, logging
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter
from Config import config
from Utils.EventManeger import EventHandler
#from Handlers import Login
from Engine.Engine import CJSnowFactory
from twisted.internet import protocol, reactor, task
from twisted.python import log



log.startLogging(sys.stdout)
def InitiateColorLogger(name='cjsnow'):

    cjsnow_logger = logging.getLogger("cjsnow")

    cjsnow_stream = logging.StreamHandler()

    LogFormat = "  %(reset)s%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s"
    cjsnow_stream.setFormatter(ColoredFormatter(LogFormat, log_colors={
        'DEBUG': 'white',
        'INFO': 'cyan',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'black,bg_red',
        'TAG': 'white',
    }))
    cjsnow_logger.addHandler(cjsnow_stream)

    cjsnow_logger.setLevel(logging.DEBUG)
    return cjsnow_logger

CjsnowLogger = InitiateColorLogger()
logger = logging.getLogger("cjsnow")
def onExitSignal(*a):
    logger.warning("closing?")
    if not reactor.running:
        os._exit(1)
    else:
        reactor.callFromThread(reactor.stop)

for sig in (signal.SIGABRT, signal.SIGILL, signal.SIGINT, signal.SIGSEGV, signal.SIGTERM):
    signal.signal(sig, onExitSignal)

server = CJSnowFactory(server="Login")
server.start()