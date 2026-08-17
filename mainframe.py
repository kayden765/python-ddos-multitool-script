#!/usr/bin/env python3
"""
================================================================================
MAINFRAME // SEC-OPERATIONS INTERACTIVE TERMINAL MULTITOOL CORE ENGINE
================================================================================
Architecture Model : Multi-Tier Nested Subsystem Shell (Directory-Driven Layout)
Privilege Layer    : Integrated Operating System Auto-Elevation (ctypes Execution)
Dependency Profile : Standalone Production Baseline (Zero Mandatory External Pip Packages)
Verification Layer : Advanced System-Wide Subprocess Path Resolution
Logging Core       : Optimized Thread-Safe Dual-Stream Intercept Logging Engine
Safety Parameters  : Compliant Threat Intelligence & Network Infrastructure Auditing Suite
================================================================================
"""

import os
import sys
import time
import random
import base64
import json
import socket
import struct
import subprocess
import shutil
import ctypes
import threading
import hashlib
import platform
import re
import math
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.error

# Initialize and synchronize virtual terminal sequences across Windows environments natively
if sys.platform.startswith('win'):
    try:
        # Enable ANSI escape processing explicitly for modern cmd/powershell sandboxes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        os.system('')

class Colors:
    """
    High-visibility ANSI console formatting control strings.
    Provides standard 16-color virtual terminal attribute configurations.
    """
    RED = '\033[91m'
    AMBER = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Absolute terminal clearance code sequence:
    # \033[2J -> Erase active viewing canvas
    # \033[3J -> Fully purge scrollback cache history buffer blocks
    # \033[H  -> Reset hardware cursor context to coordinates 0,0
    CLEAR_SCREEN = '\033[2J\033[3J\033[H'

class DualStreamWriter:
    """
    Thread-safe intercept standard stdout streams to simultaneously replicate console 
    outputs into local text documents while filtering out raw ANSI layout color arrays.
    """
    def __init__(self, original_stdout, log_file_handle):
        self.terminal = original_stdout
        self.log_file = log_file_handle
        self.ansi_regex = re.compile(r'\033\[[0-9;]*[a-zA-Z]')
        self.write_lock = threading.Lock()

    def write(self, message):
        with self.write_lock:
            # Deliver pristine colored output to the active screen terminal interface
            self.terminal.write(message)
            # Clean text by purging terminal manipulation and color escape blocks before saving to disk
            purified_message = self.ansi_regex.sub('', message)
            self.log_file.write(purified_message)
            self.log_file.flush()

    def flush(self):
        with self.write_lock:
            self.terminal.flush()
            self.log_file.flush()

class MainframeUI:
    """Handles the rendering engines for banners, text structures, and menu loops."""
    
    @staticmethod
    def draw_banner():
        """Renders the central system cybernetic telemetry node graphic."""
        skull_ascii = r"""
         ______
      .-"      "-.
     /            \
    |              |
    |,.  .-.  .-.  ,|
    | )(__/  \__)( |
    |/     /\     \|
    (_     ^^     _)
     \__|IIIIII|__/
      | \IIIIII/ |
      \          /
       `--------`"""
        print(f"{Colors.CYAN}{skull_ascii}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}" + "=" * 75)
        print("   MAINFRAME COMPREHENSIVE SECURITY RECONNAISSANCE ENGINE // MULTI-CORE")
        print("   DEPLOYMENT SPECIFICATION RELEASE v5.75 // AUDIT ENGINE: NOMINAL")
        print("=" * 75 + f"{Colors.RESET}\n")

    @staticmethod
    def display_main_menu():
        """Presents the cleaned, condensed root routing interface directories."""
        print(f"{Colors.BOLD}{Colors.GREEN}[MAIN SYSTEM DIRECTORY CORE]{Colors.RESET}\n")
        print(f"  [{Colors.AMBER}1{Colors.RESET}] Sub-Directory 01 // Network Infrastructure & Endpoint Recon Cores")
        print(f"  [{Colors.CYAN}2{Colors.RESET}] Sub-Directory 02 // External OSINT & Target Record Profilers")
        print(f"  [{Colors.GREEN}3{Colors.RESET}] Sub-Directory 03 // Local Data Traffic Monitors, Audits & Utilities")
        print(f"  [{Colors.CYAN}4{Colors.RESET}] Sub-Directory 04 // Advanced Infrastructure Audits & Integrity Cores")
        print("\n" + f"{Colors.RED}[SYSTEM SHUTDOWN CONTROL]{Colors.RESET}")
        print(f"  [{Colors.RED}5{Colors.RESET}] Terminate Active Mainframe Operator Control Session")
        print(f"\n{Colors.BOLD}{Colors.GREEN}" + "-" * 75 + f"{Colors.RESET}")

    @staticmethod
    def display_network_menu():
        """Renders options designated for low-level server analysis and network discovery."""
        print(f"{Colors.AMBER}[SUB-DIRECTORY 01 // NETWORK INFRASTRUCTURE & ENDPOINT RECON]{Colors.RESET}\n")
        print("  [1] High-Speed Rainbow Echo Pinger Latency Monitor")
        print("  [2] Reverse DNS Infrastructure Resolver (IP-to-Host PTR Check)")
        print("  [3] Multi-Threaded Target Service Port Scanner & Vulnerability Profiler")
        print("  [4] Local Subnet Parallel Ping Sweeper Matrix")
        print("  [5] Network Application Service Banner Grabber Auditor")
        print("  [6] DNS Reconnaissance Explorer Matrix (AddrInfo Lookup)")
        print("  [7] Passive Domain Subdomain Discovery Engine (via crt.sh Logs)")
        print("  [8] Advanced RDAP Registration Infrastructure Allocation Mapper")
        print("\n" + f"{Colors.CYAN}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [9] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.AMBER}" + "-" * 75 + f"{Colors.RESET}")

    @staticmethod
    def display_osint_menu():
        """Renders options designated for user handles, phone records, and data leak dumps."""
        print(f"{Colors.CYAN}[SUB-DIRECTORY 02 // EXTERNAL OSINT & TARGET PROFILE MANAGEMENT]{Colors.RESET}\n")
        print("  [1] Sherlock Username Account Tracer (Live Shell Subprocess Launch)")
        print("  [2] PhoneInfoga Telecom Target Scanner (Live Shell Subprocess Launch)")
        print("  [3] Holehe Email Platform Account Auditor (Live Shell Subprocess Launch)")
        print("  [4] Socialscan Concurrent Identity Profiler (Live Shell Subprocess Launch)")
        print("  [5] Live Online Data Breach Explorer & Password Leak Checker")
        print("  [6] Tor Exit Node Network Threat Intelligence Node Validator")
        print("\n" + f"{Colors.AMBER}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [7] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.CYAN}" + "-" * 75 + f"{Colors.RESET}")

    @staticmethod
    def display_utilities_menu():
        """Renders options designated for local machine audits, data parsers, and compliance trackers."""
        print(f"{Colors.GREEN}[SUB-DIRECTORY 03 // LOCAL DATA TRAFFIC, SECURITY AUDITS & METRICS]{Colors.RESET}\n")
        print("  [1] Inbound Network Packet Monitor Engine (Requires Admin Context)")
        print("  [2] Local Directory Source Code 'Secret & Private Key' Leak Scanner")
        print("  [3] Cryptographic Hash Signatures Matrix Generation & Token Analyzer")
        print("  [4] Advanced Local Host Operating System Telemetry Profiler")
        print("  [5] Base64 Cryptographic Processing Matrix (Data Transformation)")
        print("\n" + f"{Colors.CYAN}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [6] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.GREEN}" + "-" * 75 + f"{Colors.RESET}")

    @staticmethod
    def display_advanced_audits_menu():
        """Renders options designated for structural file integrity checks and certificate audits."""
        print(f"{Colors.CYAN}[SUB-DIRECTORY 04 // ADVANCED INFRASTRUCTURE AUDITS & INTEGRITY]{Colors.RESET}\n")
        print("  [1] Local File Integrity Monitor (FIMS Directory Snapshot Tracker)")
        print("  [2] SSL/TLS Certificate Expiration & Cipher Suite Auditor")
        print("  [3] Host Active Network Connection & Listening Port Profiler")
        print("  [4] Password Complexity & Offline Information Entropy Matrix")
        print("  [5] Local Network ARP Table Cache Profiler & Duplicate MAC Auditor")
        print("\n" + f"{Colors.CYAN}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [6] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.CYAN}" + "-" * 75 + f"{Colors.RESET}")

