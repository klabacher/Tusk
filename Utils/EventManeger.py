import logging

class EventHandler():
    def __init__(self):
        self.logger = logging.getLogger("cjsnow")
        self.handlers = {}
    
    def printt(self):
        print(self.handlers)

    def call(self, client, type, arg):
        self.logger.info(f"Called {type} with {arg}")
        if type in self.handlers:
            for h in self.handlers[type]:
                h(client, arg)

    def delete(self, type):
        self.logger.info(f"Try to delete {type}")
        if type in self.handlers:
            try:
                del self.handlers[type]
            except Exception:
                self.logger.error(f"Cant delete {type} because {Exception}")
        

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