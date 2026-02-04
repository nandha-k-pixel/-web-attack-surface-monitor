import subprocess

def find_live_hosts():
    print("[+] Checking live hosts...")

    command = "cat recon/subdomains.txt | httpx -silent"
    output = subprocess.check_output(command, shell=True, text=True)

    with open("recon/live_hosts.txt", "w") as f:
        f.write(output)

    print("[+] Live hosts saved to recon/live_hosts.txt")

