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
        client.sendLine('[UI_CLIENTEVENT]|101|receivedJson|{"type":"playAction","action":"closeWindow","targetWindow":"http://media.localhost/game/mpassets/minigames/cjsnow/en_US/deploy/swf/ui/windows/cardjitsu_snowplayerselect.swf"}')
        client.sendLine("[O_GONE]|4")
        client.sendLine("[W_PLACE]|1:10001|8|1")
        client.sendLine("[W_INPUT]|use|0:10|2|3|0|use|")
        client.sendLine("[W_INPUT]|touch-the-terrain|0:8600033|1|6|0|path_terrain|")
        client.sendLine("[W_INPUT]|mouse-the-terrain|0:8600033|1|3|0|path_terrain|")
        client.sendLine("[P_MAPBLOCK]|t|1|1|iVBORw0KGgoAAAANSUhEUgAAAAkAAAAFCAAAAACyOJm3AAAAHUlEQVQImWNgZeRkZARidgZGCGBnZ2CFMVHEoOoADJEAhIsKxDUAAAAASUVORK5CYII=")
        client.sendLine("[P_MAPBLOCK]|h|1|1|iVBORw0KGgoAAAANSUhEUgAAAAoAAAAGCAAAAADfm1AaAAAADklEQVQImWNogAMG8pgA3m8eAacnkzQAAAAASUVORK5CYII=")
        client.sendLine("[P_ZOOMLIMIT]|-1.000000|-1.000000")
        client.sendLine("[P_RENDERFLAGS]|0|48")
        client.sendLine("[P_SIZE]|9|5")
        client.sendLine("[P_VIEW]|5")
        client.sendLine("[P_START]|4.5|2.5|0")
        client.sendLine("[P_LOCKVIEW]|0")
        client.sendLine("[P_TILESIZE]|100")
        client.sendLine("[P_ELEVSCALE]|0.031250")
        client.sendLine("[P_RELIEF]|1")
        client.sendLine("[P_LOCKSCROLL]|1|0|0|573321786")
        client.sendLine("[P_HEIGHTMAPSCALE]|0.078125|128")
        client.sendLine("[P_HEIGHTMAPDIVISIONS]|1")
        client.sendLine("[P_CAMERA3D]|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|864397819904.000000|0.000000|0|0")
        client.sendLine("[UI_BGCOLOR]|0|0|0")
        client.sendLine("[P_DRAG]|0")
        client.sendLine("[P_CAMLIMITS]|0|0|0|0")
        client.sendLine("[P_LOCKRENDERSIZE]|0|1024|768")
        client.sendLine("[P_LOCKOBJECTS]|0")
        client.sendLine("[UI_BGSPRITE]|0:-1|0|1.000000|1.000000")
        client.sendLine("[P_TILE]|0||0|0|1|0:2|Empty Tile|0|0|0|0:7940012")
        client.sendLine("[P_TILE]|1||0|0|1|0:2|open|0|0|0|0:7940013")
        client.sendLine("[P_TILE]|2||0|0|1|0:3|enemy|0|0|0|0:7940014")
        client.sendLine("[P_TILE]|3||0|0|1|0:4|penguin|0|0|0|0:7940015")
        client.sendLine("[P_TILE]|4||0|0|1|0:100002|penguin_spawn_occupied|0|0|0|0:7940016")
        client.sendLine("[P_TILE]|5||0|0|1|0:6|penguin_spawn_unoccupied|0|0|0|0:7940017")
        client.sendLine("[P_TILE]|7||0|0|1|0:10003|enemy_spawn_unoccupied|0|0|0|0:7940018")
        client.sendLine("[P_TILE]|8||0|0|1|0:10004|enemy_spawn_occupied|0|0|0|0:7940019")
        client.sendLine("[P_TILE]|9||0|0|1|0:10005|obstacle|0|0|0|0:7940020")
        client.sendLine("[P_PHYSICS]|0|0|0|0|0|0|0|1")
        client.sendLine("[P_ASSETSCOMPLETE]|0|0")
