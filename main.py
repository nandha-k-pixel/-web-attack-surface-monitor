from recon.subdomain_enum import find_subdomains
from recon.live_hosts import find_live_hosts

print("=== Web Attack Surface Monitor ===")

domain = input("Enter target domain: ").strip()

find_subdomains(domain)
find_live_hosts()

print("[+] Scan completed successfully")

