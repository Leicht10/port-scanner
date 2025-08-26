[Extra Notes – Python Port Scanner]

Usage

- Run with:
  `python3 port_scanner.py --host <target> --start <first_port> --end <last_port>`
- Works with both IP addresses and domain names.
- Example:
  `python3 port_scanner.py --host scanme.nmap.org --start 20 --end 100`

Output

- Shows only **open ports** in the given range.
- If no ports are open, prints:
  `No open ports found in this range.`

Implementation

- Uses Python’s `socket` library with a timeout of 1 second.
- Employs `ThreadPoolExecutor` for faster concurrent scans.
- Worker threads capped at 500 to prevent overload.

Reflection

- The scanner is simple but effective for quickly checking open ports.
- Output is clean and user-friendly, focusing only on actionable results.
- Good exercise in networking basics, concurrency, and error handling.
