receiver.py

```python
#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, Raw, Ether
import gzip

def show_encapsulation(packet):
    print("packet:", packet)
    """
    Callback function that is called for each captured packet.
    It will parse and print the different protocol headers present.
    """
    print("=" * 60)

    # 1. Data Link Layer: Ethernet header
    if Ether in packet:
        ether_layer = packet[Ether]
        print("[Data Link Layer: Ethernet]")
        print(f"  - Src MAC: {ether_layer.src}")
        print(f"  - Dst MAC: {ether_layer.dst}")
        print()

    # 2. Network Layer: IP header
    if IP in packet:
        ip_layer = packet[IP]
        print("[Network Layer: IP]")
        print(f"  - Src IP: {ip_layer.src}")
        print(f"  - Dst IP: {ip_layer.dst}")
        print(f"  - TTL:    {ip_layer.ttl}")
        print()

    # 3. Transport Layer: TCP header
    if TCP in packet:
        tcp_layer = packet[TCP]
        print("[Transport Layer: TCP]")
        print(f"  - Src Port: {tcp_layer.sport}")
        print(f"  - Dst Port: {tcp_layer.dport}")
        print(f"  - Flags:    {tcp_layer.flags}")
        print()

    # 4. Application Layer: HTTP data
    #
    #   Often, HTTP data appears in the Raw payload (if it's not encrypted).
    #
    if Raw in packet:
        raw_data = packet[Raw].load
        # Try to decode as ASCII or UTF-8
        try:

            decoded_data = raw_data.decode('utf-8', errors='ignore')
        except UnicodeDecodeError:
            decoded_data = str(raw_data)

        # Check if it looks like HTTP
        if "HTTP" in decoded_data or "Host:" in decoded_data:
            print("[Application Layer: HTTP (Raw Data)]")
            print(decoded_data)

    print("=" * 60 + "\n")

def main():
    print("Starting HTTP sniffer... Press Ctrl+C to stop.")
    # Sniff only TCP traffic on port 80
    sniff(filter="tcp port 80", prn=show_encapsulation, store=False)

if __name__ == "__main__":
    main()

```

trigger.py
```python
import requests

response = requests.get("http://example.com")
print(response.status_code)
print(response.text[:200])  # Print first 200 chars
import requests

response = requests.get("http://example.com")
print(response.status_code)
print(response.text[:200])  # Print first 200 chars

```