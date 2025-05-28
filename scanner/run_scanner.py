from scanner.scanner_utils import parse_port_input, parse_ip_input
from scanner.port_scanner import scan_ports

def main():
    target_input = (input("Enter target IP or subnet (e.g. 192.168.56.0/28): ") or "127.0.0.1").strip()
    start_port = input("Enter start port (default 1): ")
    end_port = input("Enter end port (default 1024): ")

    try:
        ip_list = parse_ip_input(target_input)
        start, end = parse_port_input(start_port, end_port)

        for ip in ip_list:
            print(f"\nScanning {ip}...")
            open_ports = scan_ports(ip, (start, end))
            print(f"Open ports on {ip}: {open_ports}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
