from scapy.all import wrpcap
import os

def save_log(data):
    file_path = os.path.join(os.path.dirname(__file__), "packet_logs.txt")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(data + "\n")


def save_pcap(packets):
    file_path = os.path.join(os.path.dirname(__file__), "captured_packets.pcap")

    wrpcap(file_path, packets)

    print("\nPCAP file saved successfully!")
    print(f"Location: {file_path}")