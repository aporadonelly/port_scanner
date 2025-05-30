
---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/port_scanner.git
cd port_scanner
```

### 2. Create and activate a virtual environment
🔹 macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
🔹Windows (CMD):
```bash
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```


### How to Run
From the project root:
```bash
python3 run_scanner.py
```

You’ll be prompted to choose:

Scan type: tcp, arp, or icmp 
### if choosing ARP, admin priviliged must be used: 
```bash
sudo python run_scanner.py
```

Target IP or subnet (e.g., 127.0.0.1, 192.168.56.0/28)

Port range for TCP (e.g., 20-80 or 443)


### Output
Open ports and live hosts are printed to the terminal.

Logs are saved in scanner.log.

=============================

### 🐳 Docker Test Environment
🧱 Build & Start Containers
```bash
docker compose up --build
```
This starts:

scanner container at 192.168.56.20

remote-host (HTTP on port 8000) at 192.168.56.10

remote-host-2 (HTTP on port 8080) at 192.168.56.11

These containers live on an isolated Docker subnet: 192.168.56.0/24

### Stop Containers
```bash
docker compose down
```


### Run in Background
```bash
docker compose up -d
```


