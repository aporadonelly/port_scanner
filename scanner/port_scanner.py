# scanner/port_scanner.py
import socket
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style

from scanner.logger import setup_logger

init(autoreset=True) # autoreset=True ensures that styles don't bleed across lines.

logger = setup_logger()

def scan_port(ip, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
            logger.info(f"[+] Port {port} is open on {ip}")
            return port
    return None

def scan_ports(target_ip, port_range=(1, 1024), timeout=1, max_threads=100, rate_limit=0.01):
    logger.info(f"Starting scan on {target_ip} from port {port_range[0]} to {port_range[1]}")
    start_time = datetime.now()
    open_ports = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for port in range(port_range[0], port_range[1] + 1):
            futures.append(executor.submit(scan_port, target_ip, port, timeout))
            time.sleep(rate_limit)  # rate limit between submissions

        for f in futures:
            result = f.result()
            if result:
                open_ports.append(result)

    duration = datetime.now() - start_time
    logger.info(f"Finished scan on {target_ip} in {duration}. Open ports: {open_ports}")
    return sorted(open_ports)
