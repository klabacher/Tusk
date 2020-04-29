from Engine.Filter import Instance
from Engine.Penguin import Penguin

@Instance.register("/version")
def foo(client, arg):
    print(client)
    client.sendLine("[S_VERSION]|FY15-20150206 (4954)r|73971eecbd8923f695303b2cd04e5f70|Tue Feb  3 14:11:56 PST 2015|/var/lib/jenkins/jobs/BuildPlatform/workspace/metaserver_source/dimg")

@Instance.register("/login")
def foonix(client, arg):
    Penguin.PID = arg[1]
    Penguin.token = arg[2]
    print(client)
    client.sendLine("[S_LOGINDEBUG]|Got /login command from user")
    client.sendLine("[S_LOGINDEBUG]|Successfully verified credentials server-side")
    client.sendLine("[S_LOGINDEBUG]|Finalizing login, creating final user object")
    client.sendLine("[S_LOGIN]|"+str(Penguin.PID)+"|")
    client.sendLine("[S_WORLDTYPE]|0|1|0")
    client.sendLine("[S_WORLD]|13434341|clubpenguin_town_en_3|0:113140001|0|none|0|crowdcontrol|clubpenguin_town_en_3|0|200.5991|0")
    client.sendLine("[W_BASEASSETURL]| ")
    client.sendLine("[W_DISPLAYSTATE]|")
    client.sendLine("[M_REPORT]|11|Max Place Count|0|500")
    client.sendLine("[M_REPORT]|12|Max Place Size|0|500")
    client.sendLine("[M_REPORT]|16|Max Place Instances|0|100")
    client.sendLine("[M_REPORT]|0|Max Users|0|100")
    client.sendLine("[W_ASSETSCOMPLETE]|"+str(Penguin.PID)+"|")
