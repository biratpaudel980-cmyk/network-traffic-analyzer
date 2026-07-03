cat << 'EOF' > traffic_analyzer.py
from scapy.all import sniff, IP, TCP, UDP
import datetime

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        protocol = "Other"
        src_port = "N/A"
        dst_port = "N/A"
        
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        print(f"[{timestamp}] {protocol} Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

def main():
    print("[-] Starting network sniffer... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
EOF
