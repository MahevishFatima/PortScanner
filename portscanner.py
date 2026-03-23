import os
import re
import sys
import threading
import socket
from queue import Queue
from colorama import Fore, init

# Initialize colorama for colored console text
init(autoreset=True)

# LOGO = f"""
r"""
{Fore.LIGHTRED_EX}   _____             _____ _____   _____                                 
  / ____|           / ____|  __ \ / ____|                                
 | |  __  ___ _ __ | (___ | |__) | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | | |_ |/ _ \ '_ \ \___ \|  ___/ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |__| |  __/ | | |____) | |     ____) | (_| (_| | | | | | | |  __/ |   
  \_____|\___|_| |_|_____/|_|    |_____/ \___\__,_|_| |_|_| |_|\___|_|                     
print(LOGO)                                                                                                                                                                                 
"""


# Program logo
LOGO = fr"""

{Fore.LIGHTRED_EX}   _____             _____ _____   _____                                 
  / ____|           / ____|  __ \ / ____|                                
 | |  __  ___ _ __ | (___ | |__) | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | | |_ |/ _ \ '_ \ \___ \|  ___/ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |__| |  __/ | | |____) | |     ____) | (_| (_| | | | | | | |  __/ |   
  \_____|\___|_| |_|_____/|_|    |_____/ \___\__,_|_| |_|_| |_|\___|_|   

        GenSPScanner • Port Scanner Tool
"""
print(LOGO)

# Check for correct number of command-line arguments
if len(sys.argv) != 4:
    print(f"""
        {Fore.LIGHTYELLOW_EX}╭────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╮
        | {Fore.LIGHTGREEN_EX}Use » python {os.path.basename(__file__)} [target] [start_port] [end_port]   {Fore.LIGHTYELLOW_EX}| 
        ╰────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╯
    """)
    sys.exit(1)

# Get target IP address and port range
target_ip = str(sys.argv[1])
port_start = int(sys.argv[2])
port_end = int(sys.argv[3])

# Validate IP address or domain name
ip_pattern = re.compile(
    r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"  # IPv4
    r"|"
    r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"  # Domain name
)
if not ip_pattern.match(target_ip):
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Error! Invalid IP address or domain name.")
    sys.exit(1)

# Validate port range input
try:
    port_start = int(port_start)
    port_end = int(port_end)
    if port_start < 0 or port_end > 65535 or port_start > port_end:
        raise ValueError
except ValueError:
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Error! Invalid port range. Ports must be between 0–65535.")
    sys.exit(1)

# Create a lock for synchronized output
output_lock = threading.Lock()

# Function to scan a port
def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set timeout to speed up scanning
        try:
            sock.connect((target_ip, port))
            with output_lock:
                print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTMAGENTA_EX}{target_ip}:{port} {Fore.LIGHTGREEN_EX}(Open)")
        except:
            pass

# Worker thread function to scan ports from queue
def worker_thread():
    while True:
        port = port_queue.get()
        if port is None:
            break
        scan_port(port)
        port_queue.task_done()

# Create a queue to manage threads
port_queue = Queue()

# Create and start threads
threads = []
for _ in range(500):
    thread = threading.Thread(target=worker_thread)
    thread.daemon = True
    thread.start()
    threads.append(thread)

# Add port range to the queue
for port in range(port_start, port_end + 1):
    port_queue.put(port)

# Wait for all tasks to complete
port_queue.join()

# Stop threads
for _ in range(500):
    port_queue.put(None)
for thread in threads:
    thread.join()

print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Scanning completed.")