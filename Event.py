class Event:

    # Constructor
    def __init__(self, eventTime, eventType):
        self.eventTime = eventTime
        self.eventType = eventType
    
    # Getters
    def getEventTime(self):
        return self.eventTime
    
    def getEventType(self):
        return self.eventType
    
    # Setters
    def setEventTime(self, eventTime):
        self.eventTime = eventTime
    
    def setEventType(self, eventType):
        self.eventType = eventType