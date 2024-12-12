from Event import Event
from heapq import heappush
import logging
logger = logging.getLogger(__name__)

class EventQueue:

    # Constructor
    def __init__(self) -> None:
        logger.info('Initializing event queue')
        self.pq = []
        self.numEvents = 0
    
    # Getters
    def getQueue(self) -> list:
        return self.pq
    
    def getNumEvents(self) -> int:
        return self.numEvents
    
    # Other functions
    def enqueue(self, event : Event) -> None:
        #logger.info('Enqueueing onto event queue')
        heappush(self.pq, (event.getEventTime(), event))
        self.numEvents += 1
    
    def dequeue(self) -> Event:
        #logger.info('Dequeueing from event queue')
        try:
            event = self.pq.pop(0)[1]
            self.numEvents -= 1
            return event
        except IndexError:
            print("Queue is empty; you must enqueue an item first")
            return None