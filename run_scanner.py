# run_scanner.py
from scanner.scanner_utils import parse_port_input, parse_ip_input
from scanner.port_scanner import scan_ports
from scanner.network_scanner import arp_scan, icmp_scan
from scanner.logger import setup_logger

logger = setup_logger()

def main():
    try:
        print("🔍 Welcome to the Python Port Scanner")

        scan_type = input("Choose scan type [tcp/arp/icmp] (default: tcp): ").strip().lower() or "tcp"
        while scan_type not in ["tcp", "arp", "icmp"]:
            scan_type = input("Invalid type. Choose [tcp/arp/icmp]: ").strip().lower()

        target = input("Enter target IP or subnet (default: 127.0.0.1): ").strip() or "127.0.0.1"

        if scan_type in ["arp", "icmp"]:
            if scan_type == "arp":
                live_hosts = arp_scan(target)
            else:
                live_hosts = icmp_scan(target)

            print(f"\nActive hosts ({scan_type.upper()}):")
            for host in live_hosts:
                print(f" - {host}")
            return

        # TCP scan
        port_input = input("Enter port range (e.g. 20-80, default: 1-1024): ").strip() or "1-1024"
        # port_start, port_end = parse_port_input(*port_input.split("-"))
        if "-" in port_input:
            port_start, port_end = parse_port_input(*port_input.split("-"))
        else:
                port_start, port_end = parse_port_input(port_input, port_input)

        ip_list = parse_ip_input(target)

        for ip in ip_list:
            print(f"\nScanning {ip}...")
            open_ports = scan_ports(ip, (port_start, port_end))
            print(f"Open ports on {ip}: {open_ports}")

    except KeyboardInterrupt:
        logger.warning("Scan interrupted by user (Ctrl+C)")
        print("\n⚠️ Scan canceled by user. Exiting gracefully...")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
