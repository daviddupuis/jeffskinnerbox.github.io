Title: WiFi (with WEP Security) on Raspberry Pi
Date: 2012-11-05 00:01
Category: Electronics
Tags: Raspberry Pi
Slug: wifi-with-wep-security-on-raspberry-pi
Author: Jeff Irland
Image: linux-wifi-logo.png
Summary: While I have seen many posting on how to configure the Raspberry Pi with WPA, there is oddly little information about WEP configrations.  Hopefully this posting will solve that problem for you.

<p>The Raspberry Pi Linux distribution I'm using is Adafruit's <a href="http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2">Occidentalis</a>.  It <a href="http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1#wifi-support">supports WiFi</a> out of the box and appears easy to configure.  But as noted by Adafruit, adding peripherals to the RPi may increase the loading on the power supply to your board and this, in turn, may affect the voltage presented to the RPi.</p>
<p>This is clearly the case, even for the tiny  OURlink WiFi (802.11b/g/n) USB Adapter (uses the <a href="http://www.realtek.com/products/productsView.aspx?Langid=2&amp;PNid=21&amp;PFid=48&amp;Level=5&amp;Conn=4&amp;ProdID=277">RTl8192cu chip</a> which is <a href="http://wiki.debian.org/rtl819x">supported by Debian Linux</a>) I purchased from <a href="http://www.adafruit.com/products/814">Adafruit</a>.  When I plugged it into the RPi, it became unstable and crashed.  Adafruit advises that you can over come this by attach the RPi's USB port to a powered hub.  (Note that all USB hubs aren't powered or powered sufficient, and therefore, not all are  <a href="http://elinux.org/RPi_VerifiedPeripherals">recommended</a>.  I used a Dynex 4 Port Hub with a 5V 2.1A power adapter and all seem fine.)  If you find using a using a USB hub completely unacceptable, you could make some <a href="http://theiopage.blogspot.com.au/2012/06/increasing-raspberry-pis-usb-host.html">RPi board modifications</a> to the <a href="http://elinux.org/Polyfuses_explained">polyfuses</a>, but this isn't the "official/supported" approach for this power problem .... but first .... see the <strong>Epilogue</strong> below.</p><h2>My First Attempt (Unsuccessful)</h2>
<p>Once I got the RPi USB port properly powered, I followed the Adafruit's <a href="http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1#wifi-support">instructions</a>.  I updated the<code>/etc/network/interfaces</code> file with the following:</p>

```
########## DID NOT WORK FOR ME ##########

# The loopback network interface
auto lo
iface lo inet loopback

# The primary (wired) network interface
iface eth0 inet dhcp

# The wifi (wireless) network interface
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
      wpa-ssid YOUR_SSID
      wpa-psk YOUR_WEP_KEY
```

<p>I ran  <code>ifconfig -a</code> and got the following:</p>
<p>
<center>
<a href="http://jeffskinnerbox.files.wordpress.com/2012/11/ifconfig-a.jpg"><img class="aligncenter size-full wp-image-574" title="ifconfig -a" alt="ifconfig" src="http://jeffskinnerbox.files.wordpress.com/2012/11/ifconfig-a.jpg" width="545" height="311" /></a>
</center>
</p>
<p>This tells me that Linux sees the WiFi device and assigned it device name <code>wlan0</code>. It also says there isn't an IP address assigned and no data is moving.  Appears that network interface <code>wlan0</code> isn't running so I tried bring it up with <code>sudo ifup wlan0</code> and I got the following:</p>
<p>
<center>
<a href="http://jeffskinnerbox.files.wordpress.com/2012/11/ifup-wlan0.jpg"><img class="aligncenter size-full wp-image-576" title="ifup wlan0" alt="wlan0" src="http://jeffskinnerbox.files.wordpress.com/2012/11/ifup-wlan0.jpg" width="545" height="311" /></a>
</center>
</p>
<p>No IP assigned ... now what?</p><h2>This Worked ... But</h2>
<p>After the typical thrashing about, it came to me that I'm not using WAP security (which is implied by the<code>/etc/network/interfaces</code> file content) but I'm using WEP.  I did some web searching and found a site that claimed to address <a href="http://www.gc-linux.org/wiki/WL:Wifi_Configuration">Debian WiFi WEP configuration</a>.  This provided me the needed command syntax for the solution.   I updated the<code>/etc/network/interfaces</code> file with the following:</p>

```
# The loopback network interface
auto lo
iface lo inet loopback

# The primary (wired) network interface
iface eth0 inet dhcp

# The wifi (wireless) network interface
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
       wireless-essid YOUR_SSID
       wireless-key YOUR_WEP_KEY
```


<p>I then ran <code>sudo ifup wlan0</code> to start the wireless networking (Note: you can use <code>sudo ifdown wlan0</code> to turn-off the wireless network).  This time DHCP discovery appeared to work.  I then ran <code>ifconfig -a</code> giving me the display below with an assigned wireless IP.</p>
<p>
<center>
<a href="http://jeffskinnerbox.files.wordpress.com/2012/11/ifconfig-a-this-time-it-worked.jpg"><img class="aligncenter size-full wp-image-585" title="ifconfig -a (this time it worked)" alt="it worked" src="http://jeffskinnerbox.files.wordpress.com/2012/11/ifconfig-a-this-time-it-worked.jpg" width="545" height="322" /></a>
</center>
</p>
<p>The wireless device now has an IP address and data seems to be flowing.  In an effort to further convince myself that the WiFi was working, I disconnected the wired ethernet connection and attempted to re-login in via <code>ssh -X pi@RedRPi.local</code>, over the wireless interface. This failed, giving the message:</p>

```
ssh: Could not resolve hostname RedRPi.local: hostname nor servname provided, or not known
```

<h2>Working For Sure</h2>
<p>I suspected (after more thrashing about) it was Ssh or <a href="http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-1#bonjour-support">Avahi/Bonjour</a> or both that was getting in the way.  So I did the following:</p><ol><ol><li>I cleaned out the <code>~/.ssh/known_hosts</code> file on the PC from which I'm accessing the RPi (I'm using Cygwin with Openssh). With the entries in the file removed  ssh keys would need to be recreated on next login.</li><li>I then logged into the RPi in via <code>ssh -X pi@RedRPi.local.</code> The login created an entry the <code>~/.ssh/known_hosts</code> file on the PC.</li><li>Using vi, I edited the  <code>~/.ssh/known_hosts</code> file.  I duplicated the one existing record but changed the  IP address to the wireless address.</li><li>I restarted the openssh on the PC.  (I terminated all the Cygwin window and restarted them.  I could get anything else to work short of a PC reboot).</li><li>I then logged in using <code>ssh -X pi@192.168.1.7</code>. Now I'm wireless!!</li></ol></ol>
<p>My <code>~/.ssh/known_hosts</code> file looks like this:</p>
<p>
<center>
<a href="http://jeffskinnerbox.files.wordpress.com/2012/11/known_hosts.jpg"><img class="aligncenter size-full wp-image-594" title="known_hosts" alt="known hosts" src="http://jeffskinnerbox.files.wordpress.com/2012/11/known_hosts.jpg" width="545" height="300" /></a>
</center>
</p><h2>Epilogue</h2>
<p>I have found that if  I don't use a USB  powered hub and I plug in the OURlink WiFi (802.11b/g/n) USB Adapter while the RPi is up and running, the RPi will crash.  The good news is that, once the RPi reboots, it runs fine without the powered hub.</p>
<p>So, go ahead and use the WiFi USB Adapter, without the powered hub, but make sure the adapter is plugged in when you boot up .... problem solved!</p>
