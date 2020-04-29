from twisted.protocols.basic import LineOnlyReceiver
import logging

from Utils.EventManeger import Instance

class Spheniscidae(LineOnlyReceiver, object):

    delimiter = b"\x00" or b"\r\n"

    def __init__(self, session, server):
        self.logger = logging.getLogger("Cjsnow")

        self.session = session
        self.server = server

        # Defined once the client requests it (see handleRandomKey)
        self.randomKey = None

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
            else:
                command = packet_split[0]
                args = packet_split[1:]
                Instance.call(self, command, "args")
        elif Adata.startswith("#receivedFromFramework") == True:
            parsed = Adata.split("#receivedFromFramework")
            for x in parsed:
                Instance.call(self, "Framework", x)
        else:
            print("else")

    def sendPolicyFile(self):
        super(Spheniscidae, self).sendLine("<cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>".encode("Utf-8"))
        self.logger.debug("Outgoing Police")

    def sendLine(self, line):
        tag = line+"\r\n"
        print("Outgoing Tag: {0}".format(line))
        self.transport.write(tag.encode("utf-8"))
