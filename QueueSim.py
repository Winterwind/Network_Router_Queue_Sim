import random, os, logging, time
from Engine import Engine
from Packet import Packet
from PacketQueue import PacketQueue
from Event import Event
from EventQueue import EventQueue
logger = logging.getLogger(__name__)

def run_simulation(num_packets, arrival_rate, service_rate) -> dict[str]:
    logging.basicConfig(filename='QueueSim.log', level=logging.INFO)
    logger.info('STARTING SIM')

    r1 = random.Random()
    r1.seed(os.urandom(4))
    r2 = random.Random()
    r2.seed(os.urandom(4))

    event_queue = EventQueue()
    packet_queue = PacketQueue(0)  # Unlimited size
    engine = Engine(None, 0, False)

    total_wait_time = 0
    total_busy_time = 0
    max_queue_size = 0
    longest_wait_time = 0
    total_bytes = 0

    current_time = 0
    next_arrival = r1.expovariate(arrival_rate)
    event_queue.enqueue(Event(next_arrival, "arrival"))

    processed_packets = 0
    while processed_packets < num_packets:
        event = event_queue.dequeue()
        current_time = event.getEventTime()

        if event_queue.getNumEvents() == 0:
            next_arrival = current_time + r1.expovariate(arrival_rate)
            event_queue.enqueue(Event(next_arrival, "arrival"))

        if event.getEventType() == "arrival":
            packet_size = max(40, min(1460, int(r2.gauss(750, 200))))
            packet = Packet(processed_packets, packet_size, current_time, None)
            logger.info(f'New packet has arrived!')
            #print(f'New packet has arrived!')
            packet_queue.enqueue(packet)
            logger.info(f'Currently {packet_queue.getNumItems()} packets in queue')
            #print(f'Currently {packet_queue.getNumItems()} packets in queue')
            max_queue_size = max(max_queue_size, packet_queue.getNumItems())

            next_arrival = current_time + r1.expovariate(arrival_rate)
            event_queue.enqueue(Event(next_arrival, "arrival"))

            if not engine.getBusyStatus():
                next_packet = packet_queue.dequeue()
                service_time = (next_packet.getPacketSize() * 8) / service_rate
                next_packet.setDequeueTime(current_time + service_time)
                engine.setCurrentPacket(next_packet)
                engine.setServiceTime(service_time)
                engine.setBusyStatus(True)
                event_queue.enqueue(Event(current_time + service_time, "departure"))

        elif event.getEventType() == "departure":
            processed_packet = engine.getCurrentPacket()
            wait_time = processed_packet.dequeueTime - processed_packet.arrivalTime
            longest_wait_time = max(longest_wait_time, wait_time)
            total_wait_time += wait_time
            total_busy_time += engine.getServiceTime()
            total_bytes += processed_packet.getPacketSize()
            processed_packets += 1

            if packet_queue.getNumItems() > 0:
                next_packet = packet_queue.dequeue()
                service_time = (next_packet.getPacketSize() * 8) / service_rate
                next_packet.setDequeueTime(current_time + service_time)
                engine.setCurrentPacket(next_packet)
                engine.setServiceTime(service_time)
                event_queue.enqueue(Event(current_time + service_time, "departure"))
            else:
                engine.setBusyStatus(False)
            
            logger.info(f'Packet {processed_packets} is finished')
            #print(f'Packet {processed_packets} is finished')

    total_time = total_wait_time + total_busy_time
    avg_wait_time = total_wait_time / num_packets
    utilization = (total_busy_time / current_time) * 100

    logger.info('FINISHING SIM')

    return {
        "Total time [μs]": total_time,
        "Total number of packets served": packet_queue.getItemHist(),
        "Total Bytes Processed": total_bytes,
        "Most packets held by queue": max_queue_size,
        "Longest wait time for any packet (μs)": longest_wait_time,
        "Average Wait Time (μs)": avg_wait_time,
        "Total time the engine was busy (μs)": total_busy_time,
        "Router Utilization (%)": utilization
    }

if __name__ == '__main__':
    logger.info('STARTING PROGRAM')
    test_cases = [
    {"description": "Arrival rate much lower than service rate", "arrival_rate": 0.001, "service_rate": 100},
    {"description": "Arrival rate much greater than service rate", "arrival_rate": 0.1, "service_rate": 100},
    {"description": "Arrival rate close to service rate", "arrival_rate": 0.01, "service_rate": 100},
    ]
    which_case = int(input(f"Which test case would you like to run?\n(type 0 for {test_cases[0]['description']},\n1 for {test_cases[1]['description']},\nor 2 for {test_cases[2]['description']})\n"))
    results = run_simulation(num_packets=1000, arrival_rate=(test_cases[which_case]).get("arrival_rate"), service_rate=(test_cases[which_case]).get("service_rate"))
    for n in range(len(results)):
        logger.info(f'{list(results)[n]}: {results.get(list(results)[n])}')
    logger.info('FINISHING PROGRAM\n')