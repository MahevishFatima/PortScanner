"""
GenSPScanner - Advanced Multithreaded Port Scanner

This script scans a target system (IP or domain) for open TCP ports
within a given range. It uses multithreading to speed up scanning
and identifies common services running on open ports.

Features:
- Accepts IP address or domain name
- Resolves domain names to IP addresses
- Scans a range of ports
- Detects open ports using TCP connection
- Displays standard service names (HTTP, FTP, etc.)
- Uses multithreading for faster execution
- Handles exceptions gracefully
"""

import os
import re
import sys
import threading
import socket
from queue import Queue
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Logo
LOGO = fr"""
{Fore.LIGHTRED_EX}   _____             _____ _____   _____                                 
  / ____|           / ____|  __ \ / ____|                                
 | |  __  ___ _ __ | (___ | |__) | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | | |_ |/ _ \ '_ \ \___ \|  ___/ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |__| |  __/ | | |____) | |     ____) | (_| (_| | | | | | | |  __/ |   
  \_____|\___|_| |_|_____/|_|    |_____/ \___\__,_|_| |_|_| |_|\___|_|   

        GenSPScanner • Advanced Port Scanner
"""
print(LOGO)

# Argument check
if len(sys.argv) != 4:
    print(f"""
{Fore.LIGHTYELLOW_EX}Usage:
python {os.path.basename(__file__)} [target] [start_port] [end_port]
""")
    sys.exit(1)

target_input = sys.argv[1]

# Validate IP / Domain
ip_pattern = re.compile(
    r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    r"|"
    r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
)

if not ip_pattern.match(target_input):
    print(f"{Fore.RED}Invalid IP address or domain name.")
    sys.exit(1)

# Resolve domain → IP
try:
    target_ip = socket.gethostbyname(target_input)
    print(f"{Fore.CYAN}Resolved Target: {target_input} → {target_ip}")
except socket.gaierror:
    print(f"{Fore.RED}Failed to resolve domain.")
    sys.exit(1)

# Port range validation
try:
    port_start = int(sys.argv[2])
    port_end = int(sys.argv[3])

    if port_start < 0 or port_end > 65535 or port_start > port_end:
        raise ValueError
except ValueError:
    print(f"{Fore.RED}Invalid port range (0–65535).")
    sys.exit(1)

# Thread-safe print lock
output_lock = threading.Lock()

def scan_port(port):
    """
    Attempts to connect to a given port on the target IP.

    Parameters:
        port (int): Port number to scan

    Behavior:
        - Creates a TCP socket
        - Tries to establish a connection
        - If successful, identifies the service name
        - Prints open port details

    Exception Handling:
        - Handles timeout errors
        - Handles socket connection errors
        - Catches unexpected exceptions safely
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except:
                    service = "Unknown"

                with output_lock:
                    print(f"{Fore.YELLOW}[OPEN] {target_ip}:{port} ({service})")

    except socket.timeout:
        pass
    except socket.error:
        pass
    except Exception as e:
        with output_lock:
            print(f"{Fore.RED}Error on port {port}: {e}")


def worker():
    """
    Worker thread function.

    Continuously retrieves ports from the queue and scans them.
    Stops execution when it receives a 'None' signal.

    Workflow:
        1. Get port from queue
        2. Call scan_port()
        3. Mark task as done
    """
    while True:
        port = port_queue.get()
        if port is None:
            break
        scan_port(port)
        port_queue.task_done()


# Queue to manage ports
port_queue = Queue()

# Thread pool
THREAD_COUNT = 100
threads = []

for _ in range(THREAD_COUNT):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

# Add ports to queue
for port in range(port_start, port_end + 1):
    port_queue.put(port)

# Wait for all tasks to complete
port_queue.join()

# Stop threads
for _ in range(THREAD_COUNT):
    port_queue.put(None)

for t in threads:
    t.join()

print(f"{Fore.GREEN}Scanning completed.")