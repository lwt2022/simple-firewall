import socket

# Define the IP ranges for Japan
japan_ip_ranges = [
    ("1.0.16.0", "1.0.31.255"),
    ("1.0.64.0", "1.0.127.255"),
    ("1.1.64.0", "1.1.127.255"),
    # Add more IP ranges here
]

def is_japan_ip(ip_address):
    # Convert the IP address to an integer for comparison
    ip_int = ip_to_int(ip_address)

    # Check if the IP falls within any of the defined IP ranges
    for start, end in japan_ip_ranges:
        if ip_int >= ip_to_int(start) and ip_int <= ip_to_int(end):
            return True

    return False

def ip_to_int(ip_address):
    # Convert the IP address to an integer representation
    ip_parts = ip_address.split(".")
    ip_int = 0
    for i in range(4):
        ip_int += int(ip_parts[i]) << (24 - (8 * i))
    return ip_int

# Test the firewall script
def test_firewall():
    while True:
        source_ip = input("Enter source IP address (q to quit): ")
        if source_ip == "q":
            break

        if is_japan_ip(source_ip):
            print("Connection allowed from Japan.")
        else:
            print("Connection blocked. Not from Japan.")

test_firewall()
