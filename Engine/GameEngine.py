from Utils.GameData import GameData as GD
class GameEngine(object):
    def __init__(self, fireclient, waterclient, snowclient):
        self.fclient = fireclient
        self.wclient = waterclient
        self.sclient = snowclient
        self.mSpeed = 100
        self.map = None
        print(self.sclient)
        print(self.wclient)
        print(self.fclient)
        # sly, tank, scrap
    
    def AStag(self, line):
        clients = [self.fclient, self.wclient, self.sclient]
        for c in clients:
            c.sendLine(line)


class Enemy(GameEngine, object):
    def __init__(self, name, id, round):
        self.name = name
        self.id = id
        self.idDesign = GD[name]["IDDesign"]
        self.hp = GD[name]["HP"]
        self.range = GD[name]["Range"]
        self.power = GD[name]["Attack"]
        self.canMove = GD[name]["Move"]
        self.AniAttack = GD[name]["AniAttack"]
        self.AniMove = GD[name]["AniMove"]
        self.mSpeed = 100
        self.round = round
        self.AStag(f"[O_HERE]|{self.id}|0:{self.idDesign}|x|y|128|1|0|0|0||0:1|0|1|0")

    def move(self, x, y):
        tag = f"[O_SLIDE]|{self.id}|{x}|{y}|128|{self.mSpeed}"
        movetag = f"[O_ANIM]|{self.id}|0:{self.AniMove}|loop|700|1|0|13|2|0|0"
        self.AStag(tag)
        self.AStag(movetag)

