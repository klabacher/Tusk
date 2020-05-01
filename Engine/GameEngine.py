from Utils.GameData import GameData as GD
import time

class GameEngine(object):
    def __init__(self, fireclient, waterclient, snowclient):
        self.fclient = fireclient #object id 64
        self.wclient = waterclient #object id 65
        self.sclient = snowclient #object id 66
        self.round = 1
        self.map = None
        loadGame()

    def loadGame():
        self.map = randrange(1, 3)
        self.loadAllSpritesAndMap(self.map)
        self.spawnPenguins()
        while not self.hasWonGame() and not self.hasLost():
            self.doNextRound()
        self.goToPayout()
        return

    def doNextRound():
        self.playRoundTitle(self.round-1)
        time.sleep(3)
        #wait for received animation done
        for x in GD["Enemy"]:
            if x["Round"+self.round]["x"] is not -1:
                createAndSpawnEnemy(x)
        while not self.hasWonRound() and not self.hasLost():
            self.showGrid()
            if not self.fclient.hasDisconnected:
                self.getMoves(self.fclient)
            if not self.wclient.hasDisconnected:
                self.getMoves(self.wclient)
            if not self.sclient.hasDisconnected:
                self.getMoves(self.sclient)
            self.startTimer()
            self.hideTimer()
            self.hideGrid()
            if not self.fclient.hasDisconnected and not self.fclient.usedPowerCard and not self.fclient.hp<=0:
                self.moveAndAttack(self.fclient)
            if not self.wclient.hasDisconnected and not self.wclient.usedPowerCard and not self.wclient.hp<=0:
                self.moveAndAttack(self.wclient)
            if not self.sclient.hasDisconnected and not self.sclient.usedPowerCard and not self.sclient.hp<=0:
                self.moveAndAttack(self.sclient)
            if self.checkForCombo:
                playCombo()
            if self.fclient.usedPowerCard:
                self.playPowerCard(fclient)
            if self.wclient.usedPowerCard:
                self.playPowerCard(wclient)
            if self.sclient.usedPowerCard:
                self.playPowerCard(sclient)
            for x in GD["Enemy"]:
                if x["Round"+self.round][x] is not -1:
                    #todo: check if hp <=0
                    self.moveAndAttackEnemy(x)
        if self.hasWonRound()
            self.round+=1

    def loadAllSpritesAndMap():
        return

    def spawnPenguins():
        return

    def hasWonGame():
        return

    def hasLost():
        return

    def goToPayout():
        return

    def playRoundTitle():
        return

    def hasWonRound():
        return

    def showGrid():
        return

    def getMoves(client):
        return

    def startTimer():
        return

    def hideTimer():
        return

    def hideGrid():
        return

    def moveAndAttack(client):
        return

    def playCombo():
        return

    def playPowerCard(client):
        return

    def moveAndAttackEnemy(enemy):
        return
        
    def createAndSpawnEnemy(enemy):
        return



class Enemy(object):
    def __init__(self, name):
        self.name = name
        self.id = id["Enemy"][name]["id"]
        self.hp = GD["Enemy"][name]["HP"]
        self.range = GD["Enemy"][name]["Range"]
        self.power = GD["Enemy"][name]["Attack"]
        self.move = GD["Enemy"][name]["Move"]
        self.positionX = 0
        self.positionY = 0
