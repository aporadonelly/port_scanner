
## ✅ STEP-BY-STEP STARTER PLAN

### 📌 **Step 1: Understand the Big Picture**

The goal is to **build a Python program** that scans a range of IPs and ports to check if ports are open. You’ll also write some reports about how you designed it, tested it, and stayed ethical.

Think of it like this:

* 👩‍💻 You’re building a **tool** (the scanner)
* 📒 Then you’re writing **reports** (how, why, results, ethics)

---

### 🧠 **Step 2: Divide the Work (What to Focus on First)**

Start with **Core Functionality**:

* Scanning a list of ports on an IP address
* Then add support for scanning a **range of IPs** (a subnet)
* Finally, polish it with error handling

💡 Only after this core works, you add extra stuff like logging, rate limiting, and reports.

---

### ⚒️ **Step 3: Get the Basic Port Scanner Working (Today)**

Use this simple code as your starting point:

```python
import socket

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[+] Port {port} is open on {ip}")
        s.close()
    except:
        pass

# Example usage:
target_ip = '127.0.0.1'
for port in range(1, 1025):
    scan_port(target_ip, port)
```

✅ This will:

* Scan ports 1 to 1024 on `127.0.0.1` (localhost)
* Print open ports

---

### 📦 **Step 4: Build a Plan to Tackle the Whole Project**

Here’s a 2-day plan with priorities:

| Day          | Goals                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **Friday**   | ✅ Make the core port scanner work for 1 IP <br> ✅ Test with your own machine <br> ✅ Optional: add subnet scanning        |
| **Saturday** | ✅ Add error handling & input validation <br> ✅ Add optional features (rate limiting, logging) <br> ✅ Start documentation |
| **Sunday**   | ✅ Write the reports: software design, testing, ethics, scan detection <br> ✅ Final testing and polish code               |

---

### 🗃️ **Step 5: Set Up Your Folder Like This**

```
/port_scanner_project
│
├── scanner.py            # Your code
├── test_results.txt      # Logs or screenshots of tests
├── /reports
│   ├── design_report.md
│   ├── ethics_report.md
│   ├── testing_report.md
│   └── detection_report.md
```

---

### 🔬 **Step 6: Learn the Basics of ARP, ICMP, SYN (For Bonus)**

These are **not required** to make the scanner work — they’re **optional knowledge or advanced features**.

Quick intro:

* **ICMP** – Used for “ping”; you can detect if a host is online
* **ARP** – Finds MAC addresses in local networks
* **TCP SYN Scan** – More stealthy way to detect open ports (used by tools like `nmap`)

You can explore these using **`scapy`** if you finish early.

---

### 📌 Need to Assign Tasks?

If you have 4 teammates:

* **Person A** – Builds the core scanner and subnet scan
* **Person B** – Writes reports (design, testing, ethics)
* **Person C** – Adds enhancements (rate limiting, logging)
* **Person D** – Sets up VMs and tests remote scanning

---

### ✅ Summary

**Start with this today:**

* Get a basic TCP port scanner working using the `socket` module
* Test it on `localhost`
* Then test it on another VM in your subnet
* Once this works → move to error handling and optional features


