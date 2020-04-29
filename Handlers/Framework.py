from Engine.Filter import Instance
from Engine.Penguin import Penguin
from Engine.Matchmaking import addToQueue
import json

queue = []

@Instance.register("/intro_anim_done")
def versionhandler(client, arg):
    print(client)
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"immediateAction","action":"setWorldId","worldId":1510202}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"immediateAction","action":"setBaseAssetUrl","baseAssetUrl":"http://media.localhost/game/mpassets/"}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"immediateAction","action":"setFontPath","defaultFontPath":"http://media.localhost/game/mpassets//fonts/"}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"playAction","action":"skinRoomToRoom","url":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/../assets/cjsnow_loadingscreenassets.swf", "className":"", "variant":0 }')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"loadWindow","assetPath":"","initializationPayload":[null],"layerName":"bottomLayer","loadDescription":"","type":"playAction","windowUrl":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowerrorhandler.swf","xPercent":0,"yPercent":0}')
    client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"action":"loadWindow","assetPath":"","initializationPayload":{"game":"snow","name":"'+str(client.name)+'","powerCardsFire":'+str(client.getPowerCards("fire"))+',"powerCardsSnow":'+str(client.getPowerCards("snow"))+',"powerCardsWater":'+str(client.getPowerCards("water"))+'},"layerName":"topLayer","loadDescription":"","type":"playAction","windowUrl":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf","xPercent":0,"yPercent":0}')

@Instance.register("Framework")
def readyhandler(client, arg):
    parsedJson = json.loads(arg)
    if parsedJson['triggerName']=="mmElementSelected":
        client.element = parsedJson['element']
        client.tipsEnabled = parsedJson['tipMode']
        addToQueue(client)
    if 'action' in parsedJson:
        print("test")
