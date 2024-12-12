class Packet:

    #constructor
    def __init__(self, packetID, packetSize, arrivalTime, dequeueTime) -> None:
        self.packetID = packetID
        self.packetSize = packetSize
        self.arrivalTime = arrivalTime
        self.dequeueTime = dequeueTime

    #getters
    def getPacketID(self):
        return self.packetID
    
    def getPacketSize(self):
        return self.packetSize
    
    def getArrivalTime(self):
        return self.arrivalTime
    
    def getDequeueTime(self):
        return self.dequeueTime
    
    #setters
    def setPacketID(self, packetID):
        self.packetID = packetID
    
    def setPacketSize(self, packetSize):
        self.packetSize = packetSize
    
    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime
    
    def setDequeueTime(self, dequeueTime):
        self.dequeueTime = dequeueTime