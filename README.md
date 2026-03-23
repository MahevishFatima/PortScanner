# GenSPScanner
is a simple and efficient port scanner that quickly identifies open ports on a target IP or domain

# EN
## Overview
**GenSPScanner** is a simple and efficient port scanning tool. It allows users to scan a range of ports on a specified target IP address or domain, identifying open ports and potential vulnerabilities.

## Features
- **Multithreaded Scanning**: Utilizes multiple threads to accelerate the scanning process.
- **Color-Coded Output**: Provides color-coded output for better readability.
- **Error Handling**: Includes checks for valid IP addresses, domain names, and port ranges.

## Requirements
- Python 3.x
- `colorama` package (for colored output in the terminal)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/geniuszlyy/GenSPScanner.git
   ```
2. **Install dependencies**:
   ```bash
   pip install colorama
   ```

## Usage
To use GenSPScanner, execute the script with the following command:
```bash
python portscanner.py [target] [start_port] [end_port]
```
- **target**: The IP address or domain name to scan.
- **start_port**: The starting port number in the range.
- **end_port**: The ending port number in the range.

![image](https://github.com/user-attachments/assets/70d24f99-3a73-4c5f-a492-32e600200363)


## Example
```bash
python portscanner.py 192.168.1.1 1 65535
```
This command scans ports 1 to 65535 on the IP address `192.168.100.50`.

![image](https://github.com/user-attachments/assets/652b1926-046b-46ff-9ae9-ba32e5528e45)


## Output
- Open ports are displayed in a color-coded format indicating successful connections.
- Errors such as invalid IP addresses, domain names, or port ranges are highlighted with specific messages.


