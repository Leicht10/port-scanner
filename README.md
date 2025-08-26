# 🔍 Python Port Scanner

A simple **multithreaded port scanner** written in Python.  
It scans a given host across a specified port range and prints **only the open ports**.

---

## 🚀 Features
- Scan IP addresses or domain names
- Fast scanning with **ThreadPoolExecutor**
- Customizable port ranges
- Clean output: **only open ports shown**
- Reports if **no open ports** are found

---

## ⚡ Usage
```bash
python3 port_scanner.py --host example.com --start 1 --end 100
