import logging

class EventHandler():
    def __init__(self):
        self.logger = logging.getLogger("cjsnow")
        self.handlers = {}
        self.clients = []
    
    def printt(self):
        print(self.handlers)

    def call(self, client, type, arg):
        self.logger.info(f"Called {type} with {arg}")
        if type in self.handlers:
            for h in self.handlers[type]:
                h(client, arg)
        

    def register(self, type):
        def registerhandler(handler):
            if type in self.handlers:
                self.handlers[type].append(handler)
                self.logger.info("Append for EH: " + str(type))
            else:
                self.handlers[type] = [handler]
                self.logger.info("Registered for EH: " + str(type))

            return handler
        return registerhandler


Instance = EventHandler()