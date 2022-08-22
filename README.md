# NETWORK-SCRIPT
<img src="https://img.shields.io/badge/LIB-scapy-brightgreen"> <img src="https://img.shields.io/badge/V-1.1-blue"> <br>
<b><i>This library has 3 types of scripts.. but it is based on using ARP (address resolution protocol) and its whites python scapy network library. This library has 3 types of scripts.. but it is based on using ARP (address resolution protocol) and its whites python scapy network library.</b></i>
## <a href="https://github.com/shalithamadhuwantha/Networks-scripts/tree/main/arp_spoofer">arp_spoofer</a>
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
