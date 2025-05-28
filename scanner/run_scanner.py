from scanner.scanner_utils import parse_port_input, parse_ip_input, is_host_up
from scanner.port_scanner import scan_ports, syn_scan

def main():
    target_input = (input("Enter target IP or subnet (e.g. 192.168.56.0/28): ") or "127.0.0.1").strip()
    start_port = input("Enter start port (default 1): ")
    end_port = input("Enter end port (default 1024): ")
    scan_type = input("Scan type: [1] TCP Connect (default) or [2] TCP SYN: ").strip()

    try:
        ip_list = parse_ip_input(target_input)
        start, end = parse_port_input(start_port, end_port)

        for ip in ip_list:
            print(f"\nPinging {ip} with ICMP...")
            if is_host_up(ip):
                print(f"✅ Host {ip} is up. Starting {'SYN' if scan_type == '2' else 'Connect'} scan...")
                open_ports = []

                if scan_type == "2":
                    for port in range(start, end + 1):
                        if syn_scan(ip, port):
                            print(f"[+] Port {port} is open")
                            open_ports.append(port)
                else:
                    open_ports = scan_ports(ip, (start, end))

                print(f"Open ports on {ip}: {open_ports}")
            else:
                print(f"❌ Host {ip} is down or not responding to ICMP.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
