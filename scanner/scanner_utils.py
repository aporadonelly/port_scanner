import ipaddress

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
    """Accepts single IP, CIDR subnet, or IP range (e.g., 192.168.1.5-192.168.1.20)"""
    ip_input = ip_input.strip()

    if "-" in ip_input:
        start_ip, end_ip = ip_input.split("-")
        try:
            start = ipaddress.IPv4Address(start_ip)
            end = ipaddress.IPv4Address(end_ip)
            if start > end:
                raise ValueError("Start IP must be less than or equal to end IP")

            networks = list(ipaddress.summarize_address_range(start, end))
            hosts = []
            for network in networks:
                hosts.extend([str(ip) for ip in network.hosts()])
            return hosts

        except ipaddress.AddressValueError:
            raise ValueError("Invalid IP range format")

    try:
        network = ipaddress.ip_network(ip_input, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as exc:
        try:
            ip = ipaddress.IPv4Address(ip_input)
            return [str(ip)]
        except ipaddress.AddressValueError:
            raise ValueError("Invalid IP address or subnet.") from exc
