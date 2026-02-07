# Web Attack Surface Monitor

**Version:** v1.0.0  

# Web Attack Surface Monitor

A lightweight reconnaissance automation tool designed to identify an organization’s web attack surface by discovering subdomains and filtering live web hosts.

This project focuses on the **reconnaissance phase** of security testing, which is the foundation of bug bounty hunting and red team operations.

---

## 🚀 Features

- Subdomain enumeration using **Subfinder**
- Live host detection using **Httpx**
- Automatic output storage for analysis
- Terminal-based, fast, and scriptable
- Beginner-friendly and extensible

---

## 🛠 Tools & Technologies Used

- Python 3
- Subfinder
- Httpx
- Linux (WSL / Ubuntu)

---

## 📂 Project Structure

Web-Attack-Surface-Monitor/
│
├── main.py
├── recon/
│ ├── subdomains.txt
│ ├── live_hosts.txt
│ ├── subdomain_enum.py
│ └── live_hosts.py
└── README.md


---

## ⚙️ How It Works

1. User provides a target domain
2. The tool enumerates subdomains using Subfinder
3. Discovered subdomains are saved to a file
4. Httpx checks which subdomains are live
5. Live hosts are saved for further testing

---
## Changelog

### v1.0.0
- Subdomain enumeration using Subfinder
- Live host detection using Httpx
- Vulnerability scanning using Nuclei
- Scan results saved to files

## ▶️ Usage

```bash
python3 main.py

=== Web Attack Surface Monitor ===
Enter target domain: testphp.vulnweb.com
[+] Finding subdomains...
[+] Subdomains saved to recon/subdomains.txt
[+] Checking live hosts...
[+] Live hosts saved to recon/live_hosts.txt
[+] Scan completed successfully

# Web Attack Surface Monitor

**Version:** v1.1.1  
**Status:** Stable  
**Category:** Reconnaissance & Vulnerability Scanning

Web Attack Surface Monitor is an automated security reconnaissance tool
that discovers web assets and scans them for known vulnerabilities using
industry-standard open-source tools.

---

## 🚀 Features

- Subdomain enumeration using Subfinder
- Live host detection using Httpx
- Vulnerability scanning using Nuclei
- Categorized scanning (CVEs, Exposures, Cloud, DNS)
- Clean file-based output
- Beginner-friendly and extensible

---

## 🛠 Tools Used

- Python 3
- Subfinder
- Httpx
- Nuclei
- Linux (WSL / Ubuntu)

---

## 📂 Project Structure
web-attack-surface-monitor/
├── main.py
├── recon/
│ ├── subdomains.txt
│ └── live_hosts.txt
├── scanner/
│ └── vuln_scan.py
├── scans/
│ ├── cves_results.txt
│ ├── exposures_results.txt
│ ├── cloud_results.txt
│ └── dns_results.txt
└── README.md

---

## ⚙️ How It Works

1. User provides a target domain
2. Subdomains are enumerated
3. Live hosts are identified
4. Nuclei templates scan live hosts
5. Results are saved for analysis

---

## ▶️ Usage

```bash
python3 main.py

## Output


🔒 Legal Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Do not use this tool on systems without proper permission.

👨‍💻 Author

Nandhakumar
Cyber Security Student | Aspiring Red Team Operator
