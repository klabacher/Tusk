
class GameEngine(object):
    def __init__(self, fireclient, waterclient, snowclient):
        self.fclient = fireclient
        self.wclient = waterclient
        self.sclient = snowclient
        self.map = None
        print(self.sclient)
        print(self.wclient)
        print(self.fclient)
    
    def AStag(self, line):
        clients = [fireclient, waterclient, snowclient]
        for c in clients:
            c.sendLine(line)


class Enemy(object, GameEngine):
    def __init__(self, name, hp, Erange, power):
        self.name = name
        self.hp = hp
        self.range = Erange
        self.power = power

    def move(self, x, y):
        tag = f""
        self.AStag()

