# 🔍 Python Port Scanner

A simple, modular, and extendable Python-based port scanner that scans a specific IP address over a custom range of TCP ports. Ideal for network diagnostics, learning, and safe testing environments.

---

## 🚀 Features

- TCP connect-style port scanning
- Clean modular structure using a Python package (`scanner/`)
- Input validation and error handling
- Logging to both console and `scanner.log`
- Configurable scan range and target
- Pylint-configured with `.pylintrc`

---

## 📂 Project Structure

```
port_scanner/
├── scanner/                # Main package folder
│   ├── __init__.py         # Makes it a package
│   ├── logger.py           # Logging setup
│   ├── port_scanner.py     # Scanning logic
│   ├── run_scanner.py      # Entry point
│   └── scanner_utils.py    # Input and port/IP validation
├── requirements.txt        # Python dependencies
├── .pylintrc               # Linting configuration
├── .gitignore              # Files/folders excluded from Git
└── README.md               # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/port_scanner.git
cd port_scanner
```

---

### 2. Create and activate a virtual environment

#### 🔹 On **macOS / Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔹 On **Windows (CMD)**:

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### 🔹 On **Windows (PowerShell)**:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

> 💡 If activation fails in PowerShell due to a policy error, run:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

From the root directory:

```bash
python -m scanner.run_scanner
```

You’ll be prompted to enter:
- Target IP (e.g. `127.0.0.1`, `scanme.nmap.org`)
- Start port (e.g. `20`)
- End port (e.g. `80`)

---

## 📄 Output

- Open ports will be printed in the terminal.
- Logs saved to `scanner.log`.

---

## ⚙️ Developer Notes

- Configure logging in `scanner/logger.py`
- Modify scanning behavior in `scanner/port_scanner.py`
- Customize rules in `.pylintrc`
- Exclude dev files via `.gitignore`

---

## ⚠️ Legal Notice

> This tool is intended for **educational and authorized testing only**. Do not scan networks without explicit permission.




## Steps to start the container for testing: 
On the terminal do the following to build the network (test-net), boots the remote-host, and starts a Python HTTP server on 192.168.56.10:8000:
-- docker compose up

To shut down the container: 
-- docker compose down 

To let container run in the backgroud: (I use this most of the time)
--docker compose up -d 
