# GenSPScanner
is a simple and efficient port scanner that quickly identifies open ports on a target IP or domain

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


## Example
```bash
python portscanner.py 192.168.100.50 1 1000
```
This command scans ports 1 to 1000 on the IP address `192.168.100.50`.

<img width="590" height="234" alt="image" src="https://github.com/user-attachments/assets/4736299d-a40d-481e-8628-fd5410019f0a" />

## Output
- Open ports are displayed in a color-coded format indicating successful connections.
- Errors such as invalid IP addresses, domain names, or port ranges are highlighted with specific messages.


