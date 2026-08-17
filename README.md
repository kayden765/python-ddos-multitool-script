FOR THE PHONEINFOGA OPTION TO WORK YOU MUST DOWNLOAD PHONE INFOGA EXE FILE FROM THERE GITHUB AND HAVE IT IN THE SAME FOLDER AS THE MAINFRAME


# python-security-multitool-script
A standalone, auto-elevating Python security multitool and network toolkit for defensive system audits, passive recon, packet sniffing, and offline infrastructure profiling.
# MAINFRAME // INTERACTIVE TERMINAL SECURITY MULTITOOL

An advanced, auto-elevating interactive console mainframe engineered for defensive network administration, passive infrastructure reconnaissance, and open-source intelligence (OSINT) auditing. Built completely from the ground up using a modular, directory-driven Python architecture, this suite provides security analysts and administrators with a centralized control deck containing 25 specialized diagnostic cores.

---

## 🛠️ How to Use the Multitool

Follow these quick steps to launch and operate the security multitool mainframe:

### 1. Install Dependencies
Before running the application for the first time, ensure the required third-party OSINT libraries are installed on your system:
```bash
pip install -r requirements.txt
```
*(Note: To use the PhoneInfoga module, ensure your native `phoneinfoga` binary file is placed directly in the script folder).*

### 2. Launch with Elevated Privileges
Because raw network sockets and network connection profiling require full kernel access, you **must** run the terminal as an Administrator or Root user:
* **Windows:** Search for `cmd` or `PowerShell`, right-click it, and select **"Run as Administrator"**, then run:
  ```cmd
  python mainframe.py
  ```
* **Linux / macOS:** Launch the script natively using `sudo`:
  ```bash
  sudo python3 mainframe.py
  ```

### 3. Navigate the Directories
The interface uses a multi-tier directory structure to keep your screen clean:
* Type **`1`**, **`2`**, or **`3`** at the primary console prompt (`mainframe@operator_console:~#`) to dive into a specific sub-directory category.
* Inside any sub-directory, type the matching number to execute a tool.
* To exit a sub-directory and return to the main dashboard, simply select option **`7`** or **`9`** (as marked by the navigation hints on your screen).

### 4. Inspect Session Activity Logs
* Every command, scanned target, and console output is recorded automatically in real-time.
* Look inside the dynamically created **`logs/`** folder right next to your script to review past clean-text session logs.
* Your local log assets are protected by `.gitignore` and will never be pushed to your public GitHub tree.

## 🛠️ System Architecture & Core Features

The framework is segmented into four distinct operational sub-directories to maintain an organized console real estate footprint and prevent menu overcrowding:

### 📡 Sub-Directory 01: Network Infrastructure & Endpoint Recon Cores
* **High-Speed Rainbow Echo Pinger:** A live ICMP latency stream engine that enforces strict text parsing to eliminate false-positive router gateway error replies.
* **Reverse DNS PTR Resolver:** Queries network name registries to reverse-map target IP addresses to their registered pointer profiles.
* **Multi-Threaded Port Scanner & Profiler:** Concurrently scans common service interfaces and returns a built-in cryptographic hardening and mitigation advice matrix for discovered open ports.
* **Local Subnet Ping Sweeper:** Maps out connected network device footprints in parallel using platform-native echo checks.
* **Application Banner Grabber:** Establishes direct TCP streams to inspect low-level software banners and protocol configurations.
* **DNS Reconnaissance Explorer:** Calls native address-info infrastructure to capture complex domain-to-IP path routing matrices.
* **Passive Subdomain Finder:** Passive discovery engine that crawls public distributed Certificate Transparency logs (`crt.sh`) without altering or alerting target servers.
* **Advanced RDAP Registrar Mapper:** Extracts autonomous network allocation block thresholds and administrative provider boundaries.

