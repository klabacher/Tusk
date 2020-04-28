from Engine.Filter import Spheniscidae

class Penguin(Spheniscidae):
    def __init__(self, session, spirit):
        super(Penguin, self).__init__(session, spirit)
        self.PID = 0
        self.objectId = 0
        self.token = None

        self.position = None
        self.nextPosition = None
        self.nextAttack = None

        self.health = 0
        self.nextCardXp = 0
        self.logger.info("Penguin class instantiated")

    def connectionLost(self, reason):
        #todo add conlost handling
        self.logger.warning("Connection Lost! "+str(reason))
        super(Penguin, self).connectionLost(reason)
