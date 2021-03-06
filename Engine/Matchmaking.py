from Data.penguin import PenguinDB
import logging
from Engine.GameEngine import GameEngine

Queue = []

logger = logging.getLogger("cjsnow")
def addToQueue(client):
    if matchFound(client.element):
        startGame(client)
        return
    queueStruct = [client.PID,client.element,client]
    Queue.append(queueStruct)
    print(f"Penguin {client.PID} on queue with {client.element}")
    client.inQueue = True

def matchFound(element):
    hasFire = True if element == 'fire' else False
    hasSnow = True if element == 'snow' else False
    hasWater = True if element == 'water' else False
    for x in Queue:
        if hasFire == False and x[1]=="fire":
            hasFire = True
        if hasSnow == False and x[1]=="snow":
            hasSnow = True
        if hasWater == False and x[1]=="water":
            hasWater = True
    if hasFire == True and hasSnow == True and hasWater == True:
        logger.info("A match was found")
        return True
    else:
        return False

def startGame(client):
    logger.info("Start Game called")
    client.inQueue = False
    hasFire = True if client.element == 'fire' else False
    hasSnow = True if client.element == 'snow' else False
    hasWater = True if client.element == 'water' else False
    if not hasFire:
        fireIndex = getIndexByElement("fire")
        fireId = Queue[fireIndex][0]
    else:
        fireId = client.PID
    if not hasSnow:
        snowIndex = getIndexByElement("snow")
        snowId = Queue[snowIndex][0]
    else:
        snowId = client.PID
    if not hasWater:
        waterIndex = getIndexByElement("water")
        waterId = Queue[waterIndex][0]
    else:
        waterId = client.PID
    if client.element == "fire":
        client.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
        client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
        fireclient = client
    else:
        fireclient = Queue[fireIndex][2]
        fireclient.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
        fireclient.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
    if client.element == "water":
        client.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
        client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
        waterclient = client
    else:
        waterclient = Queue[waterIndex][2]
        waterclient.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
        waterclient.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
    if client.element == "snow":
        client.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
        client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
        snowclient = client
    else:
        snowclient = Queue[snowIndex][2]
        snowclient.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
        snowclient.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
    removeFromQueue(snowclient)
    removeFromQueue(waterclient)
    removeFromQueue(fireclient)
    logger.info("Game started with players Fire:{} Snow:{} Water:{}".format(fireId,snowId,waterId))
    GameEngine(fireclient, waterclient, snowclient)
    return True

def getNameById(client, pid):
    player = client.session.query(PenguinDB).filter_by(id=pid).first()
    client.name = player.nickname
    return player.nickname

def getIndexByElement(element):
    for i in range(len(Queue)):
        if Queue[i][1] == element:
            return i
    return 0

def getQueueIndex(PID):
    for i in range(len(Queue)):
        if Queue[i][0] == PID:
            return i
    return 0

def removeFromQueue(client):
    try:
        del Queue[getQueueIndex(client.PID)]
        client.inQueue = False
        logger.warning(f"Removing {client.name}")
    except Exception as Error:
        logger.error(f"Not Removed {client.name} Because got exception: {Error}")
