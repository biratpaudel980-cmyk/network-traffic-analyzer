# network-traffic-analyzer
A lightweight Python network packet sniffer built using the Scapy library to analyze live TCP/IP traffic.

# Network Traffic Analyzer & Packet Parser

A lightweight, Python-based network packet sniffer built using the Scapy library. This tool monitors live network interfaces, decapsulates packet headers, and extracts layer-3 (IP) and layer-4 (TCP/UDP) routing metadata in real-time.

## Features
* **Live Sniffing:** Intercepts real-time raw packets directly from the network interface.
* **Protocol Decapsulation:** Extracts source/destination IP addresses, protocol types, and port numbers.
* **Clean Formatting:** Logs packet trajectories with precise human-readable timestamps.

## Technical Details & Architecture

The script operates by hooking into the network interface driver via administrative privileges (`sudo`). It listens to the raw data stream and peels back the network layers:



1. **Network Layer (IP):** Extracts the source and destination addresses.
2. **Transport Layer (TCP/UDP):** Parses the specific source and destination application ports (e.g., tracking HTTPS traffic on port 443 or mDNS on port 5353).

## How To Run It

### Prerequisites
Ensure your system has Python 3 and Scapy installed globally:
```bash
sudo apt update
sudo apt install python3-pip
sudo pip3 install scapy --break-system-packages
