Title: Having Fun with Wine, VirtualBox, and TurboTax
Date: 2014-01-15 00:01
Category: Software
Tags: Wine, VirtualBox
Slug: having-fun-with-wine-virtualbox-and-turbotax
Author: Jeff Irland
Image: virtualbox-logo.jpg
Summary: I discovered that getting Microsoft Windows applications working using Wine is a pain!  Out of necessity, I turn to VirtualBox.  Getting VirtualBox and MS Windows 8.1 working together is simple.

Sometime ago, I committed myself to Linux and [Wine][06],
with the promise that I would sincerely abandon Microsoft Windows by
not [dual booting][07] my system nor installing any [virtualization][01] software.
Well, it is now tax-time and the Federial goverment wants their "fair share" of my income.
Will my prefered tax software package, [TurboTax][02], run with Linux & Wine?
All the evidence I have gathered (see [Wine's ratings][03] for one data point)
on the web leads me to believe I will be very disapointed.
I can't find any success stories!
Never the less, I will use this as a learning opportunity.
I'm going to plung forward and try to get TurboTax working with Wine, ....
and it it fails me, resort to [VirtualBox][04],
which appears to have at least [some success][05] stories.

# Installing and Configuring Wine
Wine can be installed via the following:

```shell
sudo add-apt-repository ppa:ubuntu-wine/ppa
sudo apt-get update
sudo apt-get install wine
sudo apt-get install cabextract
sudo apt-get install winetricks
```

`winetricks` is a script which automates the installation of various useful packages,
offering a friendly interface to do so.
The `cabextract` package is a native Linux application that extracts Microsoft Cabinet files (CAB).
`ppa:ubuntu-wine/ppa` will get the latest versions for Wine and keep it updated with new releases.
This is important since the Wine support team is frequently
fixing and twecking it to get Microsoft Windows software working.
To test if you got things installed properly[^A],
execute one of the already installed Microsoft Windows packages.
Try the following: `wine notepad.exe`.

[^A]:
    **NOTE:** Use the utility [`winecfg`][08] to configure Wine and change settings like
    sound, graphics, Windows version, and so on.

# Installing TurboTax with Wine
Wine is complex and large.
I don't have the patience for hours of configuring and testing; 
particularly if in the end I can't print or electronically email my tax return.
I'm going to plung into installing TurboTax via Wine,
and see if I can get things running with minimal effort.

So, I put the CD in the drive, right clicked on the setup.exe file, picked the menu item
"Open With Wine Windows Program Loader", and got a error screen titled
["We can't install TurboTax on your computer just yet..."][09].
Appears that TurboTax doesn't like Wine's version of the .NET Framework.
A little [research][10] surggested that I should install .NET 4 via this command:

```shell
winetricks dotnet40
```

After this, I still got a .NET related error.
Specifically, the TurboTax installer was looking for the `netfx40testapplication.exe`.
Another quick search brought me to these bug report: #[1][11] and [#2][12].
I have had enough ... on to VirtualBox!!

# Installing TurboTax with VirtualBox
VirtualBox is being setup with Microsoft Windows (specifically Windows 8.1)
as a the Guest OS and with the native Linux (specifically Ubuntu 13.10) as the Host OS.
[VirtualBox version 4.3 has added Windows 8.1 support][14],
so that is the version I wish to install.
I initially installed VirtualBox via Unbuntu's software center
(eqivalent to using `sudo apt-get install virtualbox virtualbox-qt`),
which installed version 4.2.16-dfsg-3, and I had to back it out.
Instead, I install VirtualBox from the Oracle maintained repository,
following the [procedures outlined by Oracle][15].
I added the following lines (for the approprate linux distribution; mine is saucy)
to the `/etc/apt/sources.list` file:

```
# Oracle's software repository for VirtualBox
deb http://download.virtualbox.org/virtualbox/debian saucy contrib
```

Downloaded the Oracle public key for the software:

```shell
wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
```

Now install VirtualBox version 4.3:

```shell
sudo apt-get update
sudo apt-get install dkms virtualbox-4.3
```

### Configuring VirtualBox and Installing Windows 8.1
It appears you can install 32 or 64 bit Windows (assuming you have virtualization suporting processor).
I choose the 64 bit version.
As to the installation steps, I was guided by the posting "[Windows 8.1 in VirtualBox][16]",
and the steps are basically the following:

**Configure VirtualBox**

* Fired up VirtualBox, clicked the "New" button, and used the Wizard to create a virtual partition for Window
* I gave the virtual machine the name "MS Windows"
* I allocated to the virtual machine the maximum amount of RAM, that being 3.584GB
* I created a 50GB virtual hard drive with a VirtualBox Disk Image (VDI).  I Choose to have the virtual drive to grow dyanamically.
* I opened up "Settings" and under "System" > "Processor", enable "PAE/NX". I also increased the CPU Cores to the number supported on my box (i.e. 4).
* Under "Display" > "Video", I increased the Video Memory as high as I can, disable 3D Acceleration but enabled 2D Acceleration.

**Install Windows 8.1**

* Still in the "Settings" window, go to "Storage" and under "IDE" where it shows "Empty", click the disk next to it and installed Windows 8.1 64-bit DVD into the drive.
* Still with "Storage", click the disk icon right of the "CD/DVD Drive" and select "Host Drive ...".  Also check "Passthrough". Click "OK".
* Select the "Start" button om the VirtualBox Manager window.
* At this point, a window should pop up and you see the Windows 8.1 install process begin.

### Installing TurboTax on VirtualBox
This is easy.
Fire up the "MS WIndows" vitual machine, and load TruboTax like you would any other Microsoft Windows application.

# Conclusion
Everything seems to be working perfectly within TurboTax using VirtualBox!
I believe VirtualBox is destine to stay load on my Linux box.
As to Wine, .... we'll see.

# Sources
Getting Wine Working

* [A Guide to Wine on Ubuntu for Beginners](http://www.tuxarena.com/static/tut_wine_guide.php)
* [How To Run Windows Software on Ubuntu with Wine](http://www.howtogeek.com/105271/how-to-run-windows-software-on-ubuntu-with-wine/)
* [Use Wine to run Windows software on Linux](http://www.linuxuser.co.uk/tutorials/use-wine-to-run-windows-software-on-linux)
* [Wine 1.7.9 Released – Install on Ubuntu 13.04/12.10/12.04/11.10 and Linux Mint 16/13](http://www.tecmint.com/install-wine-on-ubuntu-and-linux-mint/)
* [Ubuntu Tips: How To Use Windows Applications in Linux Desktop Distributions](http://www.thegeekstuff.com/2009/08/ubuntu-tips-how-to-use-windows-application-in-linux-desktop-distributions/)
* [How to install Windows programs in Linux using Wine](http://www.simplehelp.net/2007/05/18/how-to-install-windows-programs-in-linux-using-wine/)
* [Running Microsoft DOS and Microsoft Windows Software on Linux](http://www.yolinux.com/TUTORIALS/LinuxTutorialRunMicrosoftExe.html)
* [winetricks](http://wiki.winehq.org/winetricks)

Getting TurboTax or Quicken Working

* [History of TurboTax Support via Wine on Linux](http://appdb.winehq.org/objectManager.php?sClass=application&iId=623)
* [Solved-Quicken 2011 Working on Linux](http://blog.jdpfu.com/2010/11/29/solved-quicken-2011-working-on-linux)

Getting VitualBox Working

* [Using Windows XP in VirtualBox on Linux](http://www.linuxjournal.com/content/using-windows-xp-virtualbox-linux)
* [Install windows 7 through virtual box in ubuntu 12.04](http://askubuntu.com/questions/187424/install-windows-7-through-virtual-box-in-ubuntu-12-04)
* [How to Install Windows XP on Ubuntu with VirtualBox](http://www.wikihow.com/Install-Windows-XP-on-Ubuntu-with-VirtualBox)
* [Install Windows 8.1 on Oracle VirtualBox](http://betanews.com/2013/10/21/install-windows-8-1-on-oracle-virtualbox/)
* [Windows 8.1 in VirtualBox](http://www.geekthis.net/blog/95/windows-81-in-virtualbox)
* [VirtualBox/Installation](https://help.ubuntu.com/community/VirtualBox/Installation)
* [Starting VirtualBox](https://www.virtualbox.org/manual/ch01.html#idp51679504)


[01]:http://en.wikipedia.org/wiki/Virtualization
[02]:https://turbotax.intuit.com/
[03]:http://appdb.winehq.org/objectManager.php?sClass=application&iId=623
[04]:https://www.virtualbox.org/
[05]:https://blogs.oracle.com/wbays/entry/turbotax_on_virtualbox_problem_solved
[06]:http://www.winehq.org/
[07]:http://en.wikipedia.org/wiki/Multi-booting
[08]:http://wiki.winehq.org/winecfg
[09]:https://ttlc.intuit.com/questions/1899606-error-we-can-t-install-turbotax-on-your-computer-just-yet
[10]:http://superuser.com/questions/476872/installing-net-4-0-framework-on-wine-using-winetricks
[11]:http://www.winehq.org/pipermail/wine-bugs/2012-January/308034.html
[12]:http://wine.1045685.n5.nabble.com/Bug-29666-New-TurboTax-2011-fails-to-install-td5161768.html
[13]:http://www.linuxjournal.com/content/using-windows-xp-virtualbox-linux
[14]:http://www.lifehacker.com.au/2013/10/virtualbox-4-3-adds-windows-8-1-support/
[15]:https://www.virtualbox.org/wiki/Linux_Downloads
[16]:http://www.geekthis.net/blog/95/windows-81-in-virtualbox
