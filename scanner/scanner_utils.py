import ipaddress
from scapy.all import ICMP, IP, sr1, ARP, Ether, srp

def validate_port_range(start, end):
    if 0 < start <= 65535 and 0 < end <= 65535 and start <= end:
        return True
    raise ValueError("Port range must be between 1 and 65535 and start <= end")

def parse_port_input(start_str, end_str, default_start=1, default_end=1024):
    start = int(start_str) if start_str else default_start
    end = int(end_str) if end_str else default_end
    validate_port_range(start, end)
    return start, end

def parse_ip_input(ip_input):
    """Accepts a single IP or subnet (e.g., 192.168.56.0/28) and returns a usable ips"""
    try:
        network = ipaddress.ip_network(ip_input, strict=False) #strict=False 
        return [str(ip) for ip in network.hosts()]
    except ValueError as exc:
        raise ValueError("Invalid IP address or subnet.") from exc

def is_host_up(ip, timeout=1):
    try:
        packet = IP(dst=ip)/ICMP()
        reply = sr1(packet, timeout=timeout, verbose=0)
        return reply is not None
    except PermissionError:
        print("ICMP requires root permission")
        return True

def arp_scan(subnet):
    arp_req = ARP(pdst=subnet)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp_req
    answered, _ = srp(packet, timeout=2, verbose=0)
    return [resp.psrc for _, resp in answered]
