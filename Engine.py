from Packet import Packet
import logging
logger = logging.getLogger(__name__)

class Engine:

    #constructor
    def __init__(self, currentPacket : Packet, serviceTime, busyStatus : bool) -> None:
        logger.info('Initializing engine')
        self.currentPacket = currentPacket
        self.serviceTime = serviceTime
        self.busyStatus = busyStatus

    #getters
    def getCurrentPacket(self) -> Packet:
        return self.currentPacket
    
    def getServiceTime(self):
        return self.serviceTime
    
    def getBusyStatus(self) -> bool:
        return self.busyStatus
    
    #setters
    def setCurrentPacket(self, currentPacket) -> None:
        self.currentPacket = currentPacket
    
    def setServiceTime(self, serviceTime) -> None:
        self.serviceTime = serviceTime
    
    def setBusyStatus(self, busyStatus) -> None:
        self.busyStatus = busyStatus