from Utils.GameData import GameData as GD
class GameEngine(object):
    def __init__(self, fireclient, waterclient, snowclient):
        self.fclient = fireclient
        self.wclient = waterclient
        self.sclient = snowclient
        self.round = 1
        self.map = None
        loadGame()

    def loadGame():
        chooseRandomMap()
        while not hasWonGame() and not hasLost():
            doNextRound()
        goToPayout()
        return

    def doNextRound():
        playRoundTitle(self.round-1)
        for x in GD["Enemy"]:
            if x["Round"+self.round][x] is not -1:
                createAndSpawnEnemy(x)
        while not hasWonRound() and not hasLost():
            showGrid()
            if not self.fclient.hasDisconnected:
                getMoves(self.fclient)
            if not self.wclient.hasDisconnected:
                getMoves(self.wclient)
            if not self.sclient.hasDisconnected:
                getMoves(self.sclient)
            startTimer()
            hideTimer()
            hideGrid()
            if not self.fclient.hasDisconnected and not self.fclient.usedPowerCard:
                moveAndAttack(self.fclient)
            if not self.wclient.hasDisconnected and not self.wclient.usedPowerCard:
                moveAndAttack(self.wclient)
            if not self.sclient.hasDisconnected and not self.sclient.usedPowerCard:
                moveAndAttack(self.sclient)
            if self.fclient.usedPowerCard:
                playPowerCard(fclient)
            if self.wclient.usedPowerCard:
                playPowerCard(wclient)
            if self.sclient.usedPowerCard:
                playPowerCard(sclient)
            for x in GD["Enemy"]:
                if x["Round"+self.round][x] is not -1:
                    #todo: check if hp <=0
                    moveAndAttackEnemy(x)
        if hasWonRound()
            self.round+=1



class Enemy(object):
    def __init__(self, name, id, round):
        self.name = name
        self.id = id
        self.hp = GD["Enemy"][name]["HP"]
        self.range = GD["Enemy"][name]["Range"]
        self.power = GD["Enemy"][name]["Attack"]
        self.move = GD["Enemy"][name]["Move"]
        self.positionX = 0
        self.positionY = 0
