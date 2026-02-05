from recon.subdomain_enum import find_subdomains
from recon.live_hosts import find_live_hosts
from scans.vuln_scan import run_nuclei

print("=== Web Attack Surface Monitor ===")

domain = input("Enter target domain: ").strip()

find_subdomains(domain)
find_live_hosts()
run_nuclei("recon/live_hosts.txt")

print("[+] Scan completed successfully")