def find_global_command(command_name):
    """
    Systematically combs through active system path blocks, user configurations,
    and hidden global storage paths to find standalone third-party tools.
    """
    cmd_path = shutil.which(command_name)
    if cmd_path:
        return cmd_path
        
    try:
        home_dir = os.path.expanduser('~')
        pipx_bin_dir = os.path.join(home_dir, '.local', 'bin')
        fallback_path = shutil.which(command_name, path=pipx_bin_dir)
        if fallback_path:
            return fallback_path
    except Exception:
        pass

    if os.name == 'nt':
        try:
            local_appdata = os.environ.get('LOCALAPPDATA', '')
            if local_appdata:
                pipx_local_path = os.path.join(local_appdata, 'pipx', 'shared', 'bin')
                fallback_path = shutil.which(command_name, path=pipx_local_path)
                if fallback_path:
                    return fallback_path
        except Exception:
            pass

    try:
        import site
        if hasattr(site, 'getuserbase'):
            user_base = site.getuserbase()
            if user_base:
                fallback_dir = os.path.join(user_base, 'Scripts' if os.name == 'nt' else 'bin')
                fallback_path = shutil.which(command_name, path=fallback_dir)
                if fallback_path:
                    return fallback_path
    except Exception:
        pass

    try:
        bindir = os.path.dirname(sys.executable)
        fallback_path = shutil.which(command_name, path=bindir)
        if fallback_path:
            return fallback_path
        fallback_path = shutil.which(command_name, path=os.path.join(bindir, 'Scripts'))
        if fallback_path:
            return fallback_path
    except Exception:
        pass

    return command_name

# ================================================================================
# SUB-DIRECTORY 01 ENGINE ROUTINES (NETWORK CORES)
# ================================================================================

def run_pinger_engine():
    """
    Constructs real-time ICMP requests using the local system shell runtime variables.
    Includes explicit verification filters to eliminate false-positive error echo logs.
    """
    print(f"{Colors.CLEAR_SCREEN}{Colors.RED}[WARNING // NETWORK STREAM ENGINE DEPLOYED]{Colors.RESET}")
    target_host = input(f"{Colors.BOLD}Enter target IP address routing node [Default: 185.220.101.5]: {Colors.RESET}").strip()
    if not target_host:
        target_host = "185.220.101.5"
    
    print(f"\n{Colors.CYAN}Spawning native network shell utility. Tap Ctrl+C to trigger interrupt signal...{Colors.RESET}\n")
    time.sleep(1)

    is_windows = sys.platform.startswith('win')
    cmd_args = ['ping', '-n', '1', '-w', '1000', target_host] if is_windows else ['ping', '-c', '1', '-W', '1', target_host]

    colors_list = [Colors.RED, Colors.AMBER, Colors.GREEN, Colors.CYAN]
    idx = 0
    
    try:
        while True:
            start_time = time.time()
            process = subprocess.run(cmd_args, capture_output=True, text=True)
            duration_ms = int((time.time() - start_time) * 1000)
            
            chosen_color = colors_list[idx % len(colors_list)]
            out = process.stdout.lower()
            
            if process.returncode == 0 and ("ttl=" in out or "time=" in out) and "unreachable" not in out and "timed out" not in out:
                latency_str = ""
                if "time=" in out:
                    try:
                        parts = out.split("time=")[1].split()[0]
                        parts = ''.join(c for c in parts if c.isdigit() or c == '.')
                        latency_ms = float(parts)
                        latency_str = f"{latency_ms}ms"
                    except Exception:
                        latency_str = f"~{duration_ms}ms"
                else:
                    latency_str = f"~{duration_ms}ms"
                
                print(f"{chosen_color}{target_host} ➔ {latency_str} // ECHO_SUCCESS_ACK{Colors.RESET}")
            else:
                print(f"{Colors.RED}{target_host} ➔ CRITICAL // PACKET_TIMEOUT_DROP{Colors.RESET}")
            
            idx += 1
            time.sleep(0.4)
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.AMBER}[STREAM STOP SIGNAL LOGGED // CONSOLE CACHE RECOVERED]{Colors.RESET}")
        time.sleep(1.5)

def run_reverse_dns():
    """Queries active name server structures to trace IP pointer (PTR) records."""
    print(f"\n{Colors.AMBER}[MODULE 02 // REVERSE DNS INFRASTRUCTURE RESOLVER]{Colors.RESET}")
    print("Performs lookups against pointer distribution files to track host allocation layers.")
    target_ip = input("\nEnter target IP address to query: ").strip()
    if not target_ip:
        return
        
    print(f"\n{Colors.GREEN}Initiating socket gethostbyaddr handshake sequence...{Colors.RESET}")
    time.sleep(0.5)
    
    try:
        hostname, alias_list, ip_list = socket.gethostbyaddr(target_ip)
        print(f"\n{Colors.GREEN}[✓] RESOLUTION TARGET ACQUIRED // REGISTERED PTR RECORD{Colors.RESET}")
        print("-" * 75)
        print(f"  ➔ Core Assigned Hostname : {Colors.CYAN}{hostname}{Colors.RESET}")
        print(f"  ➔ Alternative Name Aliases: {alias_list}")
        print(f"  ➔ Interface Bindings Array: {ip_list}")
    except socket.herror:
        print(f"\n{Colors.RED}[!] Host Resolution Miss: No valid reverse name pointers exist for this location.{Colors.RESET}")
    except Exception as err:
        print(f"\n{Colors.RED}[!] Network Mapping Exception Logged: {err}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nModule matrix complete. Press Enter to pull up directory layout...")

def run_port_scanner():
    """Launches rapid asynchronous connections across ports and profiles vulnerabilities/hardening vectors."""
    print(f"\n{Colors.AMBER}[MODULE 03 // MULTI-THREADED PORT SCANNER & VULNERABILITY PROFILER]{Colors.RESET}")
    target = input("Enter target domain identifier or IP node: ").strip()
    if not target:
        return
        
    print(f"\n{Colors.GREEN}Resolving lookup records against root nameservers...{Colors.RESET}")
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Target Identity Bound: {Colors.CYAN}{target_ip}{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}[!] Failed to resolve server destination mapping: {e}{Colors.RESET}")
        input("\nPress Enter to return...")
        return

    # Configuration database mapping common services to audit/defense context parameters
    port_hardening_db = {
        21: ("FTP", "Plaintext authentication credentials. Audit for anonymous logins or transition to SFTP/FTPS."),
        22: ("SSH", "Secure Shell interface. Verify key-based authentication is enforced and root login is deactivated."),
        23: ("Telnet", "Highly insecure plaintext stream. Immediate deprecation recommended; transition to SSH."),
        25: ("SMTP", "Mail relay protocol. Ensure server is not operating as an open relay to prevent exploitation."),
        53: ("DNS", "Domain Name System. Audit against zone transfer exposures (AXFR) and amplification risks."),
        80: ("HTTP", "Unencrypted web platform. Enforce absolute TLS encryption redirects over port 443."),
        110: ("POP3", "Post Office Protocol. Plaintext credential exchange. Transition immediately to POP3S."),
        135: ("RPC Endpoint", "Microsoft RPC Endpoint Mapper. Often probed for environment footprinting. Restrict exposure."),
        139: ("NetBIOS", "NetBIOS Session Service. Legacy networking transport protocol. Restrict access at gateway boundary."),
        443: ("HTTPS", "Secure Web Socket. Verify modern cryptographic cipher baseline suites (TLS 1.2 / TLS 1.3) are mandatory."),
        445: ("SMB", "Microsoft Directory Sharing. Ensure message signing is required to mitigate relay threats."),
        1433: ("MSSQL", "Microsoft SQL Database engine server interface. Isolate from public ingress routes."),
        3306: ("MySQL", "Open-source SQL engine infrastructure node access point. Restrict to internal localhost paths."),
        3389: ("RDP", "Remote Desktop Gateway. Enforce Network Level Authentication (NLA) and route inside a defensive VPN."),
        8080: ("HTTP-Alt", "Alternative web application runtime proxy port. Review background system dependencies for patches."),
        8443: ("HTTPS-Alt", "Alternative secure server administration access dashboard. Restrict via strict ACL configurations.")
    }

    print(f"{Colors.BOLD}{'INTERFACE':<12}{'SERVICE':<16}{'STATUS':<12}{'DEFENSIVE PROFILING ARCHIVE'}{Colors.RESET}")
    print("-" * 110)

    # Thread-safe print coordinator lock
    print_lock = threading.Lock()

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.2)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                service_meta = port_hardening_db.get(port, ("unknown", "No supplementary baseline audit records compiled."))
                with print_lock:
                    print(f"{Colors.GREEN}Port {port:<8}{service_meta[0]:<16}{'OPEN':<12}{Colors.RESET}{Colors.AMBER}{service_meta[1]}{Colors.RESET}")
            s.close()
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(scan_port, sorted(port_hardening_db.keys()))

    print("-" * 110)
    input(f"\nScan operations sequence terminated. Press Enter to resume...")

def run_ping_sweeper():
    """Dispatches low-overhead echo sweeps to establish network mapping vectors."""
    print(f"\n{Colors.AMBER}[MODULE 04 // LOCAL SUBNET PARALLEL PING SWEEPER]{Colors.RESET}")
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        parts = local_ip.split('.')
        default_subnet = ".".join(parts[:3]) if len(parts) == 4 else "192.168.1"
    except Exception:
        default_subnet = "192.168.1"

    subnet = input(f"Enter target local subnet prefix [Default: {default_subnet}]: ").strip() or default_subnet
    print(f"\n{Colors.CYAN}Spawning thread pools for network matrix {subnet}.1 to {subnet}.254...{Colors.RESET}\n")
    
    is_windows = sys.platform.startswith('win')
    cmd_base = ['ping', '-n', '1', '-w', '400'] if is_windows else ['ping', '-c', '1', '-W', '1']

    print(f"{Colors.BOLD}{'LOCAL IP NODE':<22}{'RESPONSE METRIC'}{Colors.RESET}")
    print("-" * 45)

    def check_host(i):
        ip = f"{subnet}.{i}"
        try:
            res = subprocess.run(cmd_base + [ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if res.returncode == 0:
                print(f"{Colors.GREEN}{ip:<22}[ RESPONSIVE DEVICE ONLINE ]{Colors.RESET}")
        except Exception:
            pass

    try:
        with ThreadPoolExecutor(max_workers=35) as executor:
            executor.map(check_host, range(1, 255))
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Subnet sweep thread process broken by console operator command.{Colors.RESET}")

    print("-" * 45)
    input(f"\nSweep operation complete. Press Enter to exit subsystem layer...")

def run_banner_grabber():
    """Intercepts server banner configurations by establishing direct TCP connections."""
    print(f"\n{Colors.AMBER}[MODULE 05 // NETWORK SERVICE BANNER GRABBER AUDITOR]{Colors.RESET}")
    target = input("Enter target server domain or address block: ").strip()
    if not target:
        return
    port_input = input("Enter operational application port (e.g., 21, 22, 80): ").strip()
    try:
        port = int(port_input)
    except ValueError:
        print(f"{Colors.RED}[!] Format Check Exception: Target port must be a numerical value.{Colors.RESET}")
        time.sleep(1.2)
        return

    print(f"\n{Colors.GREEN}Deploying stream socket descriptor to {target}:{port}...{Colors.RESET}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.5)
        s.connect((target, port))
        
        if port in [80, 8080]:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            
        banner = s.recv(1024)
        s.close()
        
        print(f"\n{Colors.GREEN}[✓] REMOTE DATA CAPTURED // SOFTWARE RECORD ANCHOR{Colors.RESET}\n")
        print("-" * 75)
        print(banner.decode('utf-8', errors='ignore').strip())
    except Exception as e:
        print(f"\n{Colors.RED}[!] Pipeline Dropped: Stream handshake interface rejected: {e}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nPress Enter to return to menu directory structure...")

def run_dns_recon():
    """Extracts fundamental domain host structural assignments from the native address profile lists."""
    print(f"\n{Colors.AMBER}[MODULE 06 // DNS RECONNAISSANCE EXPLORER MATRIX]{Colors.RESET}")
    target = input("Enter target domain network path (e.g., system.com): ").strip()
    if not target:
        return

    print(f"\n{Colors.GREEN}Calling native socket infrastructure interfaces...{Colors.RESET}")
    try:
        addr_info = socket.getaddrinfo(target, None)
        resolved_records = set()
        for node in addr_info:
            resolved_records.add(node[4][0])
            
        print(f"\n{Colors.GREEN}[✓] NAME SCAN RESOLUTION INDEX{Colors.RESET}")
        print("-" * 75)
        print(f"  Target Domain Target: {target}")
        for ip in resolved_records:
            print(f"  ➔ Active Route Mapped Endpoint: {Colors.CYAN}{ip}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Namespace Resolution Trace Failed: {e}{Colors.RESET}")

    print("-" * 75)
    input(f"\nModule run finalized. Press Enter to drop back to choices...")

def run_subdomain_finder():
    """Crawls crt.sh passively to isolate exposed subdomains without generating target alerts."""
    print(f"\n{Colors.AMBER}[MODULE 07 // PASSIVE DOMAIN SUBDOMAIN FINDER]{Colors.RESET}")
    print("Queries distributed certificate transparency indices to pinpoint network allocations.")
    target_root = input("\nEnter target parent root domain (e.g., corporate.com): ").strip()
    if not target_root:
        return
        
    print(f"\n{Colors.GREEN}Opening stream to transparency certificate logs database endpoint...{Colors.RESET}")
    url = f"https://crt.sh.{target_root}&output=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status == 200:
                raw_json = response.read().decode('utf-8')
                data = json.loads(raw_json)
                isolated_subs = set()
                
                for item in data:
                    name_value = item.get('name_value', '')
                    for split_node in name_value.split('\n'):
                        split_node = split_node.strip().lower()
                        if split_node.endswith(target_root) and "*" not in split_node:
                            isolated_subs.add(split_node)
                            
                print(f"\n{Colors.GREEN}[✓] PASSIVE DISCOVERY RECON LOG INDEX ({len(isolated_subs)} ENTRIES TRACKED){Colors.RESET}")
                print("-" * 75)
                for subdomain in sorted(isolated_subs):
                    print(f"  ➔ Verified Subdomain Host: {Colors.CYAN}{subdomain}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Server Connection Error: Server dropped protocol flag HTTP {response.status}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] External Index Disconnected: Registry logs unreadable or stream timeout: {e}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to drop layout cache...")

def run_rdap_lookup():
    """Maps autonomous network ranges and registrar details using the global RDAP architecture."""
    print(f"\n{Colors.AMBER}[MODULE 08 // ADVANCED RDAP REGISTRATION INFRASTRUCTURE MAPPER]{Colors.RESET}")
    target_input = input("Enter target system IP address or domain path: ").strip()
    if not target_input:
        return
        
    is_raw_ip = True
    try:
        socket.inet_aton(target_input)
    except Exception:
        is_raw_ip = False
        
    if not is_raw_ip:
        print(f"{Colors.GREEN}Resolving domain target to network routing address...{Colors.RESET}")
        try:
            lookup_ip = socket.gethostbyname(target_input)
            print(f"Domain mapped to routing coordinate: {Colors.CYAN}{lookup_ip}{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error tracking domain mapping: {e}. Attempting direct query format...{Colors.RESET}")
            lookup_ip = target_input
    else:
        lookup_ip = target_input

    print(f"\n{Colors.GREEN}Sending configuration request packet array to RDAP name registries...{Colors.RESET}")
    url = f"https://rdap.org{lookup_ip}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mainframe-Terminal-Multitool'})
    
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            raw_data = response.read().decode('utf-8')
            parsed_records = json.loads(raw_data)
            
            print(f"\n{Colors.GREEN}[✓] PRODUCTION INFRASTRUCTURE METRIC DATA BLOCKS{Colors.RESET}")
            print("-" * 75)
            print(f"  ➔ Primary Entity Identifier : {Colors.CYAN}{parsed_records.get('name', 'UNREGISTERED')}{Colors.RESET}")
            print(f"  ➔ Assigned Allocation Block : {parsed_records.get('startAddress', 'N/A')} - {parsed_records.get('endAddress', 'N/A')}")
            print(f"  ➔ Registered Country Code   : {parsed_records.get('country', 'UNKNOWN')}")
            
            entities = parsed_records.get('entities', [])
            if entities:
                vcard = entities[0].get('vcardArray', [])
                if len(vcard) > 1:
                    for element in vcard[1]:
                        if element[0] == 'fn':
                            print(f"  ➔ Administrative Provider  : {Colors.AMBER}{element[3]}{Colors.RESET}")
    except Exception as err:
        print(f"\n{Colors.RED}[!] Registry Allocation Block Record Missing or Timeout: {err}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nModule pipeline sequence finished. Press Enter to navigate back to choices...")

# ================================================================================
# SUB-DIRECTORY 02 ENGINE ROUTINES (EXTERNAL OSINT CORES)
# ================================================================================

def run_sherlock_hook():
    """Invokes globally configured Sherlock profiles via system execution scripts."""
    print(f"\n{Colors.CYAN}[MODULE 01 // LIVE SYSTEM LAUNCH: SHERLOCK USERNAME TRACER]{Colors.RESET}")
    print("Prerequisite Validation: System context maps global 'sherlock' configuration binaries.")
    
    target_handle = input("\nEnter target identity alias to audit: ").strip()
    if not target_handle:
        return
        
    print(f"\n{Colors.GREEN}Spawning live shell execution sandbox subprocess environment...{Colors.RESET}")
    executable_target = find_global_command('sherlock')
    print(f"Running context: {executable_target} {target_handle} --timeout 5\n")
    print("-" * 75)
    
    try:
        subprocess.run([executable_target, target_handle, '--timeout', '5'], capture_output=False, text=True)
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Environment Path Exception: System variables cannot locate the executable command.{Colors.RESET}")
        print("Resolve this by configuring your shell or executing: pipx install sherlock-project")
        
    print("-" * 75)
    input(f"\nSubprocess returned exit context code. Press Enter to open submenu...")

def run_phoneinfoga_hook():
    """Invokes compiled PhoneInfoga infrastructure components via binary execution modules."""
    print(f"\n{Colors.CYAN}[MODULE 02 // LIVE SYSTEM LAUNCH: PHONEINFOGA TELECOM SCANNER]{Colors.RESET}")
    print("Prerequisite Validation: Global environment path definitions contain the 'phoneinfoga' script.")
    
    target_number = input("\nEnter target layout telephone with country flag code (e.g., +14155552671): ").strip()
    if not target_number:
        return
        
    print(f"\n{Colors.GREEN}Spawning live shell execution sandbox subprocess environment...{Colors.RESET}")
    executable_target = find_global_command('phoneinfoga')
    print(f"Running context: {executable_target} scan -n {target_number}\n")
    print("-" * 75)
    
    try:
        subprocess.run([executable_target, 'scan', '-n', target_number], capture_output=False, text=True)
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Environment Path Exception: Local machine environment cannot see binary configuration nodes.{Colors.RESET}")
        print("Verify your workspace subfolder assets or ensure the program path is added to your environment rules.")
        
    print("-" * 75)
    input(f"\nSubprocess returned exit context code. Press Enter to open submenu...")

def run_holehe_hook():
    """Invokes Holehe registration trace components via native package trackers."""
    print(f"\n{Colors.CYAN}[MODULE 03 // LIVE SYSTEM LAUNCH: HOLEHE EMAIL PLATFORM AUDITOR]{Colors.RESET}")
    print("Prerequisite Validation: Python workspace registers global package 'holehe' configurations.")
    
    target_mail = input("\nEnter target email address profile to trace: ").strip()
    if not target_mail or "@" not in target_mail:
        print(f"{Colors.RED}[!] Input Format Validation Error: Invalid structure format tracking input.{Colors.RESET}")
        time.sleep(1)
        return
        
    print(f"\n{Colors.GREEN}Spawning live shell execution sandbox subprocess environment...{Colors.RESET}")
    executable_target = find_global_command('holehe')
    print(f"Running context: {executable_target} {target_mail}\n")
    print("-" * 75)
    
    try:
        subprocess.run([executable_target, target_mail], capture_output=False, text=True)
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Environment Path Exception: Execution link dropped due to missing package file structures.{Colors.RESET}")
        print("Deploy capabilities to your local python setup via terminal step: pip install holehe")
        
    print("-" * 75)
    input(f"\nSubprocess returned exit context code. Press Enter to open submenu...")

def run_socialscan_hook():
    """Invokes Socialscan concurrent matrix queries via platform command modules."""
    print(f"\n{Colors.CYAN}[MODULE 04 // LIVE SYSTEM LAUNCH: SOCIALSCAN CONCURRENT IDENTITY PROFILER]{Colors.RESET}")
    print("Prerequisite Validation: Python workspace registers deployment package 'socialscan' installations.")
    
    target_string = input("\nEnter target credential handle or mail index to cross-reference: ").strip()
    if not target_string:
        return
        
    print(f"\n{Colors.GREEN}Spawning live shell execution sandbox subprocess environment...{Colors.RESET}")
    executable_target = find_global_command('socialscan')
    print(f"Running context: {executable_target} {target_string}\n")
    print("-" * 75)
    
    try:
        subprocess.run([executable_target, target_string], capture_output=False, text=True)
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Environment Path Exception: Script link trace dropped due to unprovisioned package headers.{Colors.RESET}")
        print("Provision this workspace framework layer by executing command step: pip install socialscan")
        
    print("-" * 75)
    input(f"\nSubprocess returned exit context code. Press Enter to open submenu...")

def run_live_breach_checker():
    """
    Queries open-source API telemetry registries to audit exposures.
    Leverages unauthenticated range hashes to flag leaked credentials safely.
    """
    print(f"\n{Colors.CYAN}[MODULE 05 // LIVE ONLINE DATA BREACH EXPLORER & PASSWORD CHECKER]{Colors.RESET}")
    print(" [1] Audit Email Identifier Exposure (XposedOrNot Public API)")
    print(" [2] Audit Password Exposure Anonymously (HaveIBeenPwned Range API)")
    mode = input("Select inspection target mode (1/2): ").strip()
    
    if mode == "1":
        target_email = input("\nEnter target email address to audit: ").strip()
        if not target_email or "@" not in target_email:
            print(f"{Colors.RED}[!] Format Error: Invalid email structure.{Colors.RESET}")
            time.sleep(1.2)
            return
        print(f"\n{Colors.GREEN}Querying XposedOrNot live database registry...{Colors.RESET}")
        url = f"https://xposedornot.com{target_email}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mainframe-Terminal-Multitool'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    raw_json = response.read().decode('utf-8')
                    parsed_data = json.loads(raw_json)
                    print(f"\n{Colors.RED}[!] EXPOSURE FOUND INSIDE INDEXED DATA LEAKS{Colors.RESET}")
                    print("-" * 75)
                    if isinstance(parsed_data, dict) and "breaches_details" in parsed_data:
                        details = parsed_data.get("breaches_details", {})
                        for breach_name in details:
                            print(f"  ➔ Exposed Source: {Colors.AMBER}{breach_name}{Colors.RESET}")
                    else:
                        print("  ➔ Record tracked inside independent credential dumps or paste files.")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print(f"\n{Colors.GREEN}[✓] STATUS SECURE: No data data breaches discovered for this email.{Colors.RESET}")
            else:
                print(f"\n{Colors.RED}[!] API query dropped: HTTP status code {err.code}{Colors.RESET}")
        except Exception as e:
            print(f"\n{Colors.RED}[!] Connection pipeline error: {e}{Colors.RESET}")
            
    elif mode == "2":
        target_password = input("\nEnter target plaintext password to audit: ").strip()
        if not target_password:
            return
        print(f"\n{Colors.GREEN}Hashing locally and generating k-anonymity anonymous range request...{Colors.RESET}")
        sha1_hash = hashlib.sha1(target_password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        url = f"https://pwnedpasswords.com{prefix}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mainframe-Terminal-Multitool'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                lines = response.read().decode('utf-8').splitlines()
                match_count = 0
                for line in lines:
                    if ":" in line:
                        hash_suffix, count_str = line.split(":")
                        if hash_suffix == suffix:
                            match_count = int(count_str)
                            break
                print(f"\n{Colors.BOLD}PWNED PASSWORDS AUDIT REPORT:{Colors.RESET}")
                print("-" * 75)
                if match_count > 0:
                    print(f"  Analysis Verdict: {Colors.RED}[!!!] LEAKED STRONGLY EXPOSED{Colors.RESET}")
                    print(f"  Prevalence Count: This exact password string was found {Colors.RED}{match_count}{Colors.RESET} times inside data breaches.")
                    print("  Security Warning: Do not utilize this credential for active online profiles.")
                else:
                    print(f"  Analysis Verdict: {Colors.GREEN}[✓] STATUS SECURE // NO KNOWN LEAKS{Colors.RESET}")
                    print("  Prevalence Count: Zero compromised occurrences indexed.")
        except Exception as e:
            print(f"\n{Colors.RED}[!] Failed to update Pwned Passwords threat feed: {e}{Colors.RESET}")
            
    else:
        print(f"{Colors.RED}[!] Invalid choice selected.{Colors.RESET}")
        
    print("-" * 75)
    print(f"\n{Colors.AMBER}Note on Name Queries:{Colors.RESET} Real names are omitted because public breach tracking platforms")
    print("index leaks strictly by unique identifiers (email/username) to ensure privacy and accuracy.")
    input(f"\nPress Enter to return to sub-directory menus...")

def run_threat_intel():
    """Downloads public Tor directory indices to check if an address maps to an exit node."""
    print(f"\n{Colors.CYAN}[MODULE 06 // TOR EXIT NODE THREAT INTELLIGENCE NODE VALIDATOR]{Colors.RESET}")
    print("Audits network addresses against real-time Tor project exit allocation manifests.")
    target_ip = input("\nEnter target IP address to check: ").strip()
    if not target_ip:
        return
        
    print(f"\n{Colors.GREEN}Configuring safe connection stream to torproject.org public network nodes...{Colors.RESET}")
    url = "https://torproject.org"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        with urllib.request.urlopen(req, timeout=12) as network_stream:
            raw_text = network_stream.read().decode('utf-8')
            allocated_exit_nodes = set()
            
            for text_row in raw_text.split('\n'):
                if text_row.startswith("ExitAddress"):
                    row_elements = text_row.split()
                    if len(row_elements) > 1:
                        allocated_exit_nodes.add(row_elements[1])
                        
            print(f"\n{Colors.GREEN}[✓] VERIFIED THREAT FEED SYNCHRONIZED{Colors.RESET}")
            print("-" * 70)
            if target_ip in allocated_exit_nodes:
                print(f"Target Track IP Address: {target_ip}")
                print(f"Threat Analysis Verdict: {Colors.RED}[!!!] THREAT DETECTED // CONFIRMED TOR EXIT LAYER GATEWAY{Colors.RESET}")
                print("Context Mapping Profile: Host address matches anonymous network data relay segments.")
            else:
                print(f"Target Track IP Address: {target_ip}")
                print(f"Threat Analysis Verdict: {Colors.GREEN}[✓] MONITOR RECORD STABLE // DIRECT ROUTE TRAFFIC{Colors.RESET}")
                print("Context Mapping Profile: Network location is absent from indexed public relay lists.")
    except Exception as ex:
        print(f"\n{Colors.RED}[!] Failed to capture streaming telemetry metrics from threat source: {ex}{Colors.RESET}")
        
    print("-" * 70)
    input(f"\nModule processing terminated. Press Enter to draw sub-directory menus...")

# ================================================================================
# SUB-DIRECTORY 03 ENGINE ROUTINES (LOCAL AUDITS & UTILITIES)
# ================================================================================

def run_traffic_monitor():
    """Taps directly into the machine's local socket layers using raw packet capturing flags."""
    print(f"\n{Colors.GREEN}[MODULE 01 // INBOUND NETWORK PACKET MONITOR ENGINE]{Colors.RESET}")
    print("Decodes real-time inbound packet metrics hitting your network interface adapter cards.")
    print(f"{Colors.RED}[ADMIN RISK WARNING] Raw socket intercept requires Administrator / Root rights context.{Colors.RESET}\n")
    
    if input("Initialize network socket mirroring operations pipeline? (Y/N): ").strip().upper() != 'Y':
        return

    async_dns_register = {}
    cache_lock = threading.Lock()

    def resolve_ip_async(ip_address):
        def worker_task():
            try:
                resolved_hostname, _, _ = socket.gethostbyaddr(ip_address)
                with cache_lock:
                    async_dns_register[ip_address] = resolved_hostname
            except Exception:
                with cache_lock:
                    if ip_address.startswith("192.168.") or ip_address.startswith("10.") or ip_address.startswith("172."):
                        async_dns_register[ip_address] = "Internal LAN Gateway Address"
                    elif ip_address == "127.0.0.1":
                        async_dns_register[ip_address] = "Localhost Software Loopback"
                    else:
                        async_dns_register[ip_address] = "Direct Routing Node Provider"
                        
        with cache_lock:
            if ip_address not in async_dns_register:
                async_dns_register[ip_address] = "Tracking Domain Node..."
                threading.Thread(target=worker_task, daemon=True).start()

    try:
        if os.name == "nt":
            sys_host = socket.gethostname()
            adapter_ip = socket.gethostbyname(sys_host)
            print(f"\n{Colors.GREEN}Binding raw IP network sockets pipeline to interface: {adapter_ip}{Colors.RESET}")
            
            sniffer_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
            sniffer_socket.bind((adapter_ip, 0))
            sniffer_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            sniffer_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        else:
            print(f"\n{Colors.GREEN}Binding generic raw socket interface frame trackers to Unix descriptors...{Colors.RESET}")
            sniffer_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            
    except PermissionError:
        print(f"\n{Colors.RED}[!] Privilege Level Error: Active context has insufficient access rights.{Colors.RESET}")
        print("Rectify this by right-clicking your terminal and choosing 'Run as Administrator'.")
        input(f"\nPress Enter to break execution tracking...")
        return
    except Exception as socket_err:
        print(f"\n{Colors.RED}[!] Hardware Link dropped: Socket failure: {socket_err}{Colors.RESET}")
        input(f"\nPress Enter to break execution tracking...")
        return

    print(f"\n{Colors.CYAN}Capture Matrix online. Streaming raw traffic frames. Tap Ctrl+C to drop link...{Colors.RESET}\n")
    print(f"{Colors.BOLD}{'PROTOCOL':<12}{'SOURCE IP':<18}{'RESOLVED IDENTITY / PROV FLAG':<38}{'BUFFER LENGTH'}{Colors.RESET}")
    print("-" * 80)

    try:
        while True:
            raw_packet_bytes = sniffer_socket.recvfrom(65535)[0]
            ipv4_header_bytes = raw_packet_bytes[0:20]
            unpacked_header = struct.unpack('!BBHHHBBH4s4s', ipv4_header_bytes)
            
            protocol_flag = unpacked_header[6]
            source_address_string = socket.inet_ntoa(unpacked_header[8])
            packet_total_length = len(raw_packet_bytes)

            with cache_lock:
                identity_mapping = async_dns_register.get(source_address_string, None)

            if identity_mapping is None:
                resolve_ip_async(source_address_string)
                identity_mapping = "Resolving..."

            if len(identity_mapping) > 35:
                identity_mapping = identity_mapping[:32] + "..."

            if protocol_flag == 6:
                protocol_label, row_color = "TCP_STREAM", Colors.CYAN
            elif protocol_flag == 17:
                protocol_label, row_color = "UDP_DATAGRAM", Colors.AMBER
            elif protocol_flag == 1:
                protocol_label, row_color = "ICMP_ECHO", Colors.GREEN
            else:
                protocol_label, row_color = f"IP_PROTO-{protocol_flag}", Colors.RESET

            print(f"{row_color}{protocol_label:<12}{source_address_string:<18}{identity_mapping:<38}{packet_total_length} Bytes{Colors.RESET}")
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.AMBER}[CAPTURE DRIVER PAUSED // CLOSING SOCKET HOOK REGISTRIES]{Colors.RESET}")
        if os.name == "nt":
            try:
                sniffer_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            except Exception:
                pass
        input(f"\nNetwork data buffer cleared. Press Enter to load utilities deck...")

def run_secret_scanner():
    """Scans local project source files using regex patterns to catch hardcoded api tokens."""
    print(f"\n{Colors.GREEN}[MODULE 02 // LOCAL DIRECTORY 'SECRET & KEY' LEAK SCANNER]{Colors.RESET}")
    print("Scans files recursively using exact cryptographic signature validation maps.")
    target_path = input("\nEnter folder directory path path to scan [Default = current folder '.']: ").strip() or "."
    
    if not os.path.exists(target_path):
        print(f"{Colors.RED}[!] Input Target Exception: Path directory mapping unresolvable.{Colors.RESET}")
        time.sleep(1.2)
        return

    print(f"\n{Colors.GREEN}Analyzing source data text streams. Filtering compiled binary blocks...{Colors.RESET}\n")
    regex_signature_dictionary = {
        "Google Cloud Access API Key": re.compile(r'AIza[0-9A-Za-z-_]{35}'),
        "Generic Assignment Security Hash": re.compile(r'(?i)(api_key|secret_key|password|private_key)\s*[:=]\s*["\'][0-9a-zA-Z-_]{16,64}["\']'),
        "Private Cryptographic Key Header": re.compile(r'-----BEGIN (RSA|EC|DSA|OPENSSH)? PRIVATE KEY-----'),
        "AWS Cloud Identity Allocation Token Structure": re.compile(r'AKIA[0-9A-Z]{16}')
    }

    discovered_leaks_counter = 0
    ignored_file_extensions = ('.exe', '.dll', '.png', '.jpg', '.jpeg', '.gif', '.zip', '.tar', '.gz', '.pdf', '.mp4', '.pyc')
    ignored_directory_trees = ('.git', '__pycache__', 'venv', '.local', 'node_modules')

    for root, directories, filenames in os.walk(target_path):
        directories[:] = [d for d in directories if d not in ignored_directory_trees]
        for filename in filenames:
            if filename.endswith(ignored_file_extensions):
                continue
            absolute_file_path = os.path.join(root, filename)
            try:
                with open(absolute_file_path, 'r', encoding='utf-8', errors='ignore') as file_reader:
                    for sequence_line_num, cleartext_row in enumerate(file_reader, 1):
                        for signature_label, validation_regex in regex_signature_dictionary.items():
                            regex_match = validation_regex.search(cleartext_row)
                            if regex_match:
                                discovered_leaks_counter += 1
                                captured_raw_string = regex_match.group(0)
                                obfuscated_value = captured_raw_string[:8] + "..." + captured_raw_string[-4:] if len(captured_raw_string) > 12 else "********"
                                print(f"{Colors.RED}[ RISK LEAK DETECTED ]{Colors.RESET} File: {filename} | Line: {sequence_line_num} | Flag: {signature_label} -> {Colors.AMBER}{obfuscated_value}{Colors.RESET}")
            except Exception:
                pass

    print("\n" + "-" * 70)
    print(f"Directory audit finalized. Total exposed storage indicators flagged: {Colors.RED}{discovered_leaks_counter}{Colors.RESET}")
    input(f"\nPress Enter to reset terminal menu systems interface...")

def run_hash_matrix():
    """Generates localized cryptographic hashes or determines algorithm types based on bit lengths."""
    print(f"\n{Colors.GREEN}[MODULE 03 // CRYPTOGRAPHIC HASH SIGNATURE GENERATOR & ANALYZER]{Colors.RESET}")
    print(" [1] Process Text String into Cryptographic Signatures (Checksums)")
    print(" [2] Profile Unknown Hash Formats using Bit-Length Constraints")
    menu_choice = input("Select operation mode target (1/2): ").strip()

    if menu_choice == "1":
        plaintext_input_bytes = input("\nEnter text string to convert: ").encode('utf-8')
        print(f"\n{Colors.BOLD}COMPUTED HASH METRICS:{Colors.RESET}")
        print(f"  MD5 Checksum Payload    : {Colors.CYAN}{hashlib.md5(plaintext_input_bytes).hexdigest()}{Colors.RESET}")
        print(f"  SHA-1 Signature Payload : {Colors.AMBER}{hashlib.sha1(plaintext_input_bytes).hexdigest()}{Colors.RESET}")
        print(f"  SHA-256 Core Checksum   : {Colors.GREEN}{hashlib.sha256(plaintext_input_bytes).hexdigest()}{Colors.RESET}")
    elif menu_choice == "2":
        raw_signature_hash = input("\nEnter unknown hash signature string to verify: ").strip().lower()
        purified_hash_string = "".join(char for char in raw_signature_hash if char.isalnum())
        character_length_metric = len(purified_hash_string)
        
        print(f"\n{Colors.BOLD}TELEMETRY STRUCTURE ANALYSIS REPORT:{Colors.RESET}")
        print(f"  Captured Character Bit-Length: {character_length_metric}")
        
        if character_length_metric == 32:
            print(f"  Isolated Target Type Matrix  : {Colors.CYAN}MD5 Message Digest (128-bit Signature){Colors.RESET}")
        elif character_length_metric == 40:
            print(f"  Isolated Target Type Matrix  : {Colors.AMBER}SHA-1 Secure Algorithm (160-bit Signature){Colors.RESET}")
        elif character_length_metric == 64:
            print(f"  Isolated Target Type Matrix  : {Colors.GREEN}SHA-256 Standard Structure (256-bit Signature){Colors.RESET}")
        else:
            print(f"  Isolated Target Type Matrix  : {Colors.RED}Custom, Compressed, or Multi-Layered Format Hash{Colors.RESET}")
    else:
        print(f"{Colors.RED}[!] Operations Flag Error: Provided variable context is unresolvable.{Colors.RESET}")
        
    print("-" * 70)
    input(f"\nPress Enter to reload menu directory layers...")

def run_system_profiler():
    """Gathers machine hardware data and environment tracking information natively."""
    print(f"\n{Colors.GREEN}[MODULE 04 // ADVANCED HOST SYSTEM TELEMETRY PROFILER]{Colors.RESET}")
    print("Extracting environment tracking attributes and kernel parameters...\n")
    time.sleep(0.5)

    print(f"{Colors.BOLD}OS CORE METRICS:{Colors.RESET}")
    print(f"  Primary OS Layer Name : {platform.system()}")
    print(f"  Release Build Model   : {platform.release()}")
    print(f"  Kernel Version Build  : {platform.version()}")
    print(f"  Platform Architecture : {platform.machine()}")
    print(f"  Processor Core Asset  : {platform.processor()}")
    
    print(f"\n{Colors.BOLD}NETWORK INTERFACE HARDWARE PROFILE:{Colors.RESET}")
    try:
        network_host_identifier = socket.gethostname()
        primary_interface_ip = socket.gethostbyname(network_host_identifier)
        print(f"  Console Hostname Tag : {network_host_identifier}")
        print(f"  Primary Interface IP : {primary_interface_ip}")
    except Exception as telemetry_error:
        print(f"  Failed to capture hardware device descriptors: {telemetry_error}")

    print("-" * 70)
    input(f"\nTelemetry collection phase finished. Press Enter to load submenu options...")

def run_base64_matrix():
    """Processes plaintext variables natively into standardized Base64 output arrays."""
    print(f"\n{Colors.GREEN}[MODULE 05 // BASE64 DATA PARSING & CODEC MATRIX]{Colors.RESET}")
    print(" [E] Encode Cleartext Variables into Standard Base64 String Format")
    print(" [D] Decode Base64 Obfuscated Format Arrays into Cleartext Strings")
    operational_flag = input("Select processing configuration flag (E/D): ").strip().upper()
    
    if operational_flag == 'E':
        cleartext_string_input = input("\nEnter raw text data string to transform: ")
        converted_base64_bytes = base64.b64encode(cleartext_string_input.encode('utf-8'))
        print(f"\n{Colors.GREEN}Transformation Complete Payload String:{Colors.RESET}")
        print(f"{Colors.BOLD}{converted_base64_bytes.decode('utf-8')}{Colors.RESET}")
    elif operational_flag == 'D':
        obfuscated_base64_input = input("\nEnter base64 formatted code array string to translate: ")
        try:
            translated_cleartext_bytes = base64.b64decode(obfuscated_base64_input.encode('utf-8'))
            print(f"\n{Colors.GREEN}De-obfuscated Restored Cleartext Data String:{Colors.RESET}")
            print(f"{Colors.BOLD}{translated_cleartext_bytes.decode('utf-8')}{Colors.RESET}")
        except Exception as payload_error:
            print(f"\n{Colors.RED}[!] Formatting Failure: Sequence is not a standard Base64 structure: {payload_error}{Colors.RESET}")
    else:
        print(f"{Colors.RED}[!] Operations Flag Error: Provided variable context is unresolvable.{Colors.RESET}")
        
    print("-" * 70)
    input(f"\nPress Enter to reset active console workspace...")

# ================================================================================
# SUB-DIRECTORY 04 ENGINE ROUTINES (INTEGRITY & CORE COMPLIANCE SCANS)
# ================================================================================

def run_file_integrity_monitor():
    """Tracks filesystem state drift over time by capturing localized baseline hash registries."""
    print(f"\n{Colors.GREEN}[MODULE 01 // LOCAL FILE INTEGRITY MONITOR (FIMS)]{Colors.RESET}")
    print("Audits folder nodes recursively using SHA-256 blocks to map runtime file drift.")
    target_dir = input("\nEnter target folder directory path to snapshot [Default = '.']: ").strip() or "."
    
    if not os.path.exists(target_dir):
        print(f"{Colors.RED}[!] Error: Target filesystem path unresolvable.{Colors.RESET}")
        time.sleep(1.2)
        return
        
    manifest_file = "fims_manifest.json"
    current_hashes = {}
    
    print(f"\n{Colors.GREEN}Hashing directory structures concurrently...{Colors.RESET}")
    for root, _, filenames in os.walk(target_dir):
        for filename in filenames:
            absolute_path = os.path.join(root, filename)
            try:
                sha_hasher = hashlib.sha256()
                with open(absolute_path, 'rb') as f:
                    for buffer_chunk in iter(lambda: f.read(4096), b''):
                        sha_hasher.update(buffer_chunk)
                current_hashes[absolute_path] = sha_hasher.hexdigest()
            except Exception:
                pass
                
    if not os.path.exists(manifest_file):
        try:
            with open(manifest_file, 'w', encoding='utf-8') as f:
                json.dump(current_hashes, f, indent=4)
            print(f"\n{Colors.GREEN}[✓] BASELINE DATABASE COMPILED ({len(current_hashes)} FILES INDEXED){Colors.RESET}")
            print(f"Snapshot registry configuration successfully committed to local file: {manifest_file}")
        except Exception as err:
            print(f"{Colors.RED}[!] Database export failure: {err}{Colors.RESET}")
    else:
        print(f"{Colors.AMBER}[!] Found existing baseline. Cross-referencing folder metadata changes...{Colors.RESET}\n")
        try:
            with open(manifest_file, 'r', encoding='utf-8') as f:
                baseline_hashes = json.load(f)
                
            added_files = [p for p in current_hashes if p not in baseline_hashes]
            deleted_files = [p for p in baseline_hashes if p not in current_hashes]
            modified_files = [p for p in current_hashes if p in baseline_hashes and current_hashes[p] != baseline_hashes[p]]
            
            print(f"{Colors.BOLD}INTEGRITY SCAN REPORT:{Colors.RESET}")
            print("-" * 75)
            print(f"  Active Monitored Items : {len(current_hashes)}")
            print(f"  Untracked New Additions: {Colors.AMBER}{len(added_files)}{Colors.RESET}")
            print(f"  Missing Deleted Items  : {Colors.RED}{len(deleted_files)}{Colors.RESET}")
            print(f"  Modified Data Signatures: {Colors.RED}{len(modified_files)}{Colors.RESET}")
            print("-" * 75)
            
            for p in added_files: print(f"  {Colors.GREEN}[NEW FILE]{Colors.RESET} {p}")
            for p in deleted_files: print(f"  {Colors.RED}[DELETED]{Colors.RESET} {p}")
            for p in modified_files: print(f"  {Colors.RED}[MODIFIED]{Colors.RESET} {p}")
            
            sync_permission = input("\nOverwrite baseline manifest database with current state mapping? (Y/N): ").strip().upper()
            if sync_permission == 'Y':
                with open(manifest_file, 'w', encoding='utf-8') as f:
                    json.dump(current_hashes, f, indent=4)
                print(f"{Colors.GREEN}[✓] Snapshot database registry synchronized.{Colors.RESET}")
        except Exception as sync_err:
            print(f"{Colors.RED}[!] Failed to complete workspace integrity comparison: {sync_err}{Colors.RESET}")
            
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_ssl_auditor():
    """Connects to server ports using standard ssl libraries to inspect peer certificate states and expiration vectors."""
    import ssl
    print(f"\n{Colors.GREEN}[MODULE 02 // SSL/TLS CERTIFICATE & CIPHER SUITE AUDITOR]{Colors.RESET}")
    print("Establishes secure socket connection layers to audit server ciphers and parameters.")
    target_host = input("\nEnter target host machine domain string (e.g., encrypted.com): ").strip()
    if not target_host:
        return
        
    port = 443
    print(f"\n{Colors.GREEN}Initiating production TLS connection handshake stream...{Colors.RESET}")
    try:
        ssl_context = ssl.create_default_context()
        base_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        base_socket.settimeout(4.5)
        
        secure_socket = ssl_context.wrap_socket(base_socket, server_hostname=target_host)
        secure_socket.connect((target_host, port))
        
        negotiated_cipher = secure_socket.cipher()
        peer_certificate = secure_socket.getpeercert()
        secure_socket.close()
        
        print(f"\n{Colors.GREEN}[✓] TELEMETRY DISCOVERED // SUCCESSFUL SECURE DISCOVERY HANDSHAKE{Colors.RESET}")
        print("-" * 75)
        print(f"  ➔ Active Cipher Suite: {Colors.CYAN}{negotiated_cipher[0]}{Colors.RESET} ({negotiated_cipher[1]} Protocol Build)")
        
        if peer_certificate:
            from datetime import datetime
            expiration_string = peer_certificate.get('notAfter')
            if expiration_string:
                try:
                    expiry_date = datetime.strptime(expiration_string, '%b %d %H:%M:%S %Y %Z')
                    remaining_days = (expiry_date - datetime.utcnow()).days
                    status_color = Colors.GREEN if remaining_days > 30 else Colors.RED
                    print(f"  ➔ Expiration Limit  : {expiration_string} ({status_color}{remaining_days} Days Remaining{Colors.RESET})")
                except Exception:
                    print(f"  ➔ Expiration Limit  : {expiration_string}")
                    
            subject_dict = dict(x[0] for x in peer_certificate.get('subject', []))
            print(f"  ➔ Certificate Owner : {subject_dict.get('commonName', 'N/A')}")
            issuer_dict = dict(x[0] for x in peer_certificate.get('issuer', []))
            print(f"  ➔ Cert Authority    : {issuer_dict.get('organizationName', 'N/A')}")
    except Exception as tls_err:
        print(f"\n{Colors.RED}[!] Secure Telemetry Handshake Terminated: Connection failure: {tls_err}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_connection_profiler():
    """Queries kernel network tables via native system utilities to display listening connection descriptors."""
    print(f"\n{Colors.GREEN}[MODULE 03 // HOST ACTIVE NETWORK CONNECTION & LISTENING PORT PROFILER]{Colors.RESET}")
    print("Audits open system interfaces to trace running host gateway listeners.")
    
    is_windows = sys.platform.startswith('win')
    cmd_arguments = ['netstat', '-ano'] if is_windows else ['ss', '-tuln']
    
    print(f"\n{Colors.GREEN}Executing native administrative subprocess network layer queries...{Colors.RESET}\n")
    print("-" * 75)
    
    try:
        subprocess_result = subprocess.run(cmd_arguments, capture_output=True, text=True, errors='ignore')
        output_rows = subprocess_result.stdout.splitlines()
        
        for row in output_rows[:45]:
            print(row)
        if len(output_rows) > 45:
            print(f"\n{Colors.AMBER}[...] Output truncated. Total connection descriptors log count: {len(output_rows)} lines.{Colors.RESET}")
    except Exception as exec_err:
        print(f"{Colors.RED}[!] Subprocess execution dropped: Target utility failed: {exec_err}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_password_auditor():
    """Performs localized Shannon information-entropy metric calculations to check credential complexity parameters completely offline."""
    print(f"\n{Colors.GREEN}[MODULE 04 // PASSWORD COMPLEXITY & OFFLINE INFORMATION ENTROPY SCANNERS]{Colors.RESET}")
    print("Evaluates string byte structural parameters mathematically without network exposure.")
    target_pwd = input("\nEnter credential string value to audit: ").strip()
    if not target_pwd:
        return
        
    string_length = len(target_pwd)
    has_upper = any(c.isupper() for c in target_pwd)
    has_lower = any(c.islower() for c in target_pwd)
    has_digit = any(c.isdigit() for c in target_pwd)
    has_special = any(not c.isalnum() for c in target_pwd)
    
    character_pool = 0
    if has_lower: character_pool += 26
    if has_upper: character_pool += 26
    if has_digit: character_pool += 10
    if has_special: character_pool += 32
    
    calculated_entropy = 0.0
    if character_pool > 0:
        calculated_entropy = math.log2(character_pool) * string_length
        
    print(f"\n{Colors.BOLD}INFORMATION THEORY AUDIT PARAMETERS:{Colors.RESET}")
    print("-" * 75)
    print(f"  ➔ Character Length Metric: {string_length} glyph elements")
    print(f"  ➔ Flag Allocations Array : Upper={has_upper}, Lower={has_lower}, Num={has_digit}, Symbol={has_special}")
    print(f"  ➔ Alphabet Complexity Pool: {character_pool} unique configuration variants")
    print(f"  ➔ Calculation Reference   : log2({character_pool}) * {string_length}")
    print(f"  ➔ Evaluated Entropy Rank  : {calculated_entropy:.4f} bits of information space density")
    print("-" * 75)
    
    if calculated_entropy < 40.0:
        print(f"  Analysis Verdict : {Colors.RED}[!!!] WEAK STRUCTURE // CRITICAL RATING // PASS PHRASE COMPROMISE RISK{Colors.RESET}")
    elif calculated_entropy < 70.0:
        print(f"  Analysis Verdict : {Colors.AMBER}[!] REGULAR PROFILE // MEDIUM COMPLIANCE RATING // STRENGTHENING RECOMMENDED{Colors.RESET}")
    else:
        print(f"  Analysis Verdict : {Colors.GREEN}[✓] HIGH DENSITY RUGGED BASELINE STABLE PROFILE{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_arp_profiler():
    """
    Parses active local neighbor parameters dynamically via native system calls.
    Detects duplicate MAC assignments indicating structural routing anomalies or poisoning threats.
    """
    print(f"\n{Colors.GREEN}[MODULE 05 // LOCAL NETWORK ARP Table CACHE PROFILER & DUPLICATE MAC AUDITOR]{Colors.RESET}")
    print("Audits neighbor hardware directories recursively to evaluate network layer security states.")
    time.sleep(0.5)

    is_windows = sys.platform.startswith('win')
    cmd_arguments = ['arp', '-a']
    
    print(f"\n{Colors.GREEN}Invoking administrative hardware resolution cache tables...{Colors.RESET}\n")
    print(f"{Colors.BOLD}{'LOCAL IP COMPONENT':<24}{'PHYSICAL HARDWARE ADDRESS (MAC)':<26}{'ALLOCATION STATE'}{Colors.RESET}")
    print("-" * 75)

    try:
        process_result = subprocess.run(cmd_arguments, capture_output=True, text=True, errors='ignore')
        output_lines = process_result.stdout.splitlines()
        
        # Simple dictionaries to cross-examine network address patterns
        mac_registry = {}
        arp_entries_found = 0

        # Regular expressions to parse standard IP and MAC variations smoothly
        ip_pattern = re.compile(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
        mac_pattern = re.compile(r'(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}')

        for line in output_lines:
            found_ip = ip_pattern.search(line)
            found_mac = mac_pattern.search(line)
            
            if found_ip and found_mac:
                arp_entries_found += 1
                ip_str = found_ip.group(0)
                mac_str = found_mac.group(0).lower().replace('-', ':')
                
                # Deduce interface configuration types (Dynamic vs Static bindings)
                allocation_type = "STATIC" if "static" in line.lower() else "DYNAMIC"
                
                print(f"  {ip_str:<22}{mac_str:<26}{allocation_type}")
                
                if mac_str not in mac_registry:
                    mac_registry[mac_str] = []
                mac_registry[mac_str].append(ip_str)

        print("-" * 75)
        print(f"[✓] Active hardware address caches analyzed: {arp_entries_found} network bindings mapped.")
        
        # Verify duplicate physical MAC structures (potential indicators of security anomalies)
        anomalies_detected = 0
        for mac, ip_list in mac_registry.items():
            # Filter standard broadcast/multicast boundaries (e.g., ff:ff:ff:ff:ff:ff)
            if len(ip_list) > 1 and mac != "ff:ff:ff:ff:ff:ff" and not mac.startswith("224.") and not mac.startswith("239."):
                anomalies_detected += 1
                print(f"\n{Colors.RED}[!] WARNING // DUPLICATE HARDWARE MAPPING DETECTED{Colors.RESET}")
                print(f"  Physical Hardware ID: {Colors.AMBER}{mac}{Colors.RESET}")
                print(f"  Conflicting IP Nodes: {Colors.CYAN}{', '.join(ip_list)}{Colors.RESET}")
                print("  Defensive Audit Note: Multiple logical network routes pointing to a single physical device frame")
                print("                        can indicate local routing bugs or configuration anomalies.")

        if anomalies_detected == 0:
            print(f"{Colors.GREEN}[✓] Layer 2 Security Status Baseline: Clean. No physical node overlap caught.{Colors.RESET}")

    except Exception as err:
        print(f"{Colors.RED}[!] Subprocess lookup execution error tracking table allocations: {err}{Colors.RESET}")

    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

# ================================================================================
# CENTRAL SUPSYSTEM SHELL MATRIX ORCHESTRATION LOOP
# ================================================================================

def handle_category_deck(deck_id):
    """
    Acts as the second-tier router, isolating application submenus inside locked
    loop environments to maximize screen space and remove menu clutter.
    """
    while True:
        print(Colors.CLEAR_SCREEN)
        
        # --- ENGINE PIPELINE 01: RECON UTILITIES ---
        if deck_id == "1":
            MainframeUI.display_network_menu()
            operator_input = input(f"{Colors.BOLD}mainframe@recon_cores:~# {Colors.RESET}").strip()
            
            if operator_input == "1":
                run_pinger_engine()
            elif operator_input == "2":
                run_reverse_dns()
            elif operator_input == "3":
                run_port_scanner()
            elif operator_input == "4":
                run_ping_sweeper()
            elif operator_input == "5":
                run_banner_grabber()
            elif operator_input == "6":
                run_dns_recon()
            elif operator_input == "7":
                run_subdomain_finder()
            elif operator_input == "8":
                run_rdap_lookup()
            elif operator_input == "9":
                break
                
        # --- ENGINE PIPELINE 02: EXT-OSINT UTILITIES ---
        elif deck_id == "2":
            MainframeUI.display_osint_menu()
            operator_input = input(f"{Colors.BOLD}mainframe@osint_engines:~# {Colors.RESET}").strip()
            
            if operator_input == "1":
                run_sherlock_hook()
            elif operator_input == "2":
                run_phoneinfoga_hook()
            elif operator_input == "3":
                run_holehe_hook()
            elif operator_input == "4":
                run_socialscan_hook()
            elif operator_input == "5":
                run_live_breach_checker()
            elif operator_input == "6":
                run_threat_intel()
            elif operator_input == "7":
                break
                
        # --- ENGINE PIPELINE 03: LOCAL UTILITIES & SCANS ---
        elif deck_id == "3":
            MainframeUI.display_utilities_menu()
            operator_input = input(f"{Colors.BOLD}mainframe@local_utilities:~# {Colors.RESET}").strip()
            
            if operator_input == "1":
                run_traffic_monitor()
            elif operator_input == "2":
                run_secret_scanner()
            elif operator_input == "3":
                run_hash_matrix()
            elif operator_input == "4":
                run_system_profiler()
            elif operator_input == "5":
                run_base64_matrix()
            elif operator_input == "6":
                break

        # --- ENGINE PIPELINE 04: ADVANCED COMPLIANCE AUDITS ---
        elif deck_id == "4":
            MainframeUI.display_advanced_audits_menu()
            operator_input = input(f"{Colors.BOLD}mainframe@advanced_audits:~# {Colors.RESET}").strip()
            
            if operator_input == "1":
                run_file_integrity_monitor()
            elif operator_input == "2":
                run_ssl_auditor()
            elif operator_input == "3":
                run_connection_profiler()
            elif operator_input == "4":
                run_password_auditor()
            elif operator_input == "5":
                run_arp_profiler()
            elif operator_input == "6":
                break
        else:
            break

def main():
    """
    Main runtime entry point. Automatically triggers UAC privilege escalation checks
    on Windows hosts to guarantee raw sockets tracking capability out of the box.
    """
    if sys.platform.startswith('win'):
        try:
            # Check for administrative permission matrices via shell32 APIs
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[!] Operating Privileges Insufficient. Elevating execution shell context...")
                time.sleep(1)
                # Re-invoke python executable context using shell UAC elevation triggers
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit(0)
        except Exception as elevation_fault:
            print(f"Windows privilege monitor initialization error: {elevation_fault}")
            time.sleep(2)

    # Engaged Session Logging Infrastructure
    try:
        log_directory = "logs"
        os.makedirs(log_directory, exist_ok=True)
        session_timestamp = time.strftime("%Y%m%d_%H%M%S")
        log_file_name = os.path.join(log_directory, f"session_{session_timestamp}.txt")
        
        # Instantiate dual stream hook to duplicate runtime terminal history to disk safely
        active_log_handle = open(log_file_name, "w", encoding="utf-8")
        sys.stdout = DualStreamWriter(sys.stdout, active_log_handle)
        print(f"[+] Automated Dual-Stream System Logging Operational Cores Engaged.")
        print(f"[+] Log Target Vector Initialized: {log_file_name}\n")
        time.sleep(1)
    except Exception as log_init_err:
        print(f"[!] Warning: Session logging buffer core initialization interrupted: {log_init_err}")
        time.sleep(1.5)

    while True:
        try:
            # Wipe view stack completely before drawing fresh menu maps
            print(Colors.CLEAR_SCREEN)
            MainframeUI.draw_banner()
            MainframeUI.display_main_menu()
            
            selection_target = input(f"{Colors.BOLD}mainframe@operator_console:~# {Colors.RESET}").strip()
            
            if selection_target in ["1", "2", "3", "4"]:
                handle_category_deck(selection_target)
            elif selection_target == "5":
                print(f"\n{Colors.RED}Disconnecting security core links. Clearing memory trace structures...{Colors.RESET}")
                time.sleep(1)
                print(f"{Colors.GREEN}Console session closed successfully. Systems baseline nominal.{Colors.RESET}\n")
                break
            else:
                print(f"\n{Colors.RED}[!] Unknown instruction parameter sequence. Resetting workspace...{Colors.RESET}")
                time.sleep(1.2)
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.GREEN if hasattr(Colors, 'GREEN') else Colors.RESET}[!] Main operational workflow interrupted. Disposing active frames...{Colors.RESET}")
            break
        except Exception as internal_error:
            print(f"\n{Colors.RED}Mainframe master pipeline failure logged: {internal_error}{Colors.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()