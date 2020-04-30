from twisted.protocols.basic import LineOnlyReceiver
import logging

from Utils.EventManeger import Instance

class Spheniscidae(LineOnlyReceiver, object):

    delimiter = b"\x00" or b"\r\n"

    def __init__(self, session, server):
        self.logger = logging.getLogger("cjsnow")

        self.session = session
        self.server = server



    def dataReceived(self, line):
        Adata = line.decode("utf-8")
        self.logger.info("Data: " + Adata)
        if Adata.startswith("<"):
            self.sendPolicyFile()
        elif Adata.startswith("/") == True:
            packet_split = Adata.split()
            if Adata.startswith("/place_context") == True:
                splited = Adata.split("\r\n")
                place = splited[0].split()
                place_com = place[0]
                place_arg = place[1:]
                login = splited[1].split()
                login_com = login[0]
                login_arg = login[1:]
                Instance.call(self, place_com, place_arg)
                Instance.call(self, login_com, login_arg)
            elif Adata.startswith("/intro_anim_done"):
                ps = Adata.split()
                try:
                    if ps[1] == "#receivedFromFramework":
                        Instance.call(self, "Framework", ps[2])
                    if ps[3] == "#receivedFromFramework":
                        Instance.call(self, "Framework", ps[4])
                    if ps[5] == "#receivedFromFramework":
                        Instance.call(self, "Framework", ps[6])
                except:
                        print("Framework was not sent with intro_anim_done")
            elif Adata.startswith("/anim_done") ==  True:
                ps = Adata.split()
                try:
                    if ps[3] == "/anim_done":
                        arg = []
                        arg.append(ps[4])
                        arg.append(ps[5])
                        Instance.call(self, "/anim_done", arg)
                    if ps[6] == "/anim_done":
                        arg = []
                        arg.append(ps[7])
                        arg.append(ps[8])
                        Instance.call(self, "/anim_done", arg)
                except:
                    Instance.call(self, "/anim_done", ps)
            else:
                command = packet_split[0]
                args = packet_split[1:]
                Instance.call(self, command, args)
        elif Adata.startswith("#receivedFromFramework") == True:
            parsed = Adata.split("#receivedFromFramework")
            self.logger.info(f"#receivedFromFramework call, passing {parsed[1]}")
            Instance.call(self, "Framework", parsed[1])
        else:
            self.logger.error(f"Nothing filtered from {str(Adata)}")

    def sendPolicyFile(self):
        super(Spheniscidae, self).sendLine("<cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>".encode("Utf-8"))
        self.logger.info("Outgoing Police")

    def sendLine(self, line):
        tag = line+"\r\n"
        self.logger.info("Outgoing Tag: {0}".format(line))
        self.transport.write(tag.encode("utf-8"))
