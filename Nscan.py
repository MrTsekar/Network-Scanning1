import nmap
import argparse

scanner = nmap.PortScanner()

parser = argparse.ArgumentParser(description='Nmap Scanner')
parser.add_argument('target', type=str, help='IP address or range to scan (e.g., 192.168.1.0/24)')
args = parser.parse_args()

scan_options = {
    'ports': '22,80,443',
    'arguments': '-sV -sC -O -T4'
}

scan_results = scanner.scan(args.target, arguments=scan_options['arguments'], ports=scan_options['ports'])

for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")
    
    if 'tcp' in scanner[host]:
        for port in scanner[host]['tcp']:
            print(f"Port: {port}")
            print(f"State: {scanner[host]['tcp'][port]['state']}")
            print(f"Service: {scanner[host]['tcp'][port].get('name', 'N/A')}")
            print(f"Product: {scanner[host]['tcp'][port].get('product', 'N/A')}")
            print(f"Version: {scanner[host]['tcp'][port].get('version', 'N/A')}")
            print(f"CPE: {scanner[host]['tcp'][port].get('cpe', 'N/A')}")
            print("-------------------")

    if 'script' in scanner[host]:
        for script in scanner[host]['script']:
            if 'vuln' in script:
                print(f"Vulnerability: {script}")
                print(f"Output: {scanner[host]['script'][script]}")
                print("-------------------")

    print("===========================================")
