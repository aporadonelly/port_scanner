import socket
import time
from datetime import datetime
from scanner.logger import setup_logger
from scapy.all import IP, TCP, sr1

logger = setup_logger()

def scan_ports(target_ip, port_range=(1, 1024), timeout=1, rate_limit=0.1):
    logger.info("Scanning %s from port %s to %s", target_ip, port_range[0], port_range[1])
    open_ports = []

    start_time = datetime.now()
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                logger.info("[+] Port %s is open", port)
                open_ports.append(port)
        time.sleep(rate_limit)  # Rate limiting to avoid excessive scanning

    duration = datetime.now() - start_time
    logger.info("Scan completed in %s", duration)
    return open_ports

def syn_scan(ip, port):
    packet = IP(dst=ip)/TCP(dport=port, flags='S')
    response = sr1(packet, timeout=1, verbose=0)
    if response is None:
        return False
    elif response.haslayer(TCP) and response[TCP].flags == 0x12:
        return True
    return False
