import subprocess

def find_subdomains(domain):
    print("[+] Finding subdomains...")

    command = f"subfinder -d {domain} -silent -timeout 10"
    output = subprocess.check_output(command, shell=True, text=True)

    with open("recon/subdomains.txt", "w") as f:
        f.write(output)

    print("[+] Subdomains saved to recon/subdomains.txt")
