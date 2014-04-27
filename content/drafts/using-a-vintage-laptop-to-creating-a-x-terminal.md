Title: Using a Vintage Laptop to Creating a X Terminal
Date: 2100-01-01 00:00
Category: Software
Tags: Linux
Slug: using-a-vintage-laptop-to-creating-a-x-terminal
Author: "Jeff Irland"
Image: DRAFT_stamp.svg
Summary: bla bla bla
Status: draft

On a whim, I visited a web aution site dealing in surplus government property. 
I spotted two old laptops, which claimed to be still operational,
and I place a bid of $40.
A few days later, I recieved an email saying I was the proud owner of two 
Hp Omni Book XE3 loaded with a Celeron[^A] 32bit processor!
By todays standards, the Hp Omni Book XE3 isn't exactly a race horse with its
1066 MHz clock, 128M of RAM running at 100 MHz, and 10/100 Ethernet LAN communications.
These laptops date back to 2000, the early days of the internet,
and are unashamedly equiped with a builtin phone jack / modem, [PCMCIA card slots][20],
a 1.44-MB floppy disk drive, and proudly hosting Microsoft Windows 98 Second Edition!
Here is a more complete discription of the laptops:

[^A]
    Celeron is a brand name given by Intel Corp. to a number of different microprocessor models
    targeted at budget personal computers.
    [Introduced in April 1998][09], the first Celeron branded CPU was based on the Pentium II branded core.
    Subsequent Celeron branded CPUs were based on the Pentium III, Pentium 4, Pentium M,
    and Intel Core branded processors. 
    With Damn Small Linux loaded and running `cat /proc/cpuinfo`,
    it shows the processor is of Intel cpu family 6 and model 11.
    This maps to Intel product code 80530, which [makes it a Pentium III (codename Tualatin)][10].

| Feature | Description|
|:------:|-----|
| CPU | 1066-MHz Intel Mobile Celeron processor |
| Cache	| 128KB internal L2 cache, 32KB internal L1 cache |
| Memory | 128MB of 100MHz SDRAM standard (PC100), 512MB maximum system memory (two slots available only for memory modules)(144-pin/3.3V; 1.25-in slots) |
| Mass Storage | 10GB Enhanced-IDE hard drive, Built-in 3.5-inch 1.44-MB floppy disk drive, Built-in 24X maximum-speed CD-ROM drive |
| Display | 13.3-inch diagonal 1024 × 768 XGA TFT display with 16 million colors |
| Video | S3 Savage/1X graphics controller, 2X AGP graphics, 128-bit single-cycle 3D architecture video graphics controller, 8MB of embedded video SGRAM, external video resolutions/maximum colors/refresh rates: 800 × 600/16M colors/85Hz, 1024 × 768/16M colors/85Hz, 1280 × 1024/16M colors/85Hz, 1600 × 1200/64K colors/85Hz |
| Audio | 16-bit Sound Blaster Pro–compatible stereo sound (ESS Allegra), Stereo sound via headphone-out, microphone-in port, Polk Audio speakers, 3D-enhanced PCI bus audio, Supports CD-play while system is off, Built-in microphone |
| Ports | Two Universal Serial Bus (USB) ports, Serial port: 9-pin, 115,200 bps, Parallel port: 25-pin bi-directional ECP and EPP, 4-Mbps IrDA-compliant infrared port, PS/2 keyboard/mouse port, VGA: 15-pin, Composite TV-out, RJ-11 modem jack, RJ-45 jack, Headphone-out, microphone-in ports |
| Communications | Integrated 56Kbps, v.90-compatible, worldwide capable modem + 10/100 LAN combo |
| Power | Universal AC adapter: 100 to 240 Vac input; 19-Vdc, 3.16-A output, Built-in rechargeable 9-cell Lithium-Ion battery (with up to 4-hour run time) |
| PC Card Slots | One Type III or two Type II PC Card slots, CardBus-enabled (TI 1420) |
| Weight | 7.2lb with 13.3-in display |
| Dimensions | 13.03 × 10.76 × 1.59in |
| Operating System | Microsoft Windows 98, Second Edition |

