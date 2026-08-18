# MAINFRAME // COMPREHENSIVE SECURITY RECONNAISSANCE ENGINE

**Version:** v5.90  
**Architecture:** Multi-Tier Nested Subsystem Shell (Directory-Driven Layout)  
**Platform:** Cross-Platform Windows/Linux/macOS  
**Python:** 3.8+  

---

## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Main System Directory Core](#main-system-directory-core)
5. [Sub-Directory 01 — Network Infrastructure & Endpoint Recon](#sub-directory-01--network-infrastructure--endpoint-recon)
6. [Sub-Directory 02 — External OSINT & Target Record Profilers](#sub-directory-02--external-osint--target-record-profilers)
7. [Sub-Directory 03 — Local Data Traffic, Security Audits & Utilities](#sub-directory-03--local-data-traffic-security-audits--utilities)
8. [Sub-Directory 04 — Advanced Infrastructure Audits & Integrity](#sub-directory-04--advanced-infrastructure-audits--integrity)
9. [Sub-Directory 05 — Attack Vectors & Exploit Frameworks](#sub-directory-05--attack-vectors--exploit-frameworks)
10. [Image Logger — Vercel Deployment](#image-logger--vercel-deployment)
11. [Logging & Privacy](#logging--privacy)
12. [Configuration & Customization](#configuration--customization)
13. [Dependencies](#dependencies)
14. [Disclaimer](#disclaimer)

---

## OVERVIEW

MAINFRAME is a comprehensive security reconnaissance and testing platform designed for authorized security assessments, penetration testing, and educational purposes. It provides a unified terminal interface for network analysis, OSINT gathering, local system auditing, and controlled attack vector testing.

The tool is organized into five primary operational directories, each containing specialized modules for different aspects of security testing.

---

## ARCHITECTURE

```
cybertool/
├── mainframe.py                 # Core orchestration engine & UI
├── core/
│   ├── etc/
│   │   ├── settings.py          # Configuration management
│   │   └── functions.py         # UI helpers, banners, menus
│   ├── ddos_attack/
│   │   └── ddos.py              # Beast Mode DDoS engine
│   ├── brute_force/
│   │   └── bruteforce.py        # Brute force attack module
│   ├── image_logger/
│   │   └── imagelogger.py       # Local image logger server
│   ├── sms_spam/
│   │   └── sms.py               # SMS bombing module
│   ├── email_spam/
│   │   └── email_attack.py      # Email flood module
│   ├── telegram_spam/
│   │   └── telegram.py          # Telegram injection module
│   ├── discord_spam/
│   │   └── discord.py           # Discord spam module
│   ├── network/                 # Network recon modules
│   ├── osint/                   # OSINT modules
│   ├── utilities/               # Local utility modules
│   └── advanced/                # Advanced audit modules
├── vercel-image-logger/
│   ├── api/
│   │   └── track.js             # Vercel serverless function
│   ├── vercel.json              # Vercel routing config
│   └── package.json             # Project metadata
├── input/
│   ├── brutef.txt               # Brute force wordlist
│   └── proxies.txt              # Proxy list (optional)
├── logs/                        # Session logs (gitignored)
└── README.md
```

### Key Design Principles

- **Modular Architecture:** Each attack/recon module is isolated in its own directory under `core/`
- **Lazy Imports:** Optional modules are imported independently so missing dependencies don't break the entire tool
- **Dual-Stream Logging:** All terminal output is simultaneously logged to disk
- **Cross-Platform:** Supports Windows, Linux, and macOS with platform-specific optimizations
- **Auto-Elevation:** Automatically requests Administrator/Root privileges on Windows when needed

---

## INSTALLATION

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/cybertool.git
cd cybertool

# Install Python dependencies
pip install -r requirements.txt

# Or install manually
pip install colorama requests fade beautiful-table rich
```

### Optional Dependencies

Some modules require additional tools:

- **Sherlock:** `pip install sherlock`
- **PhoneInfoga:** Requires Go installation
- **Holehe:** `pip install holehe`
- **Socialscan:** `pip install socialscan`
- **Nmap:** Required for advanced port scanning
- **Wireshark/TShark:** Required for packet monitoring
- **Node.js & Vercel CLI:** Required for Image Logger deployment (`npm i -g vercel`)

---

## MAIN SYSTEM DIRECTORY CORE

The main menu serves as the primary navigation hub, organized into 5 operational subdirectories plus a shutdown control.

```
[MAIN SYSTEM DIRECTORY CORE]

[1] Sub-Directory 01 // Network Infrastructure & Endpoint Recon Cores
[2] Sub-Directory 02 // External OSINT & Target Record Profilers
[3] Sub-Directory 03 // Local Data Traffic Monitors, Audits & Utilities
[4] Sub-Directory 04 // Advanced Infrastructure Audits & Integrity Cores
[5] Sub-Directory 05 // Attack Vectors & Exploit Frameworks [SHELL BASELINE]

[SYSTEM SHUTDOWN CONTROL]
[6] Terminate Active Mainframe Operator Control Session
```

---

## SUB-DIRECTORY 01 — NETWORK INFRASTRUCTURE & ENDPOINT RECON

**Purpose:** Active network reconnaissance, host discovery, and service enumeration.

### Modules

#### [1] High-Speed Rainbow Echo Pinger Latency Monitor
- Measures ICMP echo latency to target hosts
- Supports continuous ping monitoring with color-coded status
- Configurable target IP with default fallback
- Real-time latency display with responsive/non-responsive indicators

#### [2] Reverse DNS Infrastructure Resolver (IP-to-Host PTR Check)
- Resolves IP addresses to hostnames using reverse DNS
- Displays PTR record results or indicates missing reverse name pointers
- Useful for identifying infrastructure ownership

#### [3] Multi-Threaded Target Service Port Scanner & Vulnerability Profiler
- Scans target hosts for open TCP ports
- Multi-threaded for high-speed scanning
- Service version detection and vulnerability profiling
- Common port-to-service mapping with defensive mitigation hints
- Adjustable thread count

#### [4] Local Subnet Parallel Ping Sweeper Matrix
- Discovers active devices on local network segments
- Parallel ping sweeps across IP ranges
- Color-coded responsive device detection
- Subnet calculator for target range generation

#### [5] Network Application Service Banner Grabber Auditor
- Connects to open ports and retrieves service banners
- Identifies software versions and potential vulnerabilities
- TCP connection-based banner extraction

#### [6] DNS Reconnaissance Explorer Matrix (AddrInfo Lookup)
- Performs DNS A/AAAA record lookups
- Extracts IP addresses and aliases from target domains
- Uses system `nslookup` or Python socket resolution

#### [7] Passive Domain Subdomain Discovery Engine (via crt.sh Logs)
- Discovers subdomains through Certificate Transparency logs
- Queries crt.sh API for historical certificate data
- Passive reconnaissance without direct target contact

#### [8] Advanced RDAP Registration Infrastructure Allocation Mapper
- Queries RDAP (Registration Data Access Protocol) for domain registration info
- Extracts registrar, organization, country, and network allocation data
- Provides production infrastructure metric data blocks

#### [9] HTTP Header Security Compliance & Hardening Auditor
- Analyzes HTTP security headers
- Checks for HSTS, CSP, X-Frame-Options, X-XSS-Protection, etc.
- Provides mitigation purpose descriptions for each header

#### [10] DNS-over-HTTPS (DoH) Client Resolver Subsystem
- Performs DNS queries over HTTPS using Cloudflare DoH
- Encrypted DNS resolution for privacy
- Returns structured DNS records with TTL data

---

## SUB-DIRECTORY 02 — EXTERNAL OSINT & TARGET RECORD PROFILERS

**Purpose:** Open-source intelligence gathering and target profiling using external tools.

### Modules

#### [1] Sherlock Username Account Tracer (Live Shell Subprocess Launch)
- Hunts for usernames across 300+ social media platforms
- Launches Sherlock in a subprocess with colored output
- Real-time account discovery with site-by-site results

#### [2] PhoneInfoga Telecom Target Scanner (Live Shell Subprocess Launch)
- Telecom reconnaissance using PhoneInfoga
- Phone number validation and carrier lookup
- Number formatting and regional analysis

#### [3] Holehe Email Platform Account Auditor (Live Shell Subprocess Launch)
- Checks if email addresses are registered on 100+ platforms
- Uses Holehe to audit email presence across sites
- Color-coded results for quick analysis

#### [4] Socialscan Concurrent Identity Profiler (Live Shell Subprocess Launch)
- Concurrent username/email scanning across platforms
- Multi-threaded profile enumeration
- Live shell output with progress indicators

#### [5] Live Online Data Breach Explorer & Password Leak Checker
- Checks email/username against known data breaches
- Queries breach databases for compromised credentials
- Provides breach count and exposure details

#### [6] Tor Exit Node Network Threat Intelligence Node Validator
- Fetches current Tor exit node IPs from dan.me.uk
- Validates if an IP is a known Tor exit node
- Threat intelligence for network access control

#### [7] Online IP Geolocation & Autonomous System (ASN) Metadata Explorer
- Geolocates IP addresses using ip-api.com
- Returns city, region, country, ISP, ASN, and timezone data
- JSON-based structured geolocation results

#### [8] IDN Homograph Phishing Domain & Punycode Analyzer
- Detects internationalized domain name (IDN) homograph attacks
- Analyzes domains for deceptive Unicode characters
- Punycode conversion and visual similarity detection

---

## SUB-DIRECTORY 03 — LOCAL DATA TRAFFIC, SECURITY AUDITS & UTILITIES

**Purpose:** Local system analysis, encryption utilities, and traffic monitoring.

### Modules

#### [1] Inbound Network Packet Monitor Engine (Requires Admin Context)
- Live packet capture and analysis
- Requires Administrator privileges on Windows
- Displays source/destination IPs and protocols
- Real-time traffic monitoring with color-coded output

#### [2] Local Directory Source Code 'Secret & Private Key' Leak Scanner
- Recursively scans directories for exposed secrets
- Pattern matching for API keys, tokens, passwords, private keys
- Supports multiple file extensions: `.env`, `.pem`, `.key`, `.p12`, etc.
- Base64 pattern detection for encoded secrets

#### [3] Cryptographic Hash Signatures Matrix Generation & Token Analyzer
- Generates MD5, SHA-1, SHA-256 hashes for files/text
- Batch hash processing with progress indicators
- Hash format validation and display

#### [4] Advanced Local Host Operating System Telemetry Profiler
- Comprehensive system information gathering
- OS, hostname, architecture, processor, RAM, GPU, network interfaces
- Formatted table output with all system metrics

#### [5] Base64 Cryptographic Processing Matrix (Data Transformation)
- Encode/decode text to/from Base64
- Encrypt/decrypt text with custom password key
- File encoding/decoding support
- Stream cipher implementation for text encryption

---

## SUB-DIRECTORY 04 — ADVANCED INFRASTRUCTURE AUDITS & INTEGRITY

**Purpose:** Deep system audits, integrity checking, and network analysis.

### Modules

#### [1] Local File Integrity Monitor (FIMS Directory Snapshot Tracker)
- Creates baseline snapshots of file integrity
- MD5 hash tracking for files in specified directories
- Compares current state against baseline
- Detects unauthorized file modifications

#### [2] SSL/TLS Certificate Expiration & Cipher Suite Auditor
- Connects to remote servers and retrieves SSL/TLS certificates
- Extracts expiration dates, issuers, and subjects
- Color-coded warnings for expiring certificates
- Cipher suite enumeration

#### [3] Host Active Network Connection & Listening Port Profiler
- Displays active network connections using `netstat`
- Shows local/foreign addresses and connection states
- Lists listening ports and associated processes
- Windows-specific process resolution

#### [4] Password Complexity & Offline Information Entropy Matrix
- Analyzes password strength using zxcvbn algorithm
- Calculates entropy bits and crack time estimates
- Checks against common patterns and dictionary words
- Provides strength score and suggestions

#### [5] Local Network ARP Table Cache Profiler & Duplicate MAC Auditor
- Displays ARP table entries using `arp -a`
- Shows IP-to-MAC mappings for local network
- Identifies potential duplicate MAC address conflicts

#### [6] CIDR Subnet IPv4 Network Range & Mask Calculator
- Calculates network ranges from CIDR notation
- Converts subnet masks to wildcard masks
- Determines network class, host capacity, and broadcast address
- Supports all valid CIDR prefixes (1-32)

#### [7] UPnP SSDP Local LAN Smart Device Discovery Explorer
- Discovers UPnP devices on local network
- SSDP multicast discovery protocol
- Identifies smart devices, routers, and media servers

#### [8] Local Hosts File DNS Spoofing & Cache Poisoning Auditor
- Scans local hosts file for suspicious entries
- Detects potential DNS hijacking or cache poisoning
- Checks for common phishing/malware domains
- File hash verification for hosts file integrity

#### [9] MAC Address OUI Vendor Directory Lookup Engine
- Identifies device manufacturers from MAC addresses
- OUI (Organizationally Unique Identifier) lookup
- Supports local ARP table scanning or manual input
- Vendor name resolution from MAC prefix

---

## SUB-DIRECTORY 05 — ATTACK VECTORS & EXPLOIT FRAMEWORKS

**Purpose:** Controlled attack vectors for authorized security testing.

### Modules

#### [1] Beast Mode (DDoS)
- Multi-threaded DDoS testing engine
- **Beast Mode feature:** Hold `1` key to continuously launch attack bursts
- Press `0` to stop beast mode
- Proxy support for distributed testing
- Configurable thread count and target URL
- Real-time success/failure counters

#### [2] Image Logger
- Generates image tracking links that log visitor IP addresses
- Two deployment options:
  - **Local Server:** Runs on `http://localhost:8080`
  - **Vercel Deployment:** Auto-deploys to public Vercel URL
- Displays target GIF with Open Graph tags for Discord/social preview
- Real-time IP monitoring in mainframe terminal
- Captures User-Agent, timestamp, and IP on page visit
- `/api/logs` endpoint for programmatic log access

#### [3] Brute Force
- Automated password brute forcing with configurable wordlists
- **Auto wordlist:** Uses `input/brutef.txt` by default
- Two attack modes:
  - **Login Form:** POST request brute forcing with custom field names
  - **Basic Auth:** HTTP Basic Authentication header brute forcing
- Proxy support with multi-threading
- Success indicator matching (page text or HTTP status)
- Real-time cracked/failed counters

#### [4] SMS Spam
- SMS bombing module with multi-threading
- Proxy support for rate limit bypass
- Configurable message count and thread count
- Real-time send status tracking

#### [5] Email Spam
- Email flooding module
- SMTP configuration with custom sender/recipient
- Multi-threaded sending with proxy support
- HTML email support

#### [6] Telegram Spam
- Telegram message automation
- Token-based authentication
- Multi-threaded message sending
- Proxy support

#### [7] Discord Spam
- Discord channel/User messaging
- Token-based authentication
- Multi-threaded spam with proxy rotation
- Configurable message content and targets

---

## IMAGE LOGGER — VERCEl DEPLOYMENT

The Image Logger can be deployed to Vercel for a public URL that works everywhere, including Discord.

### How It Works

1. **Deployment:** Mainframe auto-deploys `vercel-image-logger/` to Vercel
2. **Public URL:** Generates a shareable `https://*.vercel.app` link
3. **Tracking:** When someone opens the link:
   - Their IP address is logged
   - User-Agent and timestamp are captured
   - Data is stored in Vercel's ephemeral `/tmp` storage
4. **Monitoring:** Mainframe terminal polls `/api/logs` and displays captures in real-time
5. **Image Preview:** The page serves a GIF directly as `image/gif` for proper Discord preview

### Technical Details

- **Framework:** Vercel Node.js Serverless Function
- **Image:** `https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif`
- **Logs Endpoint:** `https://vercel-image-logger.vercel.app/api/logs`
- **Response Format:** Direct binary GIF with caching disabled
- **OG Tags:** Open Graph and Twitter Card meta tags for social previews

### Local vs Vercel

| Feature | Local Server | Vercel Deployment |
|---------|-------------|-------------------|
| URL | `localhost:8080` | `*.vercel.app` |
| Discord Preview | Limited | Full image preview |
| Accessibility | Local only | Public internet |
| Logs | In-memory | Vercel `/tmp` (ephemeral) |
| Monitoring | Live terminal | Live terminal via API |

---

## LOGGING & PRIVACY

### Session Logging

MAINFRAME implements dual-stream logging:
- All terminal output is captured to `logs/session_YYYYMMDD_HHMMSS.txt`
- Logs are written in real-time as the tool runs
- ANSI color codes are stripped from log files for readability

### Privacy Protection

To protect your privacy when sharing this tool:

1. **Logs Directory:** The `logs/` folder is gitignored
2. **No IP Storage:** The Vercel image logger does not store logs locally
3. **Ephemeral Storage:** Vercel serverless functions use temporary storage
4. **Session Isolation:** Each run creates a new timestamped log file

### What Gets Logged

- Terminal output from all modules
- Image logger captures (Vercel only, not local)
- Session start/stop timestamps
- Error messages and stack traces

### What Does NOT Get Logged

- Your personal IP address (unless you test with yourself)
- Credentials or passwords entered during brute force
- Target information from recon modules
- Any data from the `input/` directory

---

## CONFIGURATION & CUSTOMIZATION

### Wordlist Configuration

The Brute Force module automatically uses:
```
input/brutef.txt
```

Place your custom wordlist at this path. One password per line.

### Proxy Configuration

Optional proxy support via:
```
input/proxies.txt
```

Format: One proxy per line (e.g., `http://proxy:port` or `socks5://proxy:port`)

### Settings

Access settings via the main menu or directly in `core/etc/settings.py`:
- Language preferences (EN/RU)
- Color schemes
- Default thread counts
- Module enable/disable flags

### Module Paths

All modules are loaded from `core/` with independent imports. To disable a module:
1. Delete or rename its folder under `core/`
2. The mainframe will skip it gracefully with a "not loaded" message

---

## DEPENDENCIES

### Python Packages

```
colorama       # Terminal colors
requests       # HTTP requests
fade           # ASCII art fading
beautiful-table # Table formatting
rich           # Terminal UI (optional)
```

### External Tools (Optional)

```
nmap           # Port scanning
tshark         # Packet capture
go             # Sherlock, PhoneInfoga
node.js        # Vercel image logger
vercel CLI     # Image logger deployment
```

### Platform-Specific

- **Windows:** `ctypes` for UAC elevation, `GetAsyncKeyState` for beast mode
- **Linux/macOS:** `subprocess` for system commands, `termios` for key detection

---

## DISCLAIMER

**This tool is for authorized security testing and educational purposes only.**

- Only use on systems you own or have explicit written permission to test
- Unauthorized access to computer systems is illegal
- The authors are not responsible for misuse or damage caused by this tool
- Users assume all liability for their actions
- Respect all applicable laws and regulations in your jurisdiction

---

## LICENSE

Copyright (C) 2024 un1ucm  
All rights reserved.

When posting this code on other resources, please indicate the author.

---

*MAINFRAME v5.90 — Comprehensive Security Reconnaissance Engine*
