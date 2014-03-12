Title: Linux Maintenance and Filesystem Hygiene
Date: 2014-02-21 18:20
Category: Linux
Tags: Linux
Slug: linux-maintenance-and-filesystem-hygiene
Author: Jeff Irland
Summary: bla bla bla

## Gather Information
For some of the maintenance activities listed here, your going to need some basic information.
This next section should be helpful.

#### Distribution Name and Version
To determine which Linux version / build / release / distribution you are running:

    # kernel name and release
    uname -sr

    # kernel version
    uname -v

    # Linux distribution
    cat /etc/*-release
    lsb_release -a

Use the following command to get a listing of all the physical hard drives
(and virutal drives) on the system:

    hwinfo --disk --short

For the Raspberry Pi, you can list the installed firmware version via:

    /opt/vc/bin/vcgencmd version

## Maintenance
#### Install Operating System and Application Patches/Updates
This will patch the Linux operating system and all its GPL applications 

    sudo apt-get update; sudo apt-get dist-upgrade

#### Updating Firmware for Raspberry Pi
In the case of the Raspberry Pi (RPi), you will want to also upgrade the firmware regularly.
[Raspbian][07] is the standard Linux operating system distribution for the RPi,
but it doesn't include firmware.
Never the less, tools for updating the firmware are included in the Raspbian distribution of Linux.
That tool is `sudo apt-get install rpi-update`.
I'm using the [Adafruit's Occidentalis distribution][08], so this requires a
[slightly different update tool][09] (`git` needs to be installed):

    sudo wget https://raw.github.com/Hexxeh/rpi-update/master/rpi-update -O /usr/bin/rpi-update
    sudo chmod +x /usr/bin/rpi-update

Once the tool has been installed, periodically you can update the firmware via these commands:

    sudo BRANCH=next rpi-update
    sudo reboot

Note that once the firmware has been sucessfully updated,
you'll need to reboot to load the new firmware.

#### Check Stoarge and Inode Usage
If you let some directories get really full, like above 95% full, you will see some serious system problems.
Check on the status of directory systems storage space and inode usage:

    df
    df -i

#### Disk and Filesystems Integrity
[Smartmontools][02] is a set of applications that can test hard drives
and read their hardware SMART statistics (install with `sudo apt-get install smartmontools`).
To ensure that your drive supports [SMART][03], type the following for each physical drive:

    sudo smartctl -i /dev/sda 

If smartctl can access the drive, you should turn on some SMART features.
Run the following command my three drives:

    sudo smartctl -s on -o on -S on /dev/sda

Check the disk's overall health:

    sudo smartctl -H /dev/sda

If it doesn’t return PASSED, you should immediately backup all your data.
A short, but more extensive test is

    sudo smartctl -t short /dev/sda

You can do a long self-test, but this can take a significant amount of time.
You might want to run it overnight and check for the results in the morning.

    sudo smartctl -t long /dev/sda

To check results, run the following:

    sudo smartctl -l selftest /dev/sda

Unfortunately, there’s no way to check progress, so just keep running that command until the results show up.

 If either test fails, you should immediately backup all your data.
Depending on the error, your drive might be close to death or it may still have a long life ahead.
Consult the [smartmontools FAQ][06].

We’ve now enabled some features and run the basic tests.
Instead of repeating the previous section daily, we can setup `smartd` to do it all automatically.
Via the demon, you can run Smartmontools in the background,
have it check drives, and email you when there are issues.
See the Sources below to figure out what needs to be done to setup the `smartd` demon.

## Clean-Up
#### Clean-Up Temporary Files
Some editors (like vim) may leave files ending with a ‘~' character laying around.
You can clean them up under your HOME as a normal user
(You can do it for the entire system as root, but that can be extremely dangerous.)
Use the command below to get a list of candidates:

    find $HOME -type f -name "*~" -print

After that appears to do what you want, add the -exec part.

    find $HOME -type f -name "*~" -print -exec rm {} \; 

Kernel crashes, when they happen, write the core dump files under /var.
Assuming you aren't saving them for debugging, you can do this to get a listing:

    sudo find /var -type f -name "core" -print

Some applications create temporary files in their own directories: 

    rm -rf ${HOME}/.macromedia/* ${HOME}/.adobe/*

#### Clean-Up Old Log Files
You can also remove old compress log files from the system with

    sudo rm -v /var/log/*.gz

#### Clean-Up Installation Packages
To remove partual packages, clean the cache, remove unused dependancies use:

    sudo apt-get autoclean
    sudo apt-get clean
    sudo apt-get autoremove

You also need to do something similar for kernel installations.
You find a the current kernel installation packages being kept in /boot by running:

    df -h /boot

The current Linux kernel installation (and one you should keep) can be identified via:

    uname -r

Run the following command to list all packages that you no longer need:

    dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d'

#### When the Hard Disk Goes South
For basic disk errors, you could try letting Linux heal itself with fsck at boot up.
To do this, shut down the system with the -F option like this:

    sudo shutdown -r -F now

Linux reboots immediately and looks for disk errors with the [`fsck`][05] command.
Confirm fixing disk errors by pressing "y" and "Enter" if prompted.

If this fails, read these articals "[Disk Maintenance under Linux (Disk Recovery][01]",
[How to recover partitions and data using Linux - Tutorial][04],
and then follow the instructions carefully!

## Sources
I consulted the following sources to create this posting:

* [Why use apt-get upgrade instead of apt-get dist-upgrade?](http://askubuntu.com/questions/194651/why-use-apt-get-upgrade-instead-of-apt-get-dist-upgrade)
* [What Kind of Maintenance Do I Need to Do On My Linux PC?](http://lifehacker.com/5817282/what-kind-of-maintenance-do-i-need-to-do-on-my-linux-pc)
* [Is system cleanup/optimization needed](http://askubuntu.com/questions/81042/is-system-cleanup-optimization-needed)
* [Disk Maintenance under Linux (Disk Recovery)](http://www.linuxjournal.com/article/193?page=0,0)
* [Smartmontools](https://help.ubuntu.com/community/Smartmontools)
* [S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology)](https://wiki.archlinux.org/index.php/S.M.A.R.T.)
* [Monitoring Hard Drive Health on Linux with smartmontools](http://blog.shadypixel.com/monitoring-hard-drive-health-on-linux-with-smartmontools/)



[01]:http://www.linuxjournal.com/article/193?page=0,0
[02]:http://sourceforge.net/apps/trac/smartmontools/wiki
[03]:http://en.wikipedia.org/wiki/S.M.A.R.T.
[04]:http://www.dedoimedo.com/computers/linux-data-recovery.html
[05]:http://linux.die.net/man/8/fsck
[06]:http://sourceforge.net/apps/trac/smartmontools/wiki/FAQ
[07]:http://www.raspbian.org/
[08]:http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/overview
[09]:https://github.com/Hexxeh/rpi-update
[10]:
[11]:
