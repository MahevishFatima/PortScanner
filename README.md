# 🔍 GenSPScanner – Advanced Multithreaded Port Scanner

GenSPScanner is a fast and efficient multithreaded TCP port scanner built in Python. It scans a target system (IP or domain) for open ports, identifies common services, and provides clean, readable output.

---

## 🚀 About the Project

GenSPScanner is designed to demonstrate core cybersecurity and networking concepts such as:

* TCP socket programming
* Multithreading for performance
* Port scanning techniques
* Service identification using standard port mappings

This tool is ideal for beginners in cybersecurity who want to understand how scanners like Nmap work at a basic level.

---

## ⚙️ Features

* ✅ Scan open ports on a target system
* ✅ Accept both IP address and domain name
* ✅ Automatic domain → IP resolution
* ✅ Multithreaded scanning (fast performance)
* ✅ Displays service names (HTTP, FTP, SSH, etc.)
* ✅ Clean and colored terminal output
* ✅ Exception handling for stability
* ✅ Queue-based thread management (producer-consumer model)

---

## 🧠 How It Works

1. User provides:

   * Target (IP or domain)
   * Start port
   * End port

2. Domain is resolved to IP using:

   ```python
   socket.gethostbyname()
   ```

3. Ports are added to a queue

4. Multiple threads:

   * Pull ports from queue
   * Attempt TCP connection using `socket.connect_ex()`

5. If connection succeeds:

   * Port is OPEN
   * Service name is identified using:

     ```python
     socket.getservbyport()
     ```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MahevishFatima/PortScanner.git
```

### 2. Install Dependencies

```bash
pip install colorama
```

---

## ▶️ Usage

```bash
python scanner.py [target] [start_port] [end_port]
```

### Example:

```bash
python scanner.py 192.168.1.1 1 1000
```

Or with domain:

```bash
python scanner.py example.com 20 100
```

---

## 📌 Sample Output

<img width="651" height="588" alt="image" src="https://github.com/user-attachments/assets/f53f1867-55d6-4ab8-9047-d930d8023c12" />

---

## 📊 Common Ports Detected

| Port | Service | Description             |
| ---- | ------- | ----------------------- |
| 21   | FTP     | File Transfer Protocol  |
| 22   | SSH     | Secure Shell            |
| 23   | Telnet  | Remote login (insecure) |
| 25   | SMTP    | Email transfer          |
| 80   | HTTP    | Web traffic             |
| 443  | HTTPS   | Secure web traffic      |
| 445  | SMB     | Windows file sharing    |

---

## ⚠️ Limitations

* Uses **standard port mapping**, not real service detection
* No **banner grabbing** (cannot detect service versions)
* Works only for **TCP connect scan**
* May be slower on very large ranges

---

## 🛡️ Disclaimer

This tool is created for **educational purposes only**.
Do not use it on networks or systems without proper authorization.

---

## 👨‍💻 Author

**Mahevish Fatima**
Cybersecurity Enthusiast

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share with others
* Contribute improvements

---
