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
    """Accepts a single IP or subnet (e.g., 192.168.56.0/28)"""
    try:
        network = ipaddress.ip_network(ip_input, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as exc:
        raise ValueError("Invalid IP address or subnet.") from exc
