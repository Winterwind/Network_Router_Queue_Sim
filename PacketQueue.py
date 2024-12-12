from Packet import Packet
import logging
logger = logging.getLogger(__name__)

class PacketQueue:

    # Constructor
    def __init__(self, maxItems : int) -> None:
        logger.info('Initializing packet queue')
        self.queue = []
        self.numItems = 0
        self.itemHist = 0
        if maxItems < 0:
            raise ValueError("Max items cannot be negative")
        else:
            self.maxItems = maxItems

    # Getters
    def getQueue(self) -> list:
        return self.queue
    
    def getNumItems(self) -> int:
        return self.numItems
    
    def getItemHist(self) -> int:
        return self.itemHist
    
    def getMaxItems(self) -> int:
        if self.maxItems != 0:
            return self.maxItems
        else:
            print("There is no maximum")
            return None
    
    # Other functions
    def enqueue(self, packet : Packet) -> None:
        #logger.info('Enqueueing onto packet queue')
        if (self.numItems < self.maxItems and self.maxItems > 0) or (self.maxItems == 0):
            self.queue.append(packet)
            self.numItems += 1
            self.itemHist += 1
        else:
            print("Queue is full; you must dequeue an item first")

    def dequeue(self) -> Packet:
        #logger.info('Dequeueing packet queue')
        if self.numItems > 0:
            try:
                packet = self.queue.pop(0)
                self.numItems -= 1
                return packet
            except IndexError:
                print("Queue is empty; you must enqueue an item first")
                return None
        else:
            print("Queue is empty; you must enqueue an item first")
            return None