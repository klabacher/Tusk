from Engine.Filter import Spheniscidae
from Engine.Matchmaking import removeFromQueue
class Penguin(Spheniscidae):
    def __init__(self, session, spirit):
        super(Penguin, self).__init__(session, spirit)
        self.PID = None
        self.name = "jjgay"#None
        self.objectId = 0
        self.token = None

        self.position = None
        self.nextPosition = None
        self.nextAttack = None

        self.health = 0
        self.nextCardXp = 0
        self.element = None
        self.tipsEnabled = True
        self.inQueue = False
        self.logger.info("Penguin class instantiated")

    def connectionLost(self, reason):
        #todo add conlost handling
        self.logger.warning("Connection Lost! "+str(reason))
        super(Penguin, self).connectionLost(reason)
        if self.inQueue:
            removeFromQueue(self)

    def getPowerCards(self,element):
        #todo: get player powercards from db
        if element == "snow":
            return 34
        if element == "water":
            return 12
        if element == "fire":
            return 52
        return 0
