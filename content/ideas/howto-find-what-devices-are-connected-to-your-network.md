Title: HowTo: Find What Devices Are Connected to Your Network
Date: 2100-01-01 00:00
Category: Software
Tags: nmap
Slug: howto-find-what-devices-are-connected-to-your-network
Author: Jeff Irland
Image: DRAFT_stamp.png
Summary: bla bla bla

WiFi networks are desirable target for wannabe hackers.
Ever wondered if someone might be taking advantage of your WiFi network?
I do.
An easy way to scan your network to see what device are connected is to use `[nmap][01]`.
With this you can find out if some unknown or unwanted device is connected to it.

Despite its popularity as a utility for network discovery and security auditing,
`nmap` isn't part of the base install for Ubuntu.
To install it, just do

    sudo apt-get install nmap

To begin your scan using `nmap -sP`,
which will run a ping scan on the specified network.
For instance, `nmap -sP 192.168.1.0/24` will scan the 256 hosts from
192.168.1.0 through 192.168.1.255 to see if they're available, and report back.

    sudo nmap -sP 192.168.1.0/24

check to see what services are running on a box

    sudo nmap -sV 192.168.1.1

* [Find What Devices Are Connected to Network In Ubuntu](http://itsfoss.com/how-to-find-what-devices-are-connected-to-network-in-ubuntu/)
* [Wi-Fi on the Command Line](http://www.linuxjournal.com/content/wi-fi-command-line)
* [ Who is on my wifi?](http://forum.backbox.org/general-support/who-is-on-my-wifi/)
* [WiFinder is a Python Driven Roommate Warning System](http://hackaday.com/2014/06/28/wifinder-is-a-python-driven-roommate-warning-system/)

* [7 Things Wi-Fi Hackers Hope You Don't Know](http://www.nowiressecurity.com/articles/things_wi-fi_hackers_hope_you_dont_know.htm)
* [First Linux Release of Wi-Fi app inSSIDer Available to Download](http://www.omgubuntu.co.uk/2011/01/wi-fi-app-inssider-2-linux-alpha-released)

# Nmap
* [Beginner's Guide to Nmap](http://www.linux.com/learn/tutorials/290879-beginners-guide-to-nmap)
* [Top 30 Nmap Command Examples For Sys/Network Admins](http://www.cyberciti.biz/networking/nmap-command-examples-tutorials/)
* [Nmap Cheat Sheet](https://blogs.sans.org/pen-testing/files/2013/10/NmapCheatSheetv1.0.pdf)
* [Nmap Referasnce Guide](http://www.bandwidthco.com/whitepapers/netforensics/recon/nmap/NMAP%20Reference%20Guide.pdf)
* [NMAP - A Stealth Port Scanner](http://www.csc.villanova.edu/~nadi/csc8580/S11/nmap-tutorial.pdf)

# Zenmap
* [Zenmap](http://nmap.org/zenmap/)
* [An introduction to using Zenmap on Linux](http://www.maketecheasier.com/using-zenmap-on-linux/)
* [Zenmap Tutorial: Audit Your Networks using Nmap GUI](http://www.linux.com/learn/tutorials/381794-audit-your-network-with-zenmap)

# Kismet
* [How to use Kismet: A free Wi-Fi network-monitoring tool](http://searchsecurity.techtarget.com/video/How-to-use-Kismet-A-free-Wi-Fi-network-monitoring-tool?videoId=8eb0fc2d1aa26410VgnVCM1000000d01c80aRCRD)




[01]:http://www.linux.com/learn/tutorials/290879-beginners-guide-to-nmap
[02]:
[03]:
[04]:
[05]:
[06]:
[07]:
[08]:
[09]:
[10]:
