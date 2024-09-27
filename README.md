# Network-Scanning1

# Overview
This repository contains a Python script that utilizes the python-nmap library to perform network scans using Nmap. The script allows users to scan specified IP addresses or ranges for open ports, services, and potential vulnerabilities.

# Features
 Scans specified ports (default: 22, 80, 443).
 Detects service versions and operating systems.
 Identifies vulnerabilities using Nmap scripts.
 Outputs scan results in a clear and readable format.
    

# Prerequisites
Before running the script, ensure you have the following installed:
    1. Nmap: Required for the script to function.
    2. Python 3: The script is written in Python 3.

# Installation
Step 1: Install Nmap
  sudo apt install nmap
Step 2: Install python-nmap Library
  sudo apt install python3-nmap
Step 3: Clone the Repository
  git clone https://github.com/MrTsekar/nmap-scanner.git
cd nmap-scanner

# Usage
python nmap_scanner.py <target>

# Output
The script will output information about each host found during the scan, including:
    Host IP address and state (up/down).
    Open ports with their states and services.
    Any detected vulnerabilities
    


