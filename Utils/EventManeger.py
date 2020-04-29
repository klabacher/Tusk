#from Engine.Penguin import Penguin

class EventHandler():
    def __init__(self):
        self.handlers = {}
    
    def printt(self):
        print(self.handlers)

    def call(self, client, type, arg):
        print("call called" + type)
        if type in self.handlers:
            for h in self.handlers[type]:
                retur = h(client, arg)
        

    def register(self, type):
        def registerhandler(handler):
            if type in self.handlers:
                self.handlers[type].append(handler)
                print("Registered for EH: " + str(type))
            else:
                self.handlers[type] = [handler]
                print("Registered for EH: " + str(type))

            return handler
        return registerhandler

Instance = EventHandler()