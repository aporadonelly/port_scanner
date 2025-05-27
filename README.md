# 🔍 Python Port Scanner

A simple, modular, and extendable Python-based port scanner that can scan a specific IP address over a custom range of TCP ports. Built for learning, local network diagnostics, and safe testing.

---

## 🚀 Features

- Scan any target IP with a specified port range
- TCP connect-style scan (safe, no raw packets)
- Built-in logging to console and `scanner.log`
- Validates and handles input errors gracefully
- Modular codebase for easy extension
- Configurable logging and linting

---

## 📂 Project Structure

```
port_scanner/
├── logger.py           # Logging setup (console + file)
├── port_scanner.py     # Main port scanning logic
├── run_scanner.py      # Entry point script
├── scanner_utils.py    # Input validation helpers
├── scanner.log         # Log output (ignored from Git)
├── requirements.txt    # Project dependencies
├── .pylintrc           # Pylint rules
└── .gitignore          # Ignored files (e.g., venv, logs)
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

Once your virtual environment is activated:

```bash
pip install -r requirements.txt
```

---

## ✅ How to Use

```bash
python run_scanner.py
```

You will be prompted for:
- **Target IP** (e.g., `127.0.0.1`)
- **Start port** (default: `1`)
- **End port** (default: `1024`)

Example:
```text
Enter IP address to scan (default 127.0.0.1): 127.0.0.1
Enter start port (default 1): 20
Enter end port (default 80):
```

---

## 📄 Output

- Open ports will be printed in the console.
- Logs are saved in `scanner.log`.

---

## ⚙️ Developer Notes

- Customize linting rules in `.pylintrc`
- Logging config is in `logger.py`
- Add more scan types or protocols (e.g., ICMP, ARP) as needed

---

## ⚠️ Legal Notice

> This tool is intended for **educational use and testing on machines you own or are authorized to scan**. Unauthorized scanning of systems or networks may be illegal and is strictly discouraged.



