import subprocess

def run_nuclei(live_hosts_file):
    print("[+] Running Nuclei vulnerability scan...")

    output_file = "scans/nuclei_results.txt"

    command = [
        "nuclei",
        "-l", live_hosts_file,
        "-severity", "medium,high,critical",
        "-o", output_file
    ]

    subprocess.run(command)

    print(f"[+] Nuclei scan completed")
    print(f"[+] Results saved to {output_file}")

