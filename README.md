## Wi-Fi Probe Request Sniffer (Python)

This Python script utilizes Scapy to identify nearby Wi-Fi networks by capturing and filtering probe request packets.

**Features:**

- Detects and displays network names (SSIDs) from probe requests.
- Stores unique network names in a set to avoid duplicates.
- Provides a user-configurable interface name and timeout duration.

**Dependencies:**

- This project requires the `scapy` library. Install it using `pip install scapy`.

**Usage:**

1. Clone this repository.
2. Open a terminal and navigate to the project directory.
3. (Optional) Edit the following in `wifi_sniffer.py` to customize:
   - `interface` (default: 'wlan4'): Specify your Wi-Fi interface name (e.g., 'wlp3s0').
   - `timeout` (default: 60 seconds): Set the duration for sniffing packets before exiting.
4. Run the script using `python wifi_sniffer.py`.

**Example Output:**

```
[+] Detected New Probe Request from: MyHomeNetwork
[+] Detected New Probe Request from: MyNeighbor's_WiFi
[+] Detected New Probe Request from: Guest_Access (timeout reached)
```

**Disclaimer:**

- Wi-Fi network sniffing can have legal implications depending on your location and the networks you target. **Always ensure you have permission to sniff traffic on a network before proceeding.**
- This script is intended for educational purposes and network discovery. Do not use it for malicious activities.

**Contributing:**

Feel free to fork this repository and make improvements! Here are some ideas:

- Implement filtering based on additional Wi-Fi packet information (e.g., signal strength).
- Add a visual representation of detected network strength (optional).
- Allow customization of the output format (e.g., saving to a file).

**Security Considerations:**

- Be aware that sniffing Wi-Fi traffic can reveal network information. Use this script ethically and responsibly.
- Consider using a network monitor tool with advanced features for more comprehensive network analysis.
