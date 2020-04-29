'<cross-domain-policy><allow-access-from domain="*" to-ports="*" /></cross-domain-policy>'
import logging, sys, json, os, signal, logging, importlib, pkgutil
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter
from Config import config
from twisted.internet import protocol, reactor, task
from twisted.internet.protocol import Factory
from twisted.python import log
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from twisted.internet import reactor, task
from twisted.internet.protocol import Factory
from Engine.Filter import Spheniscidae
from Engine.Penguin import Penguin
import Handlers

class CJSnowFactory(Factory):
    def __init__(self, *args, **kwargs):
        self.serverName = kwargs["server"]
        self.config = config
        engineString = "postgresql+{0}://{1}:{2}@{3}/{4}".format(
            self.config["Database"]["Driver"].lower(),
            self.config["Database"]["User"],
            self.config["Database"]["Password"],
            self.config["Database"]["Address"],
            self.config["Database"]["DB"])
        self.logger = logging.getLogger("cjsnow")

        self.databaseEngine = create_engine(engineString, pool_recycle=3600, pool_pre_ping=True)
        self.createSession = sessionmaker(bind=self.databaseEngine)
        self.session = None

        self.sessionValidator = task.LoopingCall(self.validateSession)
        self.sessionValidator.start(20)

        self.players = {}
        self.protocol = Penguin
        self.logger.info("Houdini module initialized")

        self.handlers = {}
        self.loadHandlerModules()

    def validateSession(self):
        if self.session is not None and len(self.players) == 0:
            self.session.close()

            self.session = None

    def loadHandlerModules(self, strictLoad=None, excludeLoad=None):
        for handlerModule in self.getPackageModules(Handlers):
            if not (strictLoad and handlerModule not in strictLoad or excludeLoad and handlerModule in excludeLoad):
                if handlerModule not in sys.modules.keys():
                    importlib.import_module(handlerModule)
        self.logger.info("Handler modules loaded")

    def getPackageModules(self, package):
        packageModules = []
        for importer, moduleName, isPackage in pkgutil.iter_modules(package.__path__):
            fullModuleName = "{0}.{1}".format(package.__name__, moduleName)
            if isPackage:
                subpackageObject = importlib.import_module(fullModuleName, package=package.__path__)
                subpackageObjectDirectory = dir(subpackageObject)
                if "Plugin" in subpackageObjectDirectory:
                    packageModules.append((subpackageObject, moduleName))
                    continue
                subPackageModules = self.getPackageModules(subpackageObject)
                packageModules = packageModules + subPackageModules
            else:
                packageModules.append(fullModuleName)

        return packageModules

    def buildProtocol(self, addr):
        if self.session is None:
            self.session = self.createSession()
        player = self.protocol(self.session, self)
        return player

    def start(self):
        self.logger.info("Starting server..")

        port = 7002

        self.logger.info("Listening on port {0}".format(port))

        reactor.listenTCP(port, self)
        reactor.run()

