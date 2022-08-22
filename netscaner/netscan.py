
# running auth test 
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
import optparse

def options():
    parse = optparse.OptionParser()
    parse.add_option("-t","--target", dest="target" , help="type your target ip and range \n EX: 192.168.168.0\\24")

    (options,arg)=parse.parse_args()
    
    if not options.target:
        parse.error("[-] Please add an targert IP or type --help for more information")
        

    return options

def scan(ip):
    # scapy.arping(ip)
    print(ip)
    arp_msg = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_msg
    avalable_device=scapy.srp(arp_broadcast,timeout=2) [0]
    # print(avalable_device.summary())
    print("{} IP \t\t\t MAC".format('\033[0m'+'\033[01m'))
    print("----------------\t\t-----------------{}".format('\033[36m'+'\033[01m'))
    for packet in avalable_device:
        # print(packet[1].show())
        print(packet[1].psrc +'\t\t'+packet[1].hwsrc)




print('\033[36m'+'\033[01m')
# scan("192.168.43.0/24")
target_ip=options().target
scan(target_ip)