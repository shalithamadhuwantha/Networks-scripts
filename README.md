# NETWORK-SCRIPT
<img src="https://img.shields.io/badge/LIB-scapy-brightgreen"> <img src="https://img.shields.io/badge/V-1.1-blue"> <img src="https://img.shields.io/badge/license-GPL--3.0%20license-red">  <img src="https://img.shields.io/badge/python-2.7-blue">  <img src="https://img.shields.io/badge/python-3.0<~-blue"><br>
<b><i>This library has 3 types of scripts.. but it is based on using ARP (address resolution protocol) and its whites python scapy network library. This library has 3 types of scripts.. but it is based on using ARP (address resolution protocol) and its whites python scapy network library.</b></i>
### You can run all these scripts in version 2.7 or 3.0 later
## <a href="https://github.com/shalithamadhuwantha/Networks-scripts/tree/main/arp_spoofer">arp_spoofer</a>
<img src="https://img.shields.io/badge/python-2.7-red">
<P>This is based on the <b>ARP protocol </b> .. it is created using python scapy framework ...But after running this script your victim computer's internet connection will stop ... But you can turn on IP forwarding of your hacker computer and you can solve this problem.👇</p>




Type in your root linux terminal: 
```
# echo 1 >/proc/sys/net/ipv4/ip_forward 
```
This script helps to replace your victim machine router mac address with our hacker machine mac address

You can see your arp table using this cmd: 
```
# arp -a
```
<p>You should change your script ip address in line 39 and 40 👇</p>
<img src="https://github.com/shalithamadhuwantha/Networks-scripts/blob/main/img/arp.PNG">

## <a href="https://github.com/shalithamadhuwantha/Networks-scripts/tree/main/mac_change">MAC_changer</a>
<img src="https://img.shields.io/badge/python-2.7--3.0%3C~-red">
<p>There is a utility to change the Mac address of your Linux machine</p>

Use this structure👇: 
```
# sudo python mac.py -i <interface> -M <mac add>
```



for example👇: 
```
# sudo python mac.py -i eth0 -M 00:11:22:33:44:55
```

Reset your Mac👇:
```
# sudo python2 mac.py  -R <interface>
```

Reset your Mac EX👇:
```
# sudo python2 mac.py  -R eth0
```

## <a href="https://github.com/shalithamadhuwantha/Networks-scripts/tree/main/netscaner">NetworkScanner</a>
<p>You can get a list of all the devices on your networ</p>

run this script👇:
```

# sudo python2 netscan.py -target 192.168.43.0\24
```
