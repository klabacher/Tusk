from Engine.Filter import Spheniscidae
from Engine.Matchmaking import removeFromQueue
from Data import penguin
class Penguin(Spheniscidae):
    def __init__(self, session, spirit):
        super(Penguin, self).__init__(session, spirit)
        self.PID = None
        self.objectId = 0
        self.name = None
        self.token = None
        self.session = session
        self.positionX = 0
        self.positionY = 0
        self.nextPositionX = 0
        self.nextPositionY = 0
        self.nextAttack = -1 #-1 no attack 1 attack 2 heal
        self.nextAttackX = 0
        self.nextAttackY = 0
        self.hp = None
        self.range = None
        self.power = None
        self.move = None
        self.nextCardXp = 0
        self.element = None
        self.tipsEnabled = True
        self.inQueue = False
        self.hasDisconnected = False
        self.usedPowerCard = False
        self.powerCardX=0
        self.powerCardY=0
        self.game = None
        self.isHost = False
        self.logger.info("Penguin class instantiated")

    def connectionLost(self, reason):
        #todo add conlost handling
        if self.inQueue:
            removeFromQueue(self)
        self.logger.warning("Connection Lost! "+str(reason))
        super(Penguin, self).connectionLost(reason)

    def getPowerCards(self,element):
        #todo: get player powercards from db
        if element == "snow":
            return 22
        if element == "water":
            return 12
        if element == "fire":
            return 5
        return 0
