from Engine.Filter import Spheniscidae

class Penguin(Spheniscidae):
    def __init__(self, session, spirit):
        super(Penguin, self).__init__(session, spirit)
        self.PID
        self.objectId
        self.token

        self.position
        self.nextPosition
        self.nextAttack

        self.health
        self.nextCardXp
        self.logger.info("Penguin class instantiated")

    def connectionLost(self, reason):
        #todo add conlost handling
        self.logger.warning("Connection Lost! "+str(reason))
        super(Penguin, self).connectionLost(reason)
