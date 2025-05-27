#!/usr/bin/env python3
"""Using shebang to run it easily"""
# Importing necessary modules
import socket
import time

# Ask the user for the target hostname or IP address
target = input('Enter the target host (e.g., example.com or IP address): ')

# Resolve the IP address of the target
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Unable to resolve host.")
    exit()

print(f'Starting scan on host: {target_ip}')

# Function to scan a specific port
def port_scan(port):
    """Scan a single port on the target IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for the connection attempt
            result = s.connect_ex((target_ip, port))  # Returns 0 if successful
            return result == 0
    except (socket.timeout, socket.error) as e:
        print(f"Error scanning port {port}: {e}")
        return False

# Record the start time
start = time.time()

# Scan ports 0 to 4
for port_num in range(5):  # we can change the range of ports here
    if port_scan(port_num):
        print(f'Port {port_num} is open')
    else:
        print(f'Port {port_num} is closed')

# Record the end time and display the time taken
end = time.time()
print(f'Time taken: {end - start:.2f} seconds')