### 🔍 Sub-Directory 02: External OSINT & Target Profile Management
* **Sherlock Username Account Tracer:** Automated live shell subprocess hooks to track specific aliases globally across social platforms.
* **PhoneInfoga Telecom Target Scanner:** Launch mechanics targeting international mobile network records and footprint variables.
* **Holehe Email Platform Auditor:** Traces email account reset endpoints to isolate profile registrations across 120+ platforms.
* **Socialscan Concurrent Identity Profiler:** Concurrently verifies username and mail index availability.
* **Live Online Data Breach Explorer:** Leverages public privacy-respecting HTTPS APIs (`XposedOrNot`) to audit exposed email credentials safely.
* **Anonymized Password Exposure Auditor:** Natively processes plaintext strings into SHA-1 signatures to query `HaveIBeenPwned` via k-anonymity 5-character prefix ranges, keeping raw data hidden from the network.
* **Tor Exit Node Validator:** Cross-examines network addresses against real-time Tor project exit allocation manifests to flag anonymized incoming traffic paths.

### 🛡️ Sub-Directory 03: Local Data Traffic, Security Audits & Utilities
* **Inbound Network Packet Monitor:** Utilizes low-level raw sockets to capture and decode TCP, UDP, and ICMP protocol packets hitting active hardware interface cards.
* **Source Code Secret Leak Scanner:** Recursively crawls text files and developer code to locate hardcoded private keys, cloud credentials, or GCP/AWS API tokens using exact regular expressions.
* **Cryptographic Hash Signatures Matrix:** Generates SHA-256, SHA-1, and MD5 cleartext checksum check matrices, and analyzes unknown strings via bit-length format rules.
* **Host Operating System Telemetry Profiler:** Extracts live environment parameters, kernel compilation tags, hostnames, and primary adapter adapters natively.
* **Base64 Codec Processing Matrix:** Natively encodes or translates data strings cleanly inside the local terminal frame.
* **Automated Repository Distribution Blueprints:** Generates local markdown documentation and dependency requirements lists with a single menu toggle button.

### 📊 Sub-Directory 04: Advanced Infrastructure Audits & Integrity Cores
* **Local File Integrity Monitor (FIMS):** Captures recursive SHA-256 baseline snapshots of folder trees to identify and log unauthorized additions, deletions, or data modifications over time.
* **SSL/TLS Certificate & Cipher Suite Auditor:** Initiates secure socket layers to evaluate remote host certificate ownership, authority chains, and remaining expiration timelines.
* **Host Listening Port Profiler:** Directly queries kernel connection tables (`netstat` / `ss`) to display active local application listeners.
* **Password Complexity & Offline Entropy Scanner:** Calculates precise password bit-strength density using mathematical Shannon information entropy models completely offline.
* **ARP Cache Profiler & Duplicate MAC Auditor:** Calls native neighbor tables (`arp -a`) to analyze local MAC bindings, systematically alerting the console to duplicate hardware addresses which can indicate local configuration errors or spoofing behavior.

---

## 🔒 Session Privacy & Logging Mechanisms

This application features an unmanaged, automated **Thread-Safe Dual-Stream Intercept Logging Engine**. 
* **Automatic Creation:** Upon initialization, the script scans the working folder and natively spins up a local `/logs` folder.
* **Pristine Cleartext Exports:** Everything that prints to your console shell screen is instantly mirrored to a timestamped file (e.g., `logs/session_YYYYMMDD_HHMMSS.txt`).
* **ANSI Filtering:** To ensure professional log readability, an integrated regular expression engine systematically strips out raw layout color escape codes before flushing the text stream to the text file block.

### 🌍 Open Source Compliance & `.gitignore` Distribution

To ensure your private execution data, targets, and snapshot histories are never leaked to public version control trackers like GitHub, the repository blueprint engine automatically compiles a defensive `.gitignore` policy. 

This mechanism creates a hard boundary around the folder, ensuring that only the core application mechanics are committed to public trees:
