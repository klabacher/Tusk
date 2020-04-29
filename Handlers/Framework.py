from Engine.Filter import Instance
from Engine.Penguin import Penguin

queue = []

@Instance.register("/intro_anim_done")
def versionhandler(client, arg):
    print(client)
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"immediateAction","action":"setWorldId","worldId":1510202}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"immediateAction","action":"setBaseAssetUrl","baseAssetUrl":"http://media.localhost/game/mpassets/"}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"immediateAction","action":"setFontPath","defaultFontPath":"http://media.localhost/game/mpassets//fonts/"}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"playAction","action":"skinRoomToRoom","url":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/../assets/cjsnow_loadingscreenassets.swf", "className":"", "variant":0 }')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"loadWindow","assetPath":"","initializationPayload":[null],"layerName":"bottomLayer","loadDescription":"","type":"playAction","windowUrl":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowerrorhandler.swf","xPercent":0,"yPercent":0}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"loadWindow","assetPath":"","initializationPayload":{"game":"snow","name":"'+str(Penguin.getUsername())+'","powerCardsFire":'+str(Penguin.getPowerCards("fire"))+',"powerCardsSnow":'+str(Penguin.getPowerCards("snow"))+',"powerCardsWater":'+str(Penguin.getPowerCards("water"))+'},"layerName":"topLayer","loadDescription":"","type":"playAction","windowUrl":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","xPercent":0,"yPercent":0}')

@Instance.register("#receivedFromFramework")
def readyhandler(client, arg):
    print(client)
    parsedJson = json.loads(arg)
    if parsedJson['triggerName']=="mmElementSelected":
        Penguin.element = parsedJson['element']
        Penguin.tipsEnabled = parsedJson['tipMode']
        addToQueue(Penguin.PID,Penguin.element)

def addToQueue(PID,element):
    if matchFound(element):
        startGame(PID)
    queueStruct = [PID,element]
    queue.append(queueStruct)
    Penguin.inQueue = True

def matchFound(element):
    hasFire = True if element == 'fire' else False
    hasSnow = True if element == 'snow' else False
    hasWater = True if element == 'water' else False
    for x in queue:
        if hasFire == False and x[1]=="fire":
            hasFire = True
        if hasSnow == False and x[1]=="snow":
            hasSnow = True
        if hasWater == False and x[1]=="water":
            hasWater = True
    if hasFire == True and hasSnow == True and hasWater == True:
        return True
    else:
        return False

def startGame(PID):
    Penguin.inQueue = False
    hasFire = True if element == 'fire' else False
    hasSnow = True if element == 'snow' else False
    hasWater = True if element == 'water' else False
    if not hasFire:
        fireId = getIndexByElement("fire")
    else:
        fireId = PID
    if not hasSnow:
        snowId = getIndexByElement("snow")
    else:
        fireId = PID
    if not hasWater:
        waterId = getIndexByElement("water")
    else:
        waterId = PID
    client.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById("fire"))+'","2":"'+str(getNameById("water"))+'","4":"'+str(getNameById("snow"))+'1"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
    #todo: send game started to all players
    return True

def getNameById(PID):
    #todo: get player name from db
    return "Jjguve5"

def getIndexByElement(element):
    for i in range(len(queue)):
        if queue[i][1] == element:
            return i
    return 0

def getQueueIndex(PID):
    for i in range(len(queue)):
        if queue[i][0] == PID:
            return i
    return 0

def removeFromQueue(PID):
    del queue[getQueueIndex(PID)]
