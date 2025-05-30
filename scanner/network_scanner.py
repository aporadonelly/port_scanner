# pylint: disable=missing-module-docstring
from ipaddress import ip_network
from colorama import Fore, init
from scapy.all import ARP, Ether, srp, ICMP, IP, sr1 # pylint: disable=no-name-in-module
from scapy.error import Scapy_Exception
from scanner.logger import setup_logger

init(autoreset=True)

logger = setup_logger()


def arp_scan(subnet):
    """Performs an ARP scan to discover active hosts in the given subnet."""
    logger.info("Scanning %s...", subnet)
    try:
        arp = ARP(pdst=subnet)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=2, verbose=0)[0]

        active_hosts = []
        for _, received in result:
            print(_)
            # logger.info(f"Host {received.psrc} is up (MAC: {received.hwsrc})")
            logger.info("Host %s is up (MAC: %s)", received.psrc, received.hwsrc)
            logger.info("Host %s...", received.psrc, )

            active_hosts.append(received.psrc)
        return active_hosts

    except Scapy_Exception as e:
        logger.error("ARP scan failed: %s", e)
        print(Fore.RED + "❌ ARP scan requires admin privileges. Please run with sudo.")
        return []




def icmp_scan(subnet):
    """Sends ICMP echo requests to hosts in the subnet and logs responsive IPs."""
    logger.info("Starting ICMP scan on %s", subnet)
    active_hosts = []

    try:
        for ip in ip_network(subnet).hosts():
            pkt = IP(dst=str(ip)) / ICMP()
            resp = sr1(pkt, timeout=0.3, verbose=0)  # ⏱️ reduced timeout
            if resp:
                logger.info("Host %s is up (ICMP reply)", ip)
                active_hosts.append(str(ip))

    except (PermissionError, Scapy_Exception) as exc:
        logger.error("ICMP scan failed: %s", exc)
        print(Fore.RED + "❌ ICMP scan requires admin privileges. Please run with sudo.")
        return []

    return active_hosts
