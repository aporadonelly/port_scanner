# 🔍 Python Port Scanner

## 🛠️ Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/port_scanner.git
cd port_scanner
```


### 2️⃣ Create and Activate a Virtual Environment

#### 🔹 macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔹 Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```



### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```



## ▶️ Running the Scanner Locally

```bash
python3 run_scanner.py
```

We'll be prompted to choose:

* **Scan type**: `tcp`, `arp`, or `icmp`
* **Target**: a single IP, range, or subnet
* **Port range**: only required for TCP scans



### 📟 Example Targets

#### ✅ Single IP

```bash
127.0.0.1
192.168.100.10
```

#### ✅ Range of IPs

```bash
192.168.100.10-192.168.100.20
```

#### ✅ Subnet (CIDR Notation)

```bash
192.168.100.0/28
```



### ARP Scans Require Admin Privileges

```bash
sudo python3 run_scanner.py
```



### Port Range Examples (TCP only)

```bash
22-80
443
```



### 📟 ICMP Example

```bash
Scan type: icmp
Target: 192.168.100.0/28
```



### 📟 ARP Example

```bash
Scan type: arp
Target: 192.168.100.0/24
```


## 📄 Output

* ✅ Open ports and live hosts are printed in the terminal
* ✅ Detailed logs are saved to `scanner.log`



## 🐳 Docker Test Environment

Our project includes a self-contained Docker testing lab with:

| Container       | Role             | IP Address       | Details           |
| --------------- | ---------------- | ---------------- | ----------------- |
| `scanner`       | Scanner CLI      | `192.168.100.20` | Runs this scanner |
| `remote-host`   | HTTP test server | `192.168.100.10` | Port `8000` open  |
| `remote-host-2` | HTTP test server | `192.168.100.11` | Port `8080` open  |

---

### 🧱 Build Docker Images

From our project root (where `docker-compose.yml` and `Dockerfile` live), do the ff.:

```bash
docker compose build
```

---

### ▶️ Start Containers and run it in the background

```bash
docker compose up -d
```

---

### 🚫 Stop Containers

```bash
docker compose down
```
