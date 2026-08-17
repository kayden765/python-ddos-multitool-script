# MAINFRAME // SEC-OPERATIONS INTERACTIVE TERMINAL MULTITOOL

An advanced, multi-directory terminal auditing shell and network diagnostics mainframe built natively in Python. Engineered exclusively for defensive network administration, compliance monitoring, and passive security analysis, this zero-dependency platform consolidates 30 production-grade scanning, profiling, and open-source intelligence (OSINT) engines into a single operational interface.

---
## 🛠️ Quick Start & Usage Guide

Follow these simple steps to run and navigate your 30-in-1 security multitool mainframe:

[1] Install System Dependencies
    Before launching the script for the first time, synchronize your Python environment using the requirements profile:
    pip install -r requirements.txt

    (Note: To utilize the PhoneInfoga module, ensure your native pre-compiled 'phoneinfoga' binary file is placed directly inside the script's active folder directory).

[2] Launch with Elevated Administrative/Root Privileges
    Because low-level packet tracking (Inbound Network Packet Monitor Engine) and local socket table lookups require full operating system kernel access, you must run your terminal with administrator privileges:
    - Windows: Search for Command Prompt or PowerShell, right-click it, select "Run as Administrator", and execute:
      python mainframe.py
    - Linux / macOS: Launch the script natively using the standard sudo command container:
      sudo python3 mainframe.py

[3] Live Visual Title Bar Scrambler
    Once the mainframe validates your privileges and boots up, it will automatically spin up a background worker thread that continuously randomizes cryptographic tokens directly inside your terminal window's top title bar for a distinct security deck aesthetic.

[4] Navigate the Directory Submenus
    The console architecture uses a multi-tier sub-menu routing system to keep your terminal layout clean and uncrowded:
    - Type '1', '2', '3', or '4' at the primary control prompt (mainframe@operator_console:~#) to dive into a specialized category sub-directory.
    - Inside any sub-directory, type the matching number to execute a tool.
    - To exit a sub-directory and return to the root menu layout, choose the navigation number ('6', '9', or '10') specified by the selection hints on your screen.

[5] Review Active Session Activity Logs
    - Every command execution, tested target parameter, and screen output is mirrored automatically in real-time.
    - Look inside the dynamically created "/logs" folder right next to your script to read past text files. 
    - The dual-stream logging core automatically strips out messy ANSI color codes before saving to disk, leaving you with pristine, cleartext session archives.


## 🏗️ Architectural Overview & Design Parameters

* **Zero-Dependency Production Baseline:** Operates entirely out-of-the-box utilizing Python standard library structures. Requires zero mandatory external installations for all core routing, auditing, and sniffing systems.
* **Thread-Safe Dual-Stream Intercept Logging:** Features an automated, non-blocking real-time capture module that intercepts standard console output stream arrays. It writes parallel logs to local timestamped cleartext files inside a dynamically generated `/logs` directory, systematically stripping raw ANSI layout formatting colors using regex verification.
* **Process Security Verification Gate:** Enforces administrative rights validation checks at boot using Windows `ctypes` or platform-native checking loops to guarantee safe initialization of low-level packet mirrors.
* **Background Micro-Daemon Visual Matrix:** Spawns a dedicated background micro-thread daemon that shuffles randomized cryptographic tokens into the window title bar dynamically to maintain an operational aesthetic while completely bypassing session log history streams.

---

## 🛠️ Deep Feature Specification Blueprint

The application architecture is divided into four highly organized operational sub-directories to manage terminal screen estate effectively:

### 📡 Sub-Directory 01: Network Infrastructure & Endpoint Recon Cores

1. **High-Speed Rainbow Echo Pinger Latency Monitor**
   * *Mechanism:* Constructs platform-native ICMP echo requests using automated shell runtime execution parameters.
   * *Capabilities:* Implements strict text parsing criteria targeting the stdout stream to isolate valid trip metrics (`ttl=` or `time=`), completely filtering out false-positive gateway replies and unreachable codes.

2. **Reverse DNS Infrastructure Resolver (IP-to-Host PTR Check)**
   * *Mechanism:* Employs low-level socket nameserver hooks via `socket.gethostbyaddr()`.
   * *Capabilities:* Resolves explicit dotted-quad IPv4 strings back to their registered pointer (PTR) resource files, mapping assigned hostnames, structural domain aliases, and alternate interface bindings arrays.

3. **Multi-Threaded Target Service Port Scanner & Vulnerability Profiler**
   * *Mechanism:* Deploys a thread pool socket execution pool using non-blocking TCP three-way handshake connection attempts (`socket.connect_ex`).
   * *Capabilities:* Concurrently audits core networking and administrative interfaces (Ports 21-8443). Features an internal cross-reference intelligence database that maps exposed ports to known software liabilities and specific defensive mitigation guidelines.

4. **Local Subnet Parallel Ping Sweeper Matrix**
   * *Mechanism:* Fires rapid, low-overhead ICMP echo sweeps asynchronously across thread configurations.
   * *Capabilities:* Dispatches concurrent network sweeps spanning local IP address limits (`.1` to `.254`) to generate absolute physical device visibility maps without colliding with downstream console buffers.

5. **Network Application Service Banner Grabber Auditor**
   * *Mechanism:* Opens direct socket streams to target endpoints and forces request payloads.
   * *Capabilities:* Intercepts protocol header configurations and application configuration parameters, explicitly sending `HEAD` requests to web endpoints to capture detailed server build metrics.

6. **DNS Reconnaissance Explorer Matrix (AddrInfo Lookup)**
   * *Mechanism:* Calls system name service infrastructure abstractions via `socket.getaddrinfo()`.
   * *Capabilities:* Resolves and isolates alternative protocol family families, interface maps, and transport route destinations to map out domain name configurations.

7. **Passive Domain Subdomain Discovery Engine**
   * *Mechanism:* Queries public certificate transparency logging infrastructure via secure HTTPS json feeds (`crt.sh`).
   * *Capabilities:* Passive data parsing that extracts verified, historically logged subdomains for target entities without transmitting packet traffic to the target infrastructure.

8. **Advanced RDAP Registration Infrastructure Allocation Mapper**
   * *Mechanism:* Connects to open Registration Data Access Protocol (RDAP) servers natively using standard network wrappers.
   * *Capabilities:* Evaluates autonomous network range allocations, country codes, administrative internet registry boundaries, and original provider provider profiles.

9. **HTTP Header Security Compliance & Hardening Auditor**
   * *Mechanism:* Pulls remote protocol structures over port 80/443 using native HTTP clients.
   * *Capabilities:* Systematically tests for the implementation of defensive hardening headers, reporting configuration strings for `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, and `X-Content-Type-Options`.

10. **DNS-over-HTTPS (DoH) Client Resolver Subsystem**
    * *Mechanism:* Encapsulates secure name resolution lookups inside encrypted outbound port 443 packets targeting Cloudflare public nameservers.
    * *Capabilities:* Bypasses localized corporate firewall blocks or DNS cache hijacking attempts by explicitly pulling wireformat or JSON DNS mappings (`A`, `AAAA`, `MX`, `TXT`) securely.

### 🔍 Sub-Directory 02: External OSINT & Target Record Profilers


11. **Sherlock Username Account Tracer**
    * *Mechanism:* Automates external python project execution contexts using unmanaged subprocess wrappers.
    * *Capabilities:* Maps system environmental path boundaries to launch global account profile audits targeting specific handles across hundreds of social networks simultaneously.

12. **PhoneInfoga Telecom Target Scanner**
    * *Mechanism:* Executes compiled Go binary packages natively using subprocess process pipes.
    * *Capabilities:* Passes target international telephone records directly to local binaries to trace structural data and telecom provider targets safely.

13. **Holehe Email Platform Account Auditor**
    * *Mechanism:* Launches targeted password reset endpoint validation calls through system subprocess shells.
    * *Capabilities:* Isolates whether a target email address has active accounts registered across over 120 major global web platforms.

14. **Socialscan Concurrent Identity Profiler**
    * *Mechanism:* Wraps around execution loops of the Socialscan platform concurrently.
    * *Capabilities:* Validates exact username and email signature visibility configurations across target spaces with high accuracy.

15. **Live Online Data Breach Explorer**
    * *Mechanism:* Communicates with public privacy-respecting breach aggregation frameworks (`XposedOrNot`) over HTTPS clients.
    * *Capabilities:* Queries historical records to check if a specific email handle has been compromised in known corporate data exposures, listing specific breach source indices.

16. **Anonymized Password Exposure Auditor**
    * *Mechanism:* Implements k-anonymity matching models by hashing password targets into localized SHA-1 string signatures.
    * *Capabilities:* Extracts the first 5 characters of the password hash to query the `HaveIBeenPwned` range API. Receives the matching suffixes securely, preventing cleartext credentials or complete hash fields from ever traveling across local network boundaries.

17. **Tor Exit Node Network Threat Intelligence Node Validator**
    * *Mechanism:* Establishes standard HTTP connections to the official Tor Project network directory registries.
    * *Capabilities:* Synchronizes an active in-memory set of verified relay nodes to check incoming or target IP addresses, immediately flagging whether traffic originates from an anonymized proxy gateway.

18. **Online IP Geolocation & Autonomous System (ASN) Metadata Explorer**
    * *Mechanism:* Parses geo-distribution tables passively using secure API connections against public registries.
    * *Capabilities:* Discovers country profiles, regional zones, coordinates, exact timezones, internet service provider identifiers, and Autonomous System Numbers (ASN).

19. * *Mechanism:* Executes local string transformations through internationalized domain codec matrices (`idna`).
    * *Capabilities:* Translates domains between Unicode and Punycode format layers, systematically detecting spoofed brand URLs that utilize lookalike non-ASCII internationalized glyphs to trick users.

### 🛡️ Sub-Directory 03: Local Data Traffic Monitors, Audits & Utilities

20. **Inbound Network Packet Monitor Engine**
    * *Mechanism:* Binds to system hardware interface loopbacks using RAW socket interface attributes (`socket.SOCK_RAW`).
    * *Capabilities:* Provides low-level sniffer configurations to decode IPv4 packet frames. Unpacks headers in real-time, calculating buffer sizes and outputting protocol 

data columns for TCP, UDP, and ICMP frames.
21. **Local Directory Source Code 'Secret & Private Key' Leak Scanner**
    * *Mechanism:* Traverses folder directory structures recursively using file block input streams.
    * *Capabilities:* Uses optimized regular expressions to flag hardcoded secrets, matching strings for GCP keys, AWS token signatures, private RSA/OpenSSH key block headers, and unencrypted password credentials.

22. **Cryptographic Hash Signatures Matrix Generation & Token Analyzer**
    * *Mechanism:* Hooks into the system `hashlib` library offline.
* Capabilities: Transforms strings into MD5, SHA-1, and SHA-256 signatures, and reconstructs profiles of unknown hashes by assessing character density parameters and structural bit-lengths.

23. Advanced Local Host Operating System Telemetry Profiler* Mechanism: Pulls system variables via the platform and socket standard architectures.* Capabilities: Compiles device environment statistics, returning kernel architecture tags, operating build versions, processor model types, and current localized LAN loopback configurations.

24. Base64 Cryptographic Processing Matrix* Mechanism: Integrates native Base64 binary transposition codecs.* Capabilities: Securely encodes cleartext strings into standard Base64 representation formats or decodes obfuscated block sequences back to text frames entirely offline.

[25] Local File Integrity Monitor (FIMS Directory Snapshot Tracker)
    - Mechanism: Encapsulates folder infrastructure maps inside a serialized JSON metadata document (fims_manifest.json).
    - Capabilities: Performs recursive calculations using SHA-256 data footprints to detect system drift, immediately reporting rows marking unauthorized directory additions, document alterations, or system file deletions.

[26] SSL/TLS Certificate Expiration & Cipher Suite Auditor- Mechanism: Wraps standard communication transport layers inside an active ssl.create_default_context() engine.- Capabilities: Handshakes with remote server ports to parse ownership data blocks, reporting root certificate authority origins, verification scopes, and precise day counts remaining before expiration.

[27] Host Active Network Connection & Listening Port Profiler- Mechanism: Executes system connection table binaries (netstat or ss) inside safe unmanaged subprocess containers.- Capabilities: Evaluates active process tables to map system listeners, listing bound process identifiers (PIDs), active connection profiles, and protocols.

[28] Password Complexity & Offline Information Entropy Matrix- Mechanism: Applies mathematical Shannon information entropy formulas (math.log2) completely offline.- Capabilities: Assesses password character diversity arrays, calculating information density bit rankings to define structural brute-force resistance without leaking data.

[29] Local Network ARP Table Cache Profiler & Duplicate MAC Auditor- Mechanism: Compiles Layer 2 neighbor state tables using system subprocess execution (arp -a).- Capabilities: Extracts IP-to-MAC hardware groupings and screens the data cache for duplicate MAC occurrences, flagging routing anomalies or spoofing behavior.

[30] CIDR Subnet IPv4 Network Range & Mask Calculator- Mechanism: Natively handles logical bit-shifting and mask arithmetic on IPv4 dotted-quad octet bytes.- Capabilities: Resolves CIDR notations to output network boundary addresses, wildcard configuration blocks, broadcast markers, and exact assignable local host counts.

🔒 Session Privacy & Logging MechanismsThis application features an unmanaged, automated Thread-Safe Dual-Stream Intercept Logging Engine.Automatic Creation: Upon initialization, the script scans the working folder and natively spins up a local /logs folder.Pristine Cleartext Exports: Everything that prints to your console shell screen is instantly mirrored to a timestamped file (e.g., logs/session_YYYYMMDD_HHMMSS.txt).ANSI Filtering: To ensure professional log readability, an integrated regular expression engine systematically strips out raw layout color escape codes before flushing the text stream to the text file block.
