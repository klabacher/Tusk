from Engine.Filter import Instance
from Engine.Penguin import Penguin
@Instance.register("/version")
def foo(client, arg):
    print(client)
    client.sendLine("[S_VERSION]|FY15-20150206 (4954)r|73971eecbd8923f695303b2cd04e5f70|Tue Feb  3 14:11:56 PST 2015|/var/lib/jenkins/jobs/BuildPlatform/workspace/metaserver_source/dimg")
