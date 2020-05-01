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
        self.map = randrange(1, 3)
        loadAllSpritesAndMap(self.map)
        spawnPenguins()
        while not self.hasWonGame() and not self.hasLost():
            self.doNextRound()
        self.goToPayout()
        return

    def doNextRound():
        self.playRoundTitle(self.round-1)
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
