# scanner/network_scanner.py
from scapy.all import ARP, Ether, srp, ICMP, IP, sr1
from scanner.logger import setup_logger

logger = setup_logger()

def arp_scan(subnet):
    logger.info(f"Starting ARP scan on {subnet}")
    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=0)[0]

    active_hosts = []
    for sent, received in result:
        logger.info(f"Host {received.psrc} is up (MAC: {received.hwsrc})")
        active_hosts.append(received.psrc)
    return active_hosts

def icmp_scan(subnet):
    from ipaddress import ip_network
    logger.info(f"Starting ICMP scan on {subnet}")
    active_hosts = []

    for ip in ip_network(subnet).hosts():
        pkt = IP(dst=str(ip))/ICMP()
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp:
            logger.info(f"Host {ip} is up (ICMP reply)")
            active_hosts.append(str(ip))
    return active_hosts