The installed 10G drive was wiped clean but the laptops did come with the orginal recovery disk.
Using the recovery disk, I quickly got the Microsoft Windows 98 operating system installed.
There was no login prompt / password required ... wow.
I activated the browser, that being Microsoft Internet Explorer 6.0.
During the activation, it asked if I wished to access the Internet via a modem ... Ahhhh, no. 
Initially, this old browser only partly worked.
I then set it to accept all cookies and it behave much better and was usable,
but it would hang sometime and it wasn't at all pretty.

With the browser and the slow internet connection,
I figured that I could then down load the Linux distribution that I need, and boot it from the disk.
My plan is to get a light-weight Linux distro installed and use it as X server with my desktop
Linux system as its X client, aka X Terminal[^B].
I choose [Lubuntu][04] as my Linux distro.
The [alternate version of Lubuntu][05] is for computers with less than 700 MB of RAM,
so I'm hoping it will do the job.
It may not be the lightest Linux distribution but I'm currently using Ubunutu,
I'm happy with it, and I figured I'll stick will the fimiluar.

[^B]
    Generally, a [X Terminal][22], a predecessor to todays [thin client][23], is a low-powered,
    diskless, quieter, and more reliable than desktop computers
    because they do not have any moving parts.
    I can't say this about this vintage laptop.

What I shortly discovered is that the antique hardware and OS (Microsoft Windows 98)
got in the way.
All the method I tryed to install Lubuntu ran into walls.
First, the [ISO image][06] was to large to burn to a CD-ROM, it required a DVD,
but this old laptop isn't DVD equiped.
Booting the ISO from a USB thumb drive wasn't posible with the laptop BIOS.
When I attempted to load the ISO image from the hard disk using methods found at
[Downloading Lubuntu 13.10][01], [Installing Lubuntu][03], and [Installation/FromWindows][02],
I found that tools and methods wouldn't work within Windows 98.

# Test Light-Weight Linux Distrabutions
I concluded that it would be best to burn the Linux distro onto a CD-ROM using
my curent desktop computer and boot the laptop with the CD-ROM as a [live system][18].
My desire is to use Lubuntu, but give the limitations of this laptop,
I'll also try out Damn Samll Linux (DSL), Puppy Linux, and Tiny Core Linux.

## Installing Damn Small Linux (DSL)
As my first trial, I choose to install [Damn Small Linux (DSL)][07].
DSL (based on the Debian distro)[^C] was released in 2003 to specifically create a
Linux operating system for [older hardware][08].
DSL supports older machines with minimal memeory by disables all unnecessary daemons or services.
It gives you a tool to directly manage daemons,
and bundled applications were chosen specifically for their stingy resource use.
DSL was designed, tested, and runs on old computers by retains support for many old devices. 

[^C]
    Damn Small Linux also uses by default [Busybox][11].
    BusyBox provides several stripped-down Unix tools in a single executable file. 
    Its originally aim was to provide a complete bootable system on a single floppy
    that would serve both as a rescue disk and as an installer for the Debian distribution.
    Busybox's use now is more focused on embedded operating systems with very limited resources.

The installation of DSL on the laptop happend without any difficulties.
I followed the excellent instructions give in the article
[How to Download and Install DSL Linux][13].
Every thing came up nicely.

But there are problems.
A major short coming of this distro is that
DSL development seemed to be at a [standstill for a long time][19].
This, and the fact that I can't find much documentation on how to support WiFi with DSL,
gives me major concerns about using it.
Never the less, the good news is that
I now know I can get some version of Linux operational on this old laptop.

## Installing Lubuntu
My next test install was [Lubuntu][04].
The article [Lubuntu: Finally, a Lightweight Ubuntu][12]
claims that Lubuntu has snappy responsiveness on older computers.
This seems to be dependent on having a Pentium III processor
and 128M or more of memory.
This laptop seems to just meet this critera and so I pushed forward.

