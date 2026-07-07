Packet Sniffer
A Python-based Packet Sniffer that captures and analyzes live network traffic using Scapy. The project supports protocol filtering, hostname resolution, packet logging, and PCAP export for analysis in Wireshark.

Features
- Capture live network packets
- Filter packets by:
  - TCP
  - UDP
  - ICMP
  - All Packets
- Display:
  - Source IP Address
  - Destination IP Address
  - Source Port
  - Destination Port
  - Protocol
  - Packet Length
  - Timestamp
  - Hostname (using Python socket library)
- Save packet details to a log file
- Export captured packets to `.pcap`
- Validate captured traffic using Wireshark

Technologies Used
- Python
- Scapy
- Socket Library
- Wireshark

Project Structure
Packet Sniffer/
│── main.py
│── sniffer.py
│── filters.py
│── logger.py
│── utils.py
│── packet_logs.txt
│── captured_packets.pcap
│── requirements.txt
│── README.md
```

Installation
1. Clone the repository
```bash
git clone <repository-link>
```
2. Navigate to the project folder
```bash
cd Packet-Sniffer
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Install Npcap (Windows)
Download and install Npcap before running the project.

Usage
Run the program:
```bash
python main.py
```
Choose one of the available options:
```
1. Capture All Packets
2. Capture TCP Packets
3. Capture UDP Packets
4. Capture ICMP Packets
```
Press **Ctrl + C** to stop packet capture.
The program automatically:
- Displays packet information
- Saves logs to `packet_logs.txt`
- Exports captured packets to `captured_packets.pcap`

 Sample Output
```
Packet #15
Time             : 21:45:16
Source IP        : 142.250.xxx.xxx
Destination IP   : 192.168.0.xxx
Protocol         : TCP
Source Port      : 443
Destination Port : 52618
Packet Length    : 66 bytes
```
Future Improvements
- DNS packet analysis
- HTTP/HTTPS packet detection
- MAC Address information
- CSV Export
- GUI using Tkinter
- Packet search functionality

Disclaimer
This project is developed for educational purposes only. Use it only on networks that you own or have permission to monitor.