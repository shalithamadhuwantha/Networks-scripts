#!/usr/bin/env python
import subprocess
import optparse
import re
print
print('EX:- sudo python mac.py -i eth0 -M 00:11:22:33:44:55' )
print
def parse_op():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface", dest="interface" , help="Interface to change its MAC address")
    parse.add_option("-M","--MAC", dest="new_MAC" , help="New MAC address")
    parse.add_option("-R","--RESET", dest="RESET_MAC" , help="Reset mac by default")

    (options,arg)=parse.parse_args()
    if options.RESET_MAC == None:
        if not options.interface:
            parse.error("[-] Please add an interface or type --help for more information")

        elif not options.new_MAC:
            parse.error("[-] Please add an new MAC or type --help for more information")

    return options

def mac_chang(newMac,interface):

    print("[+] change mac "+ interface + " to " + newMac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up" ])

def print_mac(interface,controler):

    if controler == 0:
        output= subprocess.check_output(["ifconfig", interface])
        regex_search= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
        if regex_search :
            return regex_search.group(0)
        else:
            print("[-]  Sorry, the MAC address could not be found")
    elif controler == 1:

        # output= subprocess.check_output(["ifconfig", interface])
        d= "ethtool -P "+str(interface)
        
        output = subprocess.check_output(d , shell=True)
        regex_search= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
        if regex_search :
            return regex_search.group(0)
            
        else:
            print("[-]  Sorry, the MAC address could not be found")

options = parse_op()

if options.RESET_MAC != None:
    current_mac= print_mac(options.RESET_MAC,0)
    print("[*] current MAC = "+str(current_mac))
    interfacer = options.RESET_MAC
    resr= "ifconfig "+interfacer+" hw ether $(sudo ethtool -P "+interfacer+" | awk '{print $3}')"
    subprocess.call(resr,shell=True)

    current_mac= print_mac(options.RESET_MAC,0)

elif options.RESET_MAC == None:
    current_mac= print_mac(options.interface,0)
    print("[*] current MAC = "+str(current_mac))
    mac_chang(options.new_MAC, options.interface)


    current_mac= print_mac(options.interface,0)
print("----------------------------------" )




if current_mac == options.new_MAC:
    print("[*] MAC change successful = "+str(current_mac))


elif options.RESET_MAC != None:
    defoult= print_mac(options.RESET_MAC,1)
    print("[*] MAC reset successful = "+str(defoult))
else:
    print("[*] MAC chnage NOT successfull")

