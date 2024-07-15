from scapy.all import *
interface = 'wlanX'  # Replace with your network interface
probReqs = set()
timeout = 60  # seconds

def sniff_packets(p):
    if p.haslayer(Dot11):
        netname = p.getlayer(Dot11).info.decode('utf-8')
        if netname not in probReqs:
            probReqs.add(netname)
            print('[+] Detected New Probe Request from:', netname)

sniff(iface=interface, prn=sniff_packets, store=False, timeout=timeout)