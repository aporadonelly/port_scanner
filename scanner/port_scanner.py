# scanner/port_scanner.py
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from scanner.logger import setup_logger

logger = setup_logger()

def scan_port(ip, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
            logger.info(f"[+] Port {port} is open on {ip}")
            return port
    return None

def scan_ports(target_ip, port_range=(1, 1024), timeout=1, max_threads=100):
    logger.info(f"Scanning {target_ip} from port {port_range[0]} to {port_range[1]}")
    start_time = datetime.now()
    open_ports = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, target_ip, port, timeout) for port in range(port_range[0], port_range[1] + 1)]
        for f in futures:
            result = f.result()
            if result:
                open_ports.append(result)

    duration = datetime.now() - start_time
    logger.info(f"Scan completed in {duration}")
    return sorted(open_ports)
