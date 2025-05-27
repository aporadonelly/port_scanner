# This file is for scanning utilities: ICMP ping, SYN scan, parsing, etc.
def validate_port_range(start, end):
    if 0 < start <= 65535 and 0 < end <= 65535 and start <= end:
        return True
    raise ValueError("Port range must be between 1 and 65535 and start <= end")

def parse_port_input(start_str, end_str, default_start=1, default_end=1024):
    start = int(start_str) if start_str else default_start
    end = int(end_str) if end_str else default_end
    validate_port_range(start, end)
    return start, end
