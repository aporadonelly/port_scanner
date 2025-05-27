#!/usr/bin/env python3

"""Module providing a function printing python version."""
import argparse
import ipaddress
import socket
import threading
import time
from datetime import datetime
from queue import Queue
from colorama import init, Fore, Style

# Initialize colorama
init()

# Lock for thread-safe print and logging
print_lock = threading.Lock()
log_lock = threading.Lock()

# Shared results
scan_results = {}

# Function to scan a single port on a host
def scan_port(ip, port, timeout, verbose):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((str(ip), port))
            with print_lock:
                if result == 0:
                    print(f"{Fore.GREEN}[+] {ip}:{port} OPEN{Style.RESET_ALL}")
                    scan_results.setdefault(str(ip), []).append(port)
                elif verbose:
                    print(f"{Fore.RED}[-] {ip}:{port} CLOSED{Style.RESET_ALL}")
    except socket.error:
        with print_lock:
            print(f"{Fore.YELLOW}[!] Could not connect to {ip}:{port}{Style.RESET_ALL}")

# Worker function for threads
def worker(queue, timeout, verbose, delay):
    while not queue.empty():
        ip, port = queue.get()
        scan_port(ip, port, timeout, verbose)
        queue.task_done()
        if delay:
            time.sleep(delay)

# Parse port range and list
def parse_ports(port_str):
    ports = set()
    parts = port_str.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    return sorted(p for p in ports if 0 < p < 65536)

# Parse target IPs from input
def parse_targets(target_str):
    try:
        if '/' in target_str:
            return list(ipaddress.ip_network(target_str, strict=False).hosts())
        elif '-' in target_str:
            start_ip, end_ip = target_str.split('-')
            start = ipaddress.IPv4Address(start_ip)
            end = ipaddress.IPv4Address(end_ip)
            return [ipaddress.IPv4Address(ip) for ip in range(int(start), int(end)+1)]
        else:
            return [ipaddress.ip_address(target_str)]
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid target IP format")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument('--target', '-t', required=True, help='Target IP, range (start-end), or subnet (e.g. 192.168.1.0/24)')
    parser.add_argument('--ports', '-p', default='1-1024', help='Ports to scan (e.g. 22,80,443 or 1-1024)')
    parser.add_argument('--timeout', type=float, default=1.0, help='Connection timeout in seconds (default: 1.0)')
    parser.add_argument('--threads', type=int, default=100, help='Number of concurrent threads (default: 100)')
    parser.add_argument('--delay', type=float, default=0.0, help='Delay between scans in seconds (default: 0.0)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show closed ports')
    parser.add_argument('--output', help='Path to output log file')

    args = parser.parse_args()

    try:
        targets = parse_targets(args.target)
        ports = parse_ports(args.ports)
    except argparse.ArgumentTypeError as e:
        print(f"[!] {e}")
        return

    print(f"[i] Starting scan on {len(targets)} target(s) for ports: {ports[:5]}... ({len(ports)} total)")
    start_time = datetime.now()

    q = Queue()
    for ip in targets:
        for port in ports:
            q.put((ip, port))

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(q, args.timeout, args.verbose, args.delay))
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

    duration = datetime.now() - start_time
    print(f"\n[i] Scan completed in {duration}\n")

    if scan_results:
        print("Open ports:")
        for host, open_ports in scan_results.items():
            print(f"{host}: {sorted(open_ports)}")

    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(f"Scan Report - {datetime.now()}\n")
                for host, open_ports in scan_results.items():
                    f.write(f"{host}: {sorted(open_ports)}\n")
            print(f"[i] Results saved to {args.output}")
        except IOError:
            print(f"[!] Could not write to file {args.output}")

if __name__ == '__main__':
    main()
