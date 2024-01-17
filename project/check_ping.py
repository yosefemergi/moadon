import os

def check_ping(ip):
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        return True
    return False    
def scan_network(network_prefix):
    for num in range (1, 255):
        active_ips = []
        ip = "{}.{}".format(network_prefix, num)
        if check_ping(ip) == True:
            active_ips.append(ip)
    return active_ips                                                                                    

network_prefix = "192.168.1"    
active_host =scan_network(network_prefix)
print(active_host)
         