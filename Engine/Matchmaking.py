from Data.penguin import PenguinDB
Queue = []

def addToQueue(client):
    if matchFound(client.element):
        startGame(client)
        return
    queueStruct = [client.PID,client.element]
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
        print("A match was found")
        return True
    else:
        return False

def startGame(client):
    print("Game Starting")
    client.inQueue = False
    hasFire = True if client.element == 'fire' else False
    hasSnow = True if client.element == 'snow' else False
    hasWater = True if client.element == 'water' else False
    if not hasFire:
        fireId = Queue[getIndexByElement("fire")][0]
    else:
        fireId = client.PID
    if not hasSnow:
        snowId = Queue[getIndexByElement("snow")][0]
    else:
        snowId = client.PID
    if not hasWater:
        waterId = Queue[getIndexByElement("water")][0]
    else:
        waterId = client.PID
    client.sendLine("[W_PLACELIST]|0:10001|snow_1|3 player battle scenario|1|9|5|0|1|8|0|")
    client.sendLine('[UI_CLIENTEVENT]|'+str(client.PID)+'|receivedJson|{"action":"jsonPayload","jsonPayload":{"1":"'+str(getNameById(client, fireId))+'","2":"'+str(getNameById(client, waterId))+'","4":"'+str(getNameById(client, snowId))+'"},"targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","triggerName":"matchFound","type":"immediateAction"}')
    print("Game started with players Fire:{} Snow:{} Water:{}".format(fireId,snowId,waterId))
    #todo: send game started to all players
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
    del Queue[getQueueIndex(client.PID)]
    print(f"Removing {client.PID}")
