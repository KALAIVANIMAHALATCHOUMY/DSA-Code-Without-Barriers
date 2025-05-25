import random
from collections import deque

#Node array
nodes = ["Node A", "Node B", "Node C", "Node D"]

#Journey as a linked list node or data transfer path:
class JourneyNode:
    def __init__(self, name):
        self.name = name
        self.next = None

#Packet class
class DataPacket:
    def __init__(self, id, source, destination, priority):
        self.id = id
        self.source = source
        self.destination = destination
        self.priority = priority
        self.header = Stack()
        self.path = self.create_journey(source, destination)

    def create_journey(self, src, dst):
        journey = JourneyNode(src)
        current = journey
        for node in nodes:
            if node != src and node != dst:
                step = JourneyNode(node)
                current.next = step
                current = step
        current.next = JourneyNode(dst)
        return journey

#Stack for priority or header infomations content in the packet:
class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop() if self.container else None

    def peek(self):
        return self.container[-1] if self.container else None

    def is_empty(self):
        return len(self.container) == 0

# Queue for incoming packets
incoming_queue = deque()
MAX_QUEUE_SIZE = 5  
# congestion threshold

def route_packet(packet):
    print(f"\n Routing Packet {packet.id} (Priority: {packet.priority})")
    #packet header
    packet.header.push(f"RouteInfo-{packet.source}->{packet.destination}")
    print(" Header Info:", packet.header.peek())
    # Traverse the linked list(journey path)
    print(" Journey Path:")
    node = packet.path
    while node:
        print(f"{node.name}")
        node = node.next

def network_device_simulation():
    packet_id = 1
    while True:
        src, dst = random.sample(nodes, 2)
        prio = random.choice(["High", "Medium", "Low"])
        packet = DataPacket(packet_id, src, dst, prio)

        if len(incoming_queue) >= MAX_QUEUE_SIZE:
            print("\n Congestion Detected! Dropping lowest priority packet")
            incoming_queue.pop()

        incoming_queue.appendleft(packet)
        print(f"\n Packet {packet_id} arrived from {src} to {dst} (Priority: {prio})")
        packet_id += 1

        if incoming_queue:#old packet processing
            next_packet = incoming_queue.pop()
            route_packet(next_packet)

        input("Press Enter to simulate next packet")

if __name__ == "__main__":
    network_device_simulation()
