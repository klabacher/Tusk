import json

json.load(Utils.GameData)
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
        clients = [self.fireclient, self.waterclient, self.snowclient]
        for c in clients:
            c.sendLine(line)


class Enemy(GameEngine, object):
    def __init__(self, name, id, hp, Erange, power, round):
        self.name = name
        self.id = id
        self.hp = hp
        self.range = Erange
        self.power = power
        self.mSpeed = 100
        self.round = round
        if name == "sky":
            self.design = 1
            if self.round == 1:
                self.z = 1
                self.x = 2
            elif self.round == 2:
                self.z = 1
                self.x = 2
            elif self.round == 3:
                self.z = 1
                self.x = 2
            else:
                self.z = 1
                self.x = 2
                print("Not supported most than 3 rounds")
        elif name == "tank":
            self.design = 2
            if self.round == 1:
                self.z = 1
                self.x = 2
            elif self.round == 2:
                self.z = 1
                self.x = 2
            elif self.round == 3:
                self.z = 1
                self.x = 2
            else:
                self.z = 1
                self.x = 2
                print("Not supported most than 3 rounds")
        elif name == "scrap":
            self.design = 3
            if self.round == 1:
                self.z = 1
                self.x = 2
            elif self.round == 2:
                self.z = 1
                self.x = 2
            elif self.round == 3:
                self.z = 1
                self.x = 2
            else:
                self.z = 1
                self.x = 2
                print("Not supported most than 3 rounds")
      
        self.AStag(f"[O_HERE]|{self.id}|0:{self.id}|x|y|128|1|0|0|0||0:1|0|1|0")

    def move(self, x, y):
        tag = f"[O_SLIDE]|id do gameobject|{x}|{y}|128|{self.mSpeed}"
        self.AStag(tag)

