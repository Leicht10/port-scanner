import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import ipaddress


def scan_port(port, ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()

    if result == 0:
        return f"port {port} is open"
    return None



line = argparse.ArgumentParser()
line.add_argument("--host", required=True, help="target host to scan")
line.add_argument("--start", type=int, required=True, help="first port")
line.add_argument("--end", type=int, required=True, help="last port")
ok = line.parse_args()


try:
    ip = str(ipaddress.ip_address(ok.host))
except ValueError:
    ip = socket.gethostbyname(ok.host)
except Exception:
    print("ERROR: invalid IP address or hostname")
    exit()


port_range = ok.end - ok.start
if port_range < 500:
    m = port_range
else:
    m = 500


open_ports = []
with ThreadPoolExecutor(max_workers=m) as workers:
    futures = [workers.submit(scan_port, p, ip) for p in range(ok.start, ok.end + 1)]
    for f in as_completed(futures):
        result = f.result()
        if result:
            open_ports.append(result)


if open_ports:
    for port in sorted(open_ports):
        print(port)
else:
    print("No open ports found in this range.")