I down loaded the Alternate version of Lubuntu from the site
[Lubuntu Alternate ISOs for low-RAM PCs][05], created the CD-ROM, and booted the laptop with teh CD-ROM.
The install started smoothly but slowed down and took man hours ... bad sign.
Once installed, it hung during boot up.
Looks like Lubuntu is out of the running.
It appears the 128M of RAM is just too small for Lubuntu.

## Install Puppy Linux
[Puppy Linux][21] is a popular light-weight Linux distro.
I successfully installed Puppy Linux, but once installed,
it perfromed badly when I fired up applications like a browser.
A closer reading of the Puppy Linux documentation informed me that
the Linux Kernal is going to require 100M of RAM.
So any reasonable size application will cause performance problems.

## Installing Tiny Core Linux (TCL)
[Tiny Core Linux (TCL)][14] comes in three ISO images, include CorePlus which is the installation image I required.
I download the CorePlus, image, burned it to a CD-ROM, booted it,
and selected "`Boot Core with X/GUI (TineCore) + Installation Extentions`" from the boot menu. 
This will enable you to perform a hard drive install of TCL.
See [Tiny Core Linux installation documentation for procedures][15].
(You can also do a [manual install][16],
or at least reformat the disk, if you boot directory is screwed up form previous installs.)

DON'T INSTALL WIFI OR FIRMWARE HERE.
CorePlus Installation Options: _none_

reboot

TCL install without a hitch and ran very nicely.
It has a very smaller RAM footprint like DSL but is actively supported,
well documented, includeing a book call [Into the Core: A look at Tiny Core Linux][26].
Given all this, TCL seems like a good choose for my X Terminal plans.

# Establishing the TCL Operating System
Install the WiFi adapter and plugin Ethernet cable

