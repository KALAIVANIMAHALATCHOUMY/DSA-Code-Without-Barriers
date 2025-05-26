# Network Packet Routing Simulation

This Python simulation models how data packets are created, prioritized, and routed through a simplified network. The program demonstrates core data structure concepts such as **Stacks**, **Queues**, and **Linked Lists** to simulate a network device handling incoming data packets.

---

## Features

- **DataPacket** objects simulate packets with:
  - Source and destination nodes
  - Priority level (High, Medium, Low)
  - A stack-based header containing route metadata
  - A linked list journey path through the network

- **Queue** (`deque`) used for managing incoming packets, simulating congestion when the queue exceeds capacity.

- **Stack** used in packet headers to simulate LIFO operations for routing metadata.

- **Linked List** represents the routing journey of each packet.

---

## Concepts Demonstrated

- **Stack** for packet header management (`push`, `pop`, `peek`)
- **Queue** for incoming packet management with a congestion control mechanism
- **Linked List** to represent the path a packet takes through the network
- **Object-Oriented Programming** (OOP) principles

---

## How It Works

1. A set of network nodes (e.g., A, B, C, D) is predefined.
2. Random packets are generated with:
   - A unique ID
   - Random source and destination
   - Random priority
3. The journey/path is built excluding the source and destination from the middle steps.
4. If the packet queue exceeds `MAX_QUEUE_SIZE` (5), the last one is dropped to simulate congestion.
5. Each packet is routed:
   - Header metadata is added via a `Stack`
   - The journey is printed via traversal of a `Linked List`

---

## Requirements

- Python 3.x
- No external libraries are required (only uses standard library modules: `random`, `collections`)

---


