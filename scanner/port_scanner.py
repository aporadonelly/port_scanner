# This file is for main scanning logic, threading, queue management
import socket
from datetime import datetime
from scanner.logger import setup_logger

logger = setup_logger()

def scan_ports(target_ip, port_range=(1, 1024), timeout=1):
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

    duration = datetime.now() - start_time  
    logger.info("Scan completed in %s", duration)

    return open_ports
