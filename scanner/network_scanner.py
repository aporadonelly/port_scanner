from scapy.all import ARP, Ether, srp, ICMP, IP, sr1
from scapy.error import Scapy_Exception
from scanner.logger import setup_logger
from colorama import Fore, Style, init

init(autoreset=True)

logger = setup_logger()


def arp_scan(subnet):
    logger.info(f"Starting ARP scan on {subnet}")
    try:
        arp = ARP(pdst=subnet)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=2, verbose=0)[0]

        active_hosts = []
        for sent, received in result:
            logger.info(f"Host {received.psrc} is up (MAC: {received.hwsrc})")
            active_hosts.append(received.psrc)
        return active_hosts
    
    except Scapy_Exception as e:
        logger.error("ARP scan failed due to permission error. Try running with sudo.")
        print(Fore.RED + "❌ ARP scan requires admin privileges. Please run with sudo.")
        return []

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
