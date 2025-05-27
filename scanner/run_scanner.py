# This is our entry file that a we use to run the application.
from scanner.scanner_utils import parse_port_input
from scanner.port_scanner import scan_ports

def main():
    # target = input("Enter IP address to scan (default 127.0.0.1): ") or "127.0.0.1"
    target = (input("Enter IP address to scan (default 127.0.0.1): ") or "127.0.0.1").strip() #added strip() to remove extra spaces
    start_port = input("Enter start port (default 1): ")
    end_port = input("Enter end port (default 1024): ")

    try:
        start, end = parse_port_input(start_port, end_port)
        open_ports = scan_ports(target, (start, end))
        print(f"Open ports: {open_ports}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
