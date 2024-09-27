# Nmap Scanner
This Python script utilizes the `python-nmap` library to perform network scans on specified IP addresses or ranges. It identifies open ports and gathers detailed information about the services running on those ports, making it a useful tool for network administrators and security professionals.


## Features

- Scans specified IP addresses or CIDR ranges.
- Detects open ports (default: 22, 80, 443).
- Performs service version detection and OS detection.
- Identifies potential vulnerabilities using Nmap scripts.
- Outputs detailed information about each host and its open ports.

## Requirements

- Python 3.x
- `python-nmap` library

## Installation

1. sudo apt install nmap
   
2. sudo apt install python3-nmap

3. Clone the repository:

   git clone https://github.com/MrTsekar/nmap-scanner.git
   cd nmap-scanner

## Output

- Host IP addresses and state(Up/Down)
- Open ports with their states and services.
- Any detected vulnerabilities.

