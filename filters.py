from scapy.layers.inet import TCP, UDP, ICMP

def packet_filter(packet, choice):

    if choice == "1":
        return True

    elif choice == "2":
        return packet.haslayer(TCP)

    elif choice == "3":
        return packet.haslayer(UDP)

    elif choice == "4":
        return packet.haslayer(ICMP)

    return True