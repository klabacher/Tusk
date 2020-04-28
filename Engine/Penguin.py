from Engine.Filter import Spheniscidae

class Penguin(Spheniscidae):
    def __init__(self, session, spirit):
        super(Penguin, self).__init__(session, spirit)
        self.user = None
        self.throttle = {}

        self.frame = 1
        self.x, self.y = (0, 0)
        self.age = 0
        self.muted = False
        self.playerString = None

        self.table = None
        self.waddle = None
        self.gameFinished = True

        self.logger.info("Penguin class instantiated")
    
    def connectionLost(self, reason):
        #todo add conlost handling
        self.logger.warning("Connection Lost! "+str(reason))
        super(Penguin, self).connectionLost(reason)