So it appears that Tiny Core Linux (TCL) will be my best choose for this vintage laptop conversion into a X Terminal.
Like Damn Small Linux, [Tiny Core Linux (TCL)][14] is a minimal Linux operating system
initially using [BusyBox][11] as its core system,
but latter replace with [GNU's Coreutils][17].
Tiny Core is exactly what the name suggests,
a tiny core of an operating system which boots to a fully functional graphics desktop
called [Fast Light Toolkit (FLTK)][25], pronounced "fulltick".

Tiny Core is designed to run from a RAM copy created at boot time.
Besides being fast, this protects system files from changes and ensures a pristine system on every reboot.
Easy, fast, and simple renew-ability and stability is a principle goal of Tiny Core. 
The core system provides most of what you need for a working environment,
which they can then tweak from there via applications.
The vidoe provides an excelent but quick into to [Tiny Core Linux File Architecture and Boot Process][24].

Once TCL is booted, the user is then able to connect to the online repositories
in order to install the applications they desire and configure their system.
TCL has a very simple package manager that provides a list of available packages to install.
The user need only select a package and the manager will download it with all
required dependencies and install them to the system.

[Tiny Core: The Little Distro That Could](http://www.linux-mag.com/id/7457/)

TLC's package manager, the `Apps` tool, has several methods of installing applications.
OnBoot
:   This is the default method. This extension will be installed,
    and added to the onboot list, to be mounted on the following boots. 
OnDemand
:   A loading script will be generated for this extension.
    Instead of being loaded on boot, the icon/menu entry for this extension
    will load the extension when you first need it.
    This option speeds up your boot time, at the cost of making the first start of the application slower.
Download + Load
:   The extension will be downloaded and installed for this session only.
    It will reside within the directory sytem,
    but since it is not added to the onboot list, it will not be loaded after a reboot.
Download Only
:   The extension will only be downloaded, nothing more will be done.

# Tiny Core Linux With WiFi
Install the following extensions via TCL `Apps` application (OnBoot):

* usb-utils.tcz

Now lets detect the type of WiFi USB Adapter that is plugged into the Laptop.
In my case, this WiFi Adapter is detected via `lsusb` as

* **USB ID** = 0bda:8176
* **Description** = Realtek Semiconductor RTL8188CUS 802.11n WLAN Adapter

The USB ID is listed as one of the [Tiny Core Linux supported WiFi chips][28].
Knowing this, we can install the suite of applications and firmware required to get the WiFi Adapter operational.
I install the following extensions via TCL `Apps` application (OnBoot):

* firmware.tcz
* firmware-rtlwifi.tcz
* wl-r8192cu-3.8.13-tinycore.tcz
* wifi.tcz

Now pull the Ethernet connection, reboot, and try out the WiFi.

wifi.db in home directory

* openssh.tcz
configure files in /usr/local/etc/ssh

[no wireless extensions using usb-wlan adapter with chipset rtl8192cu ](http://forum.tinycorelinux.net/index.php?topic=15535.0)

[List of Supported Wifi Devices](http://wiki.tinycorelinux.net/wiki:list_of_supported_wifi_devices)
[Setting Up WiFi](http://wiki.tinycorelinux.net/wiki:setting_up_wifi)
[How to get wireless working when no other network access is available](http://tinycorelinux.net/4.x/armv7/README/README-wifi.txt)

# [The X Environment][^D]
[^D]
    A typical X Window System implementation consists of the following compoents:
    * **X Window System (aka X, X11, X-Windows)** - [X Window System][38] provides the basic [framework, primatives, and protocals][42]
    for a graphical user interfacea (GUI) environment.
    X does not mandate the user interface — this is handled by individual programs.
    As such, the visual styling of X-based environments varies greatly;
    different programs may present radically different interfaces.
    There are several implementation of X, including [X.Org][40], [XFree86][39], [ Cygwin/X][41], and many more.
    * **X Server (aka X Display Server)** - This creates the graphical environment on a graphical display device using the X Display Protocol.
    An X server program runs on a computer with a graphical display and communicates with various X client programs. 
    * **X Client (aka X Application)** - An X client is an application program that displays on an X server
    but which is otherwise independent of that server.
    X clients are built using software libraries that support the X Window System framework.
    * **X Window Manager** - The window manager takes care of deciding the position of windows,
    placing the decorative border around them, handling icons,
    handling mouse clicks outside windows (on the “background”), handling certain keystrokes, etc.
    Examples are WindowMaker, sawfish, fvwm
    * **X Session Manager** - The session Manager automatically starts a set of applications, setting up,
    and restoring a working desktop environment.
    More precisely, it is the set of applications managing these windows
    and the information that allow these applications to restore the condition
    of their managed windows if required.
    The X session manager saves and restores the state of sessions.
    * **X Display Manager (aka Login Manager)** - This program shows the graphical login prompt in the X Window System.
    This is the first X program run by the system if the system (not the user)
    is starting X and allows you to log on to the local system, or network systems.
    More generally, a display manager runs one or more X Servers on the local computer
    and accepts incoming connections from X servers running on remote computers.
    The local servers are started by the display manager,
    which then connects to them to present the user the login screen.
    * **Desktop Environment** - A desktop environment such as LXDE, XFCE, KDE or GNOME are a suite of
    applications and configuration files designed to integrate the X Window System compoents
    to provide a consistent experience.

As stated earlier, my objective is to use the TCL laptop as a
[X Terminal][22] with my desktop Linux as the remote system.
Starting an X session is typically done in one of two ways:

1. The X session is started via a [X Display Manager][27], and the user logs in at a GUI screen.
2. The user starts X manually after logging in to a text console. This is typically done with the `startx` command, which is a simple shell script wrapper for `xinit`.

X runs with root privileges in either case, since it needs raw access to hardware devices.
In the X Window System,
The X Display Manager runs as a program that allows the starting of a session
on an X server from the same or another computer.
A display manager presents the user with a login screen which prompts for a username and password.
A session starts when the user successfully enters a valid combination of username and password.
The X Display Manager function was established, in part, to support standalone X Terminals.

A display manager can run on the local computer where the user sits or on a remote one.
WHen local, the display manager starts one or more X servers,
displaying the login screen.
When the display manager is remote, the display manager works according to the
X Display Manager Control Protocol (XDMCP)[^E].
Unlike [vncviewer][31] that just duplicates the current screen on a remote system,
XDMCP allows several different users to login and run different X sessions at the same time.

[^E]
    XDMCP is inherently insecure as it does not encrypt your traffic.
    Therefore, only use XDMCP on a wired network that you you trust. Also,
    consider using alternatives that feature security (and often compression) such as [FreeNX][35].
    XDMCP also uses a large amount of bandwidth because it uses no compression.
    A 100mbit (wired) network may be necessary.
    However, the lack of compression can make XDMCP provide very fast graphics when the bandwidth is available.

The XDMCP protocol mandates that the X server starts autonomously and connects to the display manager.
You configure an XDMCP Chooser program running on the local computer (or X Terminal)
to connect to a specific remote X Display Manager
or to display a list of suitable hosts that the user can choose from. 
When the user selects a host from the list,
the XDMCP Chooser running on the local machine will send a message
to the selected remote computer's display manager
and instruct it to connect the X server on the local computer or terminal.

If your Linux box boots into a graphical login screen,
you already are running a display manager. 
So you know that TCL isn't using a X Display Manager,
but my desktop Linux system is.
Specifically, its using `lightdm`
(you can determine this by running `cat /etc/X11/default-display-manager`
or `ps -A | grep dm`).

For my [desktop environment][43], I'm using Unity
Lightweight X11 Desktop Environment (LXDE).
It consits of:
Window Manager
:   Openbox, the default window manager of LXDE
Display Manager
:   lxdm is the disaplay manager for LXDE
Session Manager
:   [LXSession][37] is the standard session manager used by LXDE
    and it's desktop-independent and can be used with any window manager.


What is happending when you start up Unity?
The following is an abrivated [summary of startup activites][44].

1. The kernel starts the `init` process as process number 1, and it is responsible for starting all other processes.
2. `init` starts the LXDE Display Manager `/usr/sbin/lightdm` fairly late in the init process (the system dbus, filesystem and the graphics display system all must be ready).
3. `lightdm` creates an xauthority file and then starts X, starting it on virtual terminal 7
4. `unity-greeter` get's the names of potential Window Managers `/usr/share/xsessions/*.desktop`.
5. Once logged in, the `.desktop` files from `/usr/share/xsessions/*.desktop` now determine the rest of the startup sequence.
6. The `/usr/sbin/lightdm-session` shell script is run with the arguments `gnome-session --session=ubuntu`
7. `/usr/sbin/lightdm-session` then runs `$HOME/.profile`, loads `$HOME/.Xresources`, `$HOME/.Xmodmap`, runs scripts in `/etc/X11/xinit/xinitrc.d`, runs the Xsession scripts in `/etc/X11/Xsession.d/*`, using the options in `/etc/X11/Xsession`.options.
8. `lightdm-session` starts a Window Manager, or for Unity, starts the `gnome-session` Session Manager. The Window Manager uses the Unity `/usr/share/xsessions/ubuntu.desktop` configuration file.
9. `gnome-session` starts the specified program from `/usr/share/gnome-session/sessions/` and starts applications from `~/.config/autostart/` and `/etc/xdg/autostart`.

* [Running X](http://www.tldp.org/HOWTO/XWindow-User-HOWTO/runningx.html) - see the section on Display Manager if you need to run with X Terminal that has a different resolution.
[Linux-Based X Terminals with XDMCP](http://www.linuxjournal.com/article/6713)
[Linux-Based X Terminals with XDMCP](http://blog.joseluisperezdiaz.com/linux-based-x-terminals-with-xdmcp/)

[XDM and X Terminal mini-HOWTO](http://www.linuxdoc.org/HOWTO/XDM-Xterm/index.html)
[Linux XDMCP HOWTO](http://www.tldp.org/HOWTO/XDMCP-HOWTO/)

# Establishing the X Terminal Environment
There are a few ways to run X windows applications remotely
(i.e. running an X Windows application on a remote computer and having the graphical part show up on your local computer).
For something quick, use the [SSH method][34] in an `xterm` window:

```
ssh -X login@remote-computer
```

This will give a terminal session within the `xterm` window on the remote computer.
The `-X` switch says to export graphics from the remote computer (remote-computer)
to the computer you at actually sitting on (i.e. the local-computer).
For many uses, this works fine, but it doesn't give you the full login experiance on the remote computer.
Specifically, the desktop is still the local computer,
so picking any desktop icon or menu will result in a local X client.
This isn't what I want ... I want access to the remote desktop.

To do this, you could leverage the [Linux Terminal Server Project (LTSP)][29]
[Sterminal][30], or even consider [Virtual Network Computing (VNC)][31],
but these have too heavy a memory footprint for the vintage laptop I'm using.
And in the case of VNC, your really sharing an existing screen, not creating a new session.
I'll need to use the less secure classical method of using XDMCP.
Basically, on the remote computer (remote-computer)
I need to be running a special daemon that answers requests to login from a X Server.
To establish this, I'll need to do the following:

**On the remote computer**
:   Configure the Display Manager to accept logins from a remote X Server

**On the local computer**
:   Configure the local Display Manager to use the remote Display Manager. This amounts to configuring the Display Manager to run "XDMCP Chooser". 
    An alternative is to establish a X session and then log into the remote via [`Xnest`][32]. Xnest can be used to locally display the desktop of a remote computer.

### Configuring Remote Computer (Ubuntu Desktop)
On the remote-computer (in my case, a Ubuntu desktop runing `lightdm` Display Manager),
you need to tell the Display Manager to accept logins from a remote X Server.
This is easily done by configuring the file `/etc/lightdm/lightdm.conf` so it contains 

```
[SeatDefaults]
user-session=ubuntu
autologin-user=false
xserver-allow-tcp=true
greeter-session=unity-greeter

[xdmcp]
Enable=true
```

The key parameter to be added is `xserver-allow-tcp`.
For a more complete list of configuration parameters for lightDM Display Manager,
see the article "[Disable guest session in Ubuntu 11.10][33]" and
[Understanding lightdm.conf][].

### Configuring Local Computer (TCL Vintage Laptop)
I install the following extensions via TCL `Apps` application (OnBoot):

* openssl-1.0.0.tcz

### Tiny Core Linux Boot Sequence
init -> tc-config -> init -> /root/.profile -> /home/tc/.profile -> /home/tc/.xsession
[ Boot sequence - what starts xvesa xserver?](http://forum.tinycorelinux.net/index.php?topic=1924.0)

[HOWTO Xnest, secure Xnest](http://antoine.ginies.free.fr/xnest/#id2477891)
[Xnest - Create a new Display in a Window - Linux](https://www.youtube.com/watch?v=BSYmajttVDw)

[xdmcp](https://wiki.ubuntu.com/xdmcp)
[Ubuntu 12.10 Login Screen Adds Remote Desktop Access](http://www.omgubuntu.co.uk/2012/09/ubuntu-12-10-login-screen-adds-remote-desktop-access)
[How to Remote Login via XDMCP in Ubuntu](http://danilodellaquila.com/blog/how-to-remote-login-via-xdmcp-in-ubuntu)
[How to enable remote access to Xserver on Ubuntu 11.04 and Ubuntu 11.10](http://pzuk.wordpress.com/2011/10/21/how-to-enable-remote-access-to-xserver-on-ubuntu-11-04-and-ubuntu-11-10/)
[XDM and X Terminal mini-HOWTO](http://www.faqs.org/docs/Linux-mini/XDM-Xterm.html)
[Building X terminals with Linux](http://development.gbdirect.co.uk/xterminal.html)
[setting up x terminal workstation](https://groups.google.com/forum/#!topic/linux.debian.user/nUguTStjRkU)
[Remote Access](http://linuxtutorial.info/modules.php?name=MContent&pageid=45)

[X terminals in Linux (Running X programs remotely using SSH, XDMCP, or Sterminal)](http://www.spencerstirling.com/computergeek/xterminal.html)


![WABAC Machine](https://upload.wikimedia.org/wikipedia/en/3/3f/Waybackmachine3.png)



[01]:https://help.ubuntu.com/community/Lubuntu/GetLubuntu
[02]:https://help.ubuntu.com/community/Installation/FromWindows
[03]:https://help.ubuntu.com/community/Lubuntu/InstallingLubuntu
[04]:http://lubuntu.net/
[05]:https://help.ubuntu.com/community/Lubuntu/Alternate_ISO
[06]:http://en.wikipedia.org/wiki/ISO_image
[07]:http://www.damnsmalllinux.org/
[08]:http://www.osnews.com/story/24936/Damn_Small_Linux_Still_Damn_Fun
[09]:http://en.wikipedia.org/wiki/Celeron
[10]:http://en.wikipedia.org/wiki/List_of_Intel_microprocessors
[11]:http://www.busybox.net/
[12]:http://www.osnews.com/story/24476/Lubuntu_Finally_a_Lightweight_Ubuntu_
[13]:http://voices.yahoo.com/how-download-install-dsl-linux-5947706.html?cat=15
[14]:http://tinycorelinux.net/
[15]:http://tinycorelinux.net/install.html
[16]:http://tinycorelinux.net/install_manual.html
[17]:http://en.wikipedia.org/wiki/GNU_Core_Utilities
[18]:http://en.wikipedia.org/wiki/Live_CD
[19]:http://en.wikipedia.org/wiki/Damn_Small_Linux
[20]:http://en.wikipedia.org/wiki/PC_Card
[21]:http://puppylinux.org/main/Overview%20and%20Getting%20Started.htm
[22]:http://en.wikipedia.org/wiki/X_terminal
[23]:http://en.wikipedia.org/wiki/Thin_client
[24]:https://www.youtube.com/watch?v=lFxXeDKgymM
[25]:http://www.fltk.org/index.php
[26]:http://www.tinycorelinux.net/corebook.pdf
[27]:http://en.wikipedia.org/wiki/X_display_manager_(program_type)
[28]:http://wiki.tinycorelinux.net/wiki:list_of_supported_wifi_devices
[29]:http://www.ltsp.org/
[30]:http://www.spencerstirling.com/computergeek/xterminal.html
[31]:http://blog.worldlabel.com/2009/turn-your-old-laptop-into-a-powerful-linux-workhorse.html
[32]:http://en.wikipedia.org/wiki/Xnest
[33]:http://hmontoliu.blogspot.com/2011/10/disable-guest-sesson-in-ubuntu-1110.html
[34]:https://help.ubuntu.com/community/SSH/OpenSSH/Configuring
[35]:https://help.ubuntu.com/community/FreeNX
[36]:http://www.mattfischer.com/blog/?p=343
[37]:http://wiki.lxde.org/en/LXSession
[38]:http://en.wikipedia.org/wiki/X11
[39]:http://xfree86.sourceforge.net/
[40]:http://www.x.org/wiki/
[41]:http://x.cygwin.com/
[42]:http://en.wikipedia.org/wiki/X_Window_System_protocols_and_architecture
[43]:http://en.wikipedia.org/wiki/Desktop_environment
[44]:http://askubuntu.com/questions/150487/what-happens-under-the-covers-to-log-me-in-and-start-up-the-unity-graphics-user?r
[45]:
[46]:
[47]:
[48]:
[49]:
[50]:
