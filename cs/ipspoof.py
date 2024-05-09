import requests
from scapy.all import send, IP, ICMP
import time

class IPSpoofer():
    def __init__(self):
        pass

    def _get_proxy(self):
        print("IP spoofing using proxy")
        proxy_list = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
        resp  = requests.get(proxy_list)
        if resp.status_code == 200:
            for proxy in resp.iter_lines():
                proxy_http = f"http://{proxy.decode()}"
                proxy_https = f"http://{proxy.decode()}"

                print("Checking proxy:", proxy_http)
                try:
                    check = requests.get("https://ipecho.net/plain", proxies={"http":proxy_http,"https":proxy_https}, verify=False, timeout=2)
                    if check.status_code ==200:
                        print("success")
                        print(f"\n***ip spoofed using proxy {proxy.decode()}***")
                except Exception as e:
                    pass


    def spoof(self,src, dst,):
        print("IP spoofing without using proxy")
        print("Ip Spoofing by changing source and destination ip in packet header")
        packet = IP(src=src, dst=dst) / ICMP()
        print(packet)
        print(f"packet created with source:{src} and destination {dst}")
        send(packet)
            


if __name__ == "__main__":
    spoofer = IPSpoofer()
    print("Spoofing by changing packet headers")
    spoofer.spoof("192.168.1.171", "192.168.1.182")
    print("sleeping for some time")
    time.sleep(10)
    print("Spoofing by using proxy")
    spoofer._get_proxy()
