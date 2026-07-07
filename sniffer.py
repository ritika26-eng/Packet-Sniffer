import os

print("NEW SNIFFER FILE LOADED")
print("Running file:", __file__)
print("Current folder:", os.getcwd())
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

from filters import packet_filter
from utils import get_hostname
from logger import save_log, save_pcap

packet_count = 0
captured_packets = []

print("\n===== Packet Sniffer =====")
print("1. Capture All Packets")
print("2. Capture TCP Packets")
print("3. Capture UDP Packets")
print("4. Capture ICMP Packets")

choice = input("\nEnter your choice (1-4): ")

def process_packet(packet):
    global packet_count, captured_packets

    if not packet_filter(packet, choice):
        return

    packet_count += 1
    captured_packets.append(packet)

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        src_host = get_hostname(src_ip)
        dst_host = get_hostname(dst_ip)

        protocol = "Other"
        src_port = "-"
        dst_port = "-"

        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output = (
            f"\n{'='*50}\n"
            f"Packet #{packet_count}\n"
            f"Time             : {time_now}\n"
            f"Source IP        : {src_ip}\n"
            f"Source Host      : {src_host}\n"
            f"Destination IP   : {dst_ip}\n"
            f"Destination Host : {dst_host}\n"
            f"Protocol         : {protocol}\n"
            f"Source Port      : {src_port}\n"
            f"Destination Port : {dst_port}\n"
            f"Packet Length    : {len(bytes(packet))} bytes"
        )

        print(output)
        save_log(output)


def start_sniffing():
    print("\nStarting Packet Sniffer...")
    print("Press Ctrl + C to stop.\n")

    try:
        sniff(prn=process_packet, store=False)

    except KeyboardInterrupt:
        print("\nStopping Packet Sniffer...")

    finally:
        if captured_packets:
            save_pcap(captured_packets)
            print(f"Total Packets Saved: {len(captured_packets)}")
        else:
            print("No packets captured.")