import subprocess

def run_nuclei(live_hosts):
    print("[+] Running Nuclei vulnerability scan...")

    template_paths = [
        "~/nuclei-templates/http/cves",
        "~/nuclei-templates/http/exposures",
        "~/nuclei-templates/cloud",
        "~/nuclei-templates/dns"
    ]

    for path in template_paths:
        name = path.split("/")[-1]
        cmd = (
            f"nuclei -l {live_hosts} "
            f"-t {path} "
            f"-severity medium,high,critical "
            f"-o scans/{name}_results.txt"
        )
        subprocess.run(cmd, shell=True)

