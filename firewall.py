# Import the necessary modules
import subprocess

# Define the IP range for Japan
japan_ip_range = "xxx.xxx.xxx.xxx/xx"  # Replace with the actual IP range for Japan

# Block all incoming connections from outside Japan
subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", japan_ip_range, "-j", "DROP"])
