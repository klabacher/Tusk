
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
