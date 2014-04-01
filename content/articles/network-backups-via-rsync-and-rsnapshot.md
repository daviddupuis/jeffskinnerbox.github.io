Title: Network Backups via Rsync and Rsnapshot
Date: 2014-02-08 00:01
Category: Software
Tags: Linux, Rsync, Rsnapshot 
Slug: network-backups-via-rsync-and-rsnapshot
Author: Jeff Irland
Image: backup-vault.png
Summary: Using a external hard drive, and rsync / rsnapshot as a remote filesystem backup utility, I create scheduled incremental backups of my Linux & Windows filesystems. This light-weight and efficient scheme allows me to create increment backups every 4 hours and keep backups up to three months.

### Rsync and Rsnapshot
<a href="http://www.seagate.com/external-hard-drives/desktop-hard-drives/backup-plus-desk/">
<img class="img-rounded floatLeft" style="margin: 0px 8px; float: left" title="Seagate Backup Plus" alt="{{ site.author.name }}" src="http://www.hotcouponworld.com/wp-content/uploads/2013/03/4tb.jpg" width="30%" height="30%" /></a>
I got a 4 Terabyte [Seagate Backup Plus][05] hard drive as a Christmas present and
I plan to put it to use as a central backup for my Linux desktop, multiple Raspberry Pi,
my laptop, and anything else that my come along.
My plan is to keep things simple but I wish to do
regular hourly, daily, weekly, and monthly incremental backups.
This will give me the ability to recover files from the past,
but also to recover from a hardware failure or software install that has gone very badly.

There are [many backup tools][01] you can pick from but
I wanted to stick with something basic, widely used, and simple.
[Rsync][02] is one of the most widely used Linux backup solutions, and in fact,
it is often used by [other backup tools][03] as a foundational component. 
Rsync stands for **r**emote **sync**hronization tool.
Rsync is a UN*X command line utility, containing a [special protocal and algorithm][35],
that synchronizes files and directories from one location to another
while minimizing data transfer by using fast incremental file transfers.
(rsync has also been ported to Microsoft Windows, Mac, and other operating systems.)
The first time, rsync sends all the data over the network to your backup machine.
The benefit comes the next time you backup.
Instead of sending all the files again, rsync only transfers files that have been changed.
If no files were changed, no files get transferred.
And when you want to recover data, you transfer just the specific files that you want back to your machine
(using rsync or scp or telnet or whatever).

Rsnapshot is a great little utility for creating easy-to-use backups.
Using rsnapshot is possible to take snapshots of your file system at different points in time.
It creates a full-blown snapshot for each run,
but uses [hard links][14][^A] for files that haven’t changed.

[^A]:
    **NOTE:**
    [Hard links are similar to symlinks][33].
    They are normally created using the `ln` command but without the `-s` switch.
    A hard link is when two file entries point to the same [inode][31] and [disk blocks][32].
    Unlike [symlinks][34] there isn't a file and a pointer to the file, but rather two links to the same file.
    If you delete either entry the other will remain and will still contain the data.

That means you get efficient, lightweight,
incremental backups that look like exactly like full-blown copies (in every way).
This makes Rsnapshot a great choice for server backups.
This easy-to-use utility is commonly used for backing up data,
but can synchronize files for any other purpose you choose to use it for.
Remote sync can be better than other backup methods because of its speed,
and because it doesn’t require any special permissions to execute an rsync command.
With just a small knowledge of the command line, you can be backing up in no time with rsync.
You can also use [cron][15] to periodically create backups.
To top it off, it also hase a graphics frountend tool, call [grsync][04],
and [rsnapshot][08] to create scheduled incremental backups, if so desired.

### Install the Hard Drive
The physical install of the extenal [Seagate Backup Plus][05] drive was simple, just plug it in.
The only caveat is to use a [USB 3.0][06] port on the Linux box to make sure you
get the fill speed out of the drive.
Using the supplied USB 3.0 cable is a must,
since a USB 2.0 cable will force the drive to operate at a slower speed.
Check out [USB 2.0 vs USB 3.0][07] to understand further.

Under my Ubuntu system, this external disk's file system will be automatically mounted
located at `/media/jeff/"Seagate Backup Plus Drive"`.
This nice and easy, but the disk is formated as a [NTFS (New Technology File System)][10]
which is a proprietary file system developed by Microsoft.
For Linux compatibility reasons,
I want the disk to support a [Linux ext3 file system][11].
This will requiring re-formating and mounting the new disk.
To do this, I followed the procedures outlined in
in the artical "[Partition and format external hard drive as ext3 filesystem][12]".
I created a mount point called `/mnt/backup` for the hard drive and
place it in the `fstab` file so its mounted everytime at boot up.

### Install rsync, grsync, and rsnapshot
Rsync should already be installed on most Linux system.
You can install it, and the [grsync][04] & [rsnapshot][08] tools, using this command:

```bash
sudo apt-get install rsync grsync rsnapshot
```

### Select Backup Storage Location
I want to create directory for the backups that are readable by all users, but writable by only root.
To do this, do the following:

```bash
mkdir /mnt/backup
chmod a+rwx /mnt/backup
chmod o-w /mnt/backup
```
 
### Getting Familiar with rsync and Preparatory Work
In this section, we'll learn about some of rsync's features and get some foundational stuff done.
##### Dry Running a rsync Command
Rsync has the potential of really messing up things
and then doing an undo can be a tedious job.
Rsync can be run in a "dry run" mode to show you the output of the command.
For example, this will make a copy of `~/tmp`: 

```shell
rsync -azv --dry-run /home/jeff/tmp/ /home/jeff/tmp/copy-of-tmp
```

If the output shows exactly what you want to do,
then you can remove `–dry-run` option from your command and re-run it for real. 

##### Test rsync on Local System
In an effort to try out rsync in the raw,
I'll create some ad hoc backups of my desktop's home directory.
I want to preserves file timestamp, symbolic links, permissions, and owner/group.
This can be done using the rsync option `-a`.
Additional options used are `-z` to enable compression,
and `-v` to provide verbose status output.

```shell
sudo rsync -azv /home/jeff/src/rtl-sdr/ /mnt/backup/rsync-test1
```

The `sudo` is required since I have made `/mnt/backup` writable only by root.
The presence or absence of the terminating `/` within the rsync command line is important.
The following two commands produce different results:

```shell
sudo rsync -azv /home/jeff/Documents/"My Maps"/ /mnt/backup/rsync-test2
sudo rsync -azv /home/jeff/Documents/"My Maps" /mnt/backup/rsync-test3
```

The first takes the sources files and subdirectories and writes them directly to the destination directory.
The second does the same but the files and directories go wihin a directory called `My Maps`.
This is an important subtlety to remember!

##### Testing rsync on a Remote System
In this case, my Linux desktop machine is the local system and RPi is the remote machine.
The Linux desktop has the external drive used for backups.

```shell
sudo rsync -azv pi@RedRPi:/home/pi/src/nRF24L01 /mnt/backup/rsync-test4
```

This will first prompt you for a password for the `sudo`.
You will get a subsequent prompt for the login as `pi` on the `RedRPi` system,
and then the data will be transfered to the external drive.
but when performing beyond your the firewall, you should use ssh, as shown below:

```shell
sudo rsync -azv -e ssh pi@RedRPi:/home/pi/src/ /mnt/backup/rsync-test5
```

To setup ssh with rsync so that it can run automatically without prompting for the pasword,
checkout "[How to Setup Rsync with SSH on UNIX / Linux (rsync without password)][09]".
This is sometime you will want to do to support automatic, unattended backups.
Basicly, your going to do the following on the machine that will store the backups[^B]:

[^B]:
    **NOTE:**
    The command `ssh-copy-id` may not work if your attempting use the
    root login instand of pi on the remote machine.
    In this case, you'll need to manually move the public key to its destination.
    The artical "[Create SSH Passwordless Login Using SSH Keygen][13] can show you how to do this.

```shell
cd $HOME
mkdir .ssh
chmod 755 .ssh
ssh-keygen -N "" -f /$HOME/.ssh/id_rsa
ssh-copy-id -i /$HOME/.ssh/id_rsa.pub pi@RedRPi
ssh-copy-id -i /$HOME/.ssh/id_rsa.pub pi@BlackRPi
sudo bash
cd /root
mkdir .ssh
chmod 755 .ssh
ssh-keygen -N "" -f /root/.ssh/id_rsa
ssh-copy-id -i /root/.ssh/id_rsa.pub pi@RedRPi
ssh-copy-id -i /root/.ssh/id_rsa.pub pi@BlackRPi
exit
```

Now repeat the example above:

```shell
sudo rsync -azv -e ssh pi@RedRPi:/home/pi/src/ /mnt/backup/rsync-test5a
```

You should no longer be promoted for a password, except by the first `sudo`.
(Once rsync is run under a root login, this `sudo` will no longer be required).

##### Exclude Files / Directories from rsync
In a typical backup situation,
you might want to exclude one or more files (or directories) from the backup.
You might also want to exclude a specific file type from rsync.
Let's run a backup of `pi@RedRPi:/home/pi/`
but leave out the `tmp` and `src` directories.

```shell
sudo rsync -azv -e ssh --exclude 'tmp' --exclude 'src' pi@RedRPi:/home/pi/ /mnt/backup/rsync-test6
```

You could also create a file that contains the exclude list `tmp` and `src`.
This would look like:

```shell
sudo rsync -azv --exclude-from 'exclude-list.txt' pi@RedRPi:/home/pi/ /mnt/backup/rsync-test6
```

##### Running rsync as Root
The above examples works fine as long as the source login (in this case `pi` on the `RedRPi` system)
has the approprate permissions.
For example, this will fail:

```shell
sudo rsync -azv -e ssh  pi@RedRPi:/root/ /mnt/backup/rsync-test7
```

It fails because the user `pi` doesn't have `root` permissions
and the directory `/root/` can only be entered by the user `root`.
You might want to attempt to do the following:

```shell
sudo rsync -azv -e ssh root@RedRPi:/root/ /mnt/backup/rsync-test7
```

Now your asking to login to the remote system as user root.
In this case you'll be prompted to provide the RedRPi's root password,
but the root login may not have a password[^C].

[^C]:
    **NOTE:**
    Because of an abundance of paranoia,
    remote root login over `ssh` session is disabled in some Linux distributions for [security reasons][18].
    By default, the Root account password is locked in Ubuntu and most other version of Linux.
    The account has no password, even thou it prompts you to provide one.
    This means that you cannot login as Root directly or use the su command to become the Root user.
    However, since the Root account physically exists it is still possible to
    run programs with root-level privileges.
    This is where [sudo][20] comes in - it allows authorized users (normally "Administrative" users)
    to run certain programs as Root without having to know the root password.

The way around all this is to use the `--rsync-path` option for rsync.
This will work:

```shell
sudo rsync -azv -e ssh --rsync-path="sudo rsync" pi@RedRPi:/root /mnt/backup/rsync-test7
```

The `--rsync-path` parameter specifies a path to rsync on the remote machine.
So `rsync` will be executed using `sudo`, giving it root user access privilages,
and now the use of the `pi` login will gain access to the `/root` directory.
That is, on the remote machine, rsync is being run as root!
This all requires the proper set-up of ssh with password-less access, discussed earlier.

##### Configuration of ssh to Eliminate Password Prompt and Warning Messages
Proper configuration of ssh will be needed to assure routine warning messages[^D]
don't disrupt the smooth operation of rsync / rsnapshot.

[^D]:
    **NOTE:**
    One of the most common warnings you will likely encounter is a host key error
    which may not happen until long after you have made your first connection to a host.
    If any of several identifying features of the host change,
    a new host key could be created and if that happens your ssh client will let you know
    by refusing to log you into that system without first prompting you to confirm the warning,
    or may even force you to provide the login's password.
    It can be confusing on how to clean this up, but these two articals can help:
    [How to accept ssh host keys automatically on Linux][19]
    and [“Warning: Permanently added to the list of known hosts” message from Git][22].

Specifically, we need to add the approprate parameters to one of the
`ssh` configuration files listed below:

* **System-wide SSH client configuration files (i.e. /etc/ssh/ssh_config -** This files set the default configuration for all users of OpenSSH clients on that desktop/laptop and it must be readable by all users on the system.
* **User-specific SSH client configuration files (i.e. $HOME/.ssh/config -** This is user's own configuration file which, overrides the settings in the global client configuration file, `/etc/ssh/ssh_config`.

Add this to `/etc/ssh/ssh_conf` file to disable the host key checking
and the warnings[^E] for all users who access systems whos names end in 'RPi'.

[^E]:
    **NOTE:**
    The suppresion of this warning does reduce the security profile of the system.
    Instead of suppressing the warning for all ssh access to *RPi,
    you could implement this functionality [solely for the `rsync` command][21] by using
    the option `-e "ssh -o CheckHostIP=no -o StrictHostKeyChecking=no"`.
    See [ECDSA Keys Changed, SSH insecure now][37].

```
Host *RPi
    StrictHostKeyChecking no
    UserKnownHostsFile=/dev/null
```

In addition, add the following to the `$HOME/.ssh/config` file:

```
UserKnownHostsFile  ~/.ssh/known_hosts
```

Make these changes active by restarting the ssh services via the command `sudo service ssh restart`.

With ssh properly configured, a command like

```shell
sudo rsync -azv -e ssh --rsync-path="sudo rsync" pi@BlackRPi:/root/.rpi-firmware/ /mnt/backup/rsync-test8
```

should run without requesting passwords, it will run on the remote as the root user,
and warning messages about differing "ECDSA host key" should not get in your way.
It will run without user intervention; just what we need for automated backups!


##### Creating Backup Users on Remote Servers
On all the remote systems (i.e. RedRPi and BlackRPi) you need to create the login
and establish its ssh authentication keys.

```shell
sudo adduser backup_user --disabled-password -u 400
sudo mkdir /home/backup_user/.ssh
sudo chmod 700 /home/backup_user/.ssh
```

Now create a rsync wrapper script:

```shell
sudo mkdir /home/backup_user/bin
sudo vim /home/backup_user/bin/rsync-wrapper.sh
```

Enter the following in this file to create the script:

```shell

#!/bin/sh

# This script is a wrapper around rsync, so that rsync can run as root,
# and at the same time, eliminate any security risks.

# Place in the log file information concerning the execution of this script
echo -n "rsync wrapper script executed on " >> /home/backup_user/backup.log
date >> /home/backup_user/backup.log
echo -n "options passed to rsync: " >> /home/backup_user/backup.log
echo $@ >> /home/backup_user/backup.log
echo "---------------------------------------------" >> /home/backup_user/backup.log

# Now execute the script
/usr/bin/sudo /usr/bin/rsync "$@";
```

Now change the mode and owner of this file:

```shell
sudo chown backup_user:backup_user /home/backup_user/*
sudo chown backup_user:backup_user /home/backup_user/bin/rsync-wrapper.sh
sudo chmod 754 /home/backup_user/bin/rsync-wrapper.sh
```

Now for the `backup_user`, configure `sudo` such that it can run the rsync tool
as root without being being prompted for a password.
For security reasons, we what only the rsync tool to have `sudo` privileges.
Using [`visudo`][23] command, edit the [`/etc/sudoers`][24][^F] file by adding the following 
to the bottom of the file.

[^F]:
    **NOTE:**
    The sudoers configuration file enables a huge amount of configurability,
    including but not limited to: enabling root commands only from the invoking terminal;
    not requiring a password for certain commands;
    requiring a password per user or group;
    requiring re-entry of a password every time or never requiring a password at all for a particular command line.
    It can also be configured to permit passing arguments or multiple commands,
    and even supports commands with regular expressions.

```
# allows this user to not need a password to sudo the specified command(s)
backup_user    ALL=NOPASSWD:    /usr/bin/rsync
```

##### Creating Backup Users for Backup Server
On the host server (i.e. desktop) you need to create the login
(with a UID of less that 500[^G])
which will run the rsync / rsnapshot utilities
and establish its `ssh` authentication keys.

[^G]:
    **NOTE:**
    I choose a UID of 400 so that the `backup_user` would not appear on the Ubuntu login screen list.
    To hide a user from the Ubuntu login screen list,
    you should be able to add the name to the hidden-users
    list in the file `/etc/lightdm/users.conf`, but there is a [problem][25].
    The is an alternative, and that is to choose a UID value less than 500
    (See the "minimum-uid" in `/etc/lightdm/users.conf`).

```shell
sudo adduser backup_user -u 400
sudo chown backup_user:backup_user /home/backup_user/*
sudo su backup_user
cd ~
ssh-keygen -N "" -f ~/.ssh/id_rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub backup_user@RedRPi
ssh-copy-id -i ~/.ssh/id_rsa.pub backup_user@BlackRPi
exit
```

##### Increased Security
To increase the security of the overall scheme, 
on the remote systems and on the local system,
remove the user password from the `backup_user` user via

```shell
sudo passwd --delete backup_user
```

### Configuring rsnapshot for Incremental Backups
Our mission here is to use rsnapshot to create backups of both normal
and protected/restricted files from one server to another over `ssh`
without enabling remote root access to either server while
maintaining original file attributes and permissions[^H].

[^H]:
    **NOTE:**
    To automate rsnapshot backup to a remote servers,
    you'll also need to set up key-based authentication over SSH on the remote
    machines that you want to backup,
    so that they can be accessed without need for a password login.
    And you need to make sure this arrangement survives a reboot.
    To accomplish this, you will need to create an SSH public and private keys to authenticate on the rsnapshot server.
    This was all discussed earlier.

Where rsync does the actual file backups, rsnapshot is responsible for the overall management of the backups.
In my case, I want it to schedule a nested and rotating series of incremental backups for my systems.
I want the schedule and the backup increments to be:

* Every 4 hours, create an incremental backup, and store all of them for the past 24 hours
* Create a daily incremental backups (from the last hourly backup), and store a daily backup for the past 7 days
* Create a weekly incremental backups, and store them for the past 4 weeks
* Create monthly incremental backups, and store for the past 3 months

When making the backups, the contents of `/dev`, `/proc`, `/sys`, `/tmp`, and `/run` should be excluded
because they are populated at boot (while the directories themselves are not created).
The file `/lost+found` is filesystem-specific and doesn't need to be copied.
(Note: If you plan on backing up your system somewhere other than `/mnt` or `/media`
don't forget to add it to the list, to avoid an infinite loop.)

rsnapshot also provides a non-commandline method for excluding file, which is what I'm using.
Specifically, I have defined exclusion files for Linux and Windows based systems.
For Linix, the file is called `rsync-exclude-desktop` and `rsync-exclude-RPi` and look something like this:

```
- /var/lib/pacman/sync/*
- /lost+found
- /media/*
- /cdrom/*
- /proc/*
- /mnt/*
- /run/*
- /tmp/*
- /sys/*
- /dev/*
```

For Windows, the file is called `rsync-exclude-windows`:

```
- /cygdrive/c/System\ Volume\ Information/*
- /cygdrive/c/Windows/System32/winevt/*
- /cygdrive/c/Windows/System32/catroot/*
- /cygdrive/c/Windows/System32/catroot2/*
- /cygdrive/c/Windows/System32/config/*
- /cygdrive/c/Windows/ServiceProfiles/*
- /cygdrive/c/ProgramData/Microsoft/*
- /cygdrive/c/Windows/System32/wdi/*
- /cygdrive/c/Windows/System32/wfp/*
- /cygdrive/c/Windows/System32/sru/*
- /cygdrive/c/proc/sys/Device/*
- /cygdrive/c/proc/registry*
- /cygdrive/c/Windows/Logs/*
- /cygdrive/c/hiberfil.sys
- /cygdrive/c/pagefile.sys
- /cygdrive/c/swapfile.sys
- /proc/sys/Sessions/
- UsrClass.dat
- ntuser*
- NTUSER*
- *Cache*
- *cache*
- *Lock*
- *lock*
- *LOG*
- *log*
- *.tmp
```

To implement the above backup rules (and many others),
you need to edit a configuration file[^I] located at `/etc/rsnapshot.conf`.
The configuration elements I edited are below:

[^I]:
    **NOTE:**
    The configuration file requires tabs between elements
    and all drectories require a trailing slash.
    Just open config file using a text editor such as vi or gedit but be careful.
    Many editors are set to convert any tabs entered by the user to spaces.
    This can be a source of great confusion and frustration!

```
# location where backups will be stored
snapshot_root	/mnt/backup/

# rsync command executed on the remote system
cmd_rsync	/usr/bin/rsync

# incremental backup rules
retain		hourly	6
retain		daily	7
retain		weekly	4
retain		monthly	3

# rsnapshot's log file
logfile	/var/log/rsnapshot.log

# All rsync commands have at least these options set.
rsync_short_args	-aev
rsync_long_args	--delete --numeric-ids --relative --delete-excluded

# ssh args passed 
ssh_args	-i /home/backup_user/.ssh/id_rsa

# systems to be backed up, what high level directory name is to be used
# and the additional arguments to pass to rsync
backup	/	desktop/	exclude_file=/home/backup_user/rsync-exclude-desktop
backup	backup_user@RedRPi:/	RedRPi/	exclude_file=/home/backup_user/rsync-exclude-RPi,+rsync_long_args=--rsync-path=/home/backup_user/bin/rsync-wrapper.sh
backup	backup_user@BlackRPi:/	BlackRPi/	exclude_file=/home/backup_user/rsync-exclude-RPi,+rsync_long_args=--rsync-path=/home/backup_user/bin/rsync-wrapper.sh
backup	Sara@SaraPC:/	SaraPC/	exclude_file=/home/backup_user/rsync-exclude-windows,+rsync_long_args=--fake-super
```

In my backup scheme, I have several remote systems (i.e. RedRPi, BlackRPi, and SaraPC),
and a backup server itself (i.e. desktop).
All system will use a common user called `backup_user`,
whos only purpose is to support the backup process.
From the backup system, we'll be able to logon to each remote system using
the `backup_user` ssh public key.
The main trick is to set sudoers on the remote system such that it allow rsync
root access to `backup_user`,
and it tell rsnapshot to use additionnal parameters when calling rsync.
This all required to maintain the security of the remote systems, and was discussed in the text above.

### Testing rsnapshot
rsnapshot provides an easy way to check that your configuration file doesn’t contain any syntax errors.
Simply type:

```shell
sudo rsnapshot configtest
```

If all is well, it will say ‘syntax ok’.
If there is a problem, it will spit errors at you.
If you get errors, check that you have separated items in the file using tabs
(spaces are not allowed in the configuration file).

The final step to test your configuration is to run rsnapshot in test mode, using the `-t` option:

```shell
sudo rsnapshot -t hourly
```

This tells rsnapshot to simulate an "hourly" backup.
It should print out the commands it will perform when it runs for real.
If all is well, then remove the `-t` and run it for real to create the initial backup.
This initial run is likely to run a long time, and shouldn't be do via cron as discussed below.

### Scheduling (Automating) Backups in crontab 
Linux [cron][15][^J] is used to schedule commands to be executed periodically.
You can setup commands or scripts, which will be repeatedly run at a set time.

[^J]:
    **NOTE:**
    The cron service (daemon) runs in the background and constantly checks the `/etc/crontab` file,
    and `/etc/cron.*/` directories.
    It also checks the `/var/spool/cron/` directory.
    Review the article [CronHowTo][16] to see how you can schedule and run tasks
    in the background automatically at regular intervals using crontab files. 
    Crontab ( **cron** **tab**le ) is a file which contains the schedule of cron entries to be run and at specified times.
    (If the system isn't running 24x7, consider using [anacron][17]).

For crontab, I created a wrapper script and
placed it in `/home/backup_user/bin/rsnapshot-wrapper.sh`:

```shell
#!/bin/sh

# This script is a wrapper around rsnapshot, so status information is logged
 
# Place in the log file information concerning the execution of this script
echo -n "rsnapshot wrapper script started at " >> /home/backup_user/backup.log
date >> /home/backup_user/backup.log

echo -n "options passed to rsnapshot: " >> /home/backup_user/backup.log
echo $@ >> /home/backup_user/backup.log

# Now execute the script
/usr/bin/rsnapshot "$@" >> /home/backup_user/backup.log 2>&1;

echo -n "rsnapshot wrapper script completed at " >> /home/backup_user/backup.log
date >> /home/backup_user/backup.log

echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" >> /home/backup_user/backup.log
```

Using `crontab -e`, I enter the following:

```
#   minute  hour  day-of-month  month   day-of-week   command
      0     */4         *         *         *         /home/backup_user/bin/rsnapshot-wrapper.sh hourly
      30    2           *         *         *         /home/backup_user/bin/rsnapshot-wrapper.sh daily
      30    3           *         *         1         /home/backup_user/bin/rsnapshot-wrapper.sh weekly
      30    4           1         *         *         /home/backup_user/bin/rsnapshot-wrapper.sh monthly
```

You can use `sudo crontab -l` to list the contents of root's crontab. 

### Monitoring rsnapshot
Monitoring and testing is an essential part of any backup procedure.
There’s nothing worse than finding out
that your backup hasn’t been working for six months on the day that your system crashes.
rsnapshot has a log file that records warnings and error messages.
You can find/open it here: `/var/log/rsnapshot.log`
Inspect this log regularly to make sure your backup jobs are running smoothly.
You can increase or decrease the level of logging detail in the configuration file `/etc/rsnapshot.conf`.

### Backup from Windows Machines to Linux
Backing up Windows systems has its own special challages, but utilities exist to help.
[Cygwin][27] is a a collection of tools that provide a Linux look and feel environment for Windows.
If you install it, you can use linux commands and services on your Windows.
Cygwin contains a package with [its version of rsync][29]
to make backups from the Windows based computer.
With Cygwin's rsync and the rsnapshot running on the Linux backup server,
you can set up a remote backup for the Microsoft Windows box.

To do the install the cygwin `rsync`, `ssh`, etc. tools required to support the rsnapshot backup,
you'll follow a similar design pattern used above for the Linux boxes.
Follow this procedure:

##### Install Cygwin Tools
* From the [cygwin site][27], download and run the setup program.  (Make sure to keep the setup program, since it is used to install additional Cygwin packages, if you so desire.)
* Run your cygwin `setup.exe` and expand the categories to find "rsync" and "ssh".  You'll find them under the "Net" packages.
* When the install is complete, the `rsync` and `ssh` programs (and many more) will be located in `C:\cygwin64\bin`. (This is equivalent to `/bin` when your running a `bash` shell in cygwin.)
* In Windows, open a [Command Prompt (Admin) window][28].  Within this window, get a bash shell via the command `C:\cygwin64\bin\bash`.  Next execute `export Path=/bin:$PATH`.

##### Get ssh Operational
* Now make a home directory for the cygwin user, in my case this was `mkdir /home/Sara` and then `cd /home/Sara`.
* Create a `ssh` public/private keys with the following command: `ssh-keygen -t rsa`.
* Now start up the `ssh` services by following the instructions of "[Geek to Live: Set up a personal, home SSH server][26]".
* Find out the name of the windows syste via `hostname` (it's SaraPC).
* In order to access the `ssh` server from the backup Linux box, the `ssh` port of 22 must be open in the Windows Firewall. You can check ports status by attempting connect via `ssh` (e.g. `ssh Sara@SaraPC`).  If this command appears to hang or time out (as it did for me), the port is likely blocked.  You'll need to go to your [Windows Firewall][30] and open port 22.
* Transfer the public key for the `backup_user` on the Linux Backup server to `/home/Sara/.ssh/authorized_keys`.
* Make sure that in the files `/etc/ssh/sshd_config` and `/etc/ssh/ssh_config` that you have `RSAAuthentication yes` and `PubKeyAuthentication yes`.

##### Test ssh and rsync
* On the Linux Backup server, login as the `backup_user` user.
* Test the connection via `ssh Sara@SaraPC` in a terminal window on the Linux box (note to self: Case is important!).  You should login without a password.
* Test rsync via the command `sudo rsync -azv --fake-super Sara@SaraPC:/home/Sara /mnt/backup/rsync-test9`. You'll want to use the `--fake-super` option to surpress some i[issues with group ids][36].
* Test the `/etc/rsnapshot.conf` given earlier by running `rsnapshot hourly`.

### Restore Files with rsnapshot
Restoring files are an no brainer because the backups are plain directories.
You can open a file browser or a terminal, enter a snapshot from a few hours/days/weeks/months ago,
find a working directory where your files are store, and copy them to where their needed.
In other words, you can use any regular tools on any snapshot.
No need to “revert” or “restore” files from backup, or run any special software.
This is mighty convenient, intuitive, and fool proof.

### Sources
I found these articles useful for writing this post and setting up my rsych / rsnapshot backup scheme. 

#### rsync
* [How to Backup Linux? 15 rsync Command Examples](http://www.thegeekstuff.com/2010/09/rsync-command-examples/)
* [Rsync (Remote Sync): 10 Practical Examples of Rsync Command in Linux](http://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)
* [6 rsync Examples to Exclude Multiple Files and Directories using exclude-from](http://www.thegeekstuff.com/2011/01/rsync-exclude-files-and-folders/)
* [How to Setup Rsync with SSH on UNIX / Linux (rsync without password)](http://www.thegeekstuff.com/2011/07/rsync-over-ssh-without-password/)
* [Easy Automated Snapshot-Style Backups with Linux and Rsync](http://www.mikerubel.org/computers/rsync_snapshots/)
* [Full System Backup with rsync](https://wiki.archlinux.org/index.php/Full_System_Backup_with_rsync)

#### rsnapshot
* [Debian / Ubuntu Linux Install and Configure Remote Filesystem Snapshot with rsnapshot Incremental Backup Utility](http://www.cyberciti.biz/faq/linux-rsnapshot-backup-howto/)
* [Rsnapshot (Rsync Based) – A Local/Remote File System Backup Utility for Linux](http://www.tecmint.com/rsnapshot-a-file-system-backup-utility-for-linux/)
* [rsnapshot HOWTO](http://www.rsnapshot.org/howto/1.2/rsnapshot-HOWTO.en.html#create_the_config_file)
* [UNIX / Linux: Rsnapshot Restore Backups](http://www.cyberciti.biz/faq/restoring-backup-files-with-rsnapshot-unix-linux-bsd-appleosx/)
* [The "exclude-from" and "recursive" options](https://sites.google.com/site/rsync2u/home/rsync-tutorial/the-exclude-from-option)
* [Implementing Redundant Backups with rsnapshot](http://www.evbackup.com/support-misc-redundant-backups-with-rsnapshot/)

#### rsnapshot with root access
* [Root, Sudo, and Rsnapshot](http://technokracy.net/2011/01/07/root_sudo_rsnapshot/)
* [Backup remote Linux hosts without root access, using rsnapshot](http://dev.kprod.net/?q=linux-backup-rsnapshot-no-root)
* [Backing Up Multiple Servers with Rsnapshot](http://derek.simkowiak.net/backing-up-multiple-servers-with-rsnapshot/)

#### rsync and rsnapshot with Windows
* [Backup from Windows to Linux with Rsync and SSH](http://www.smellems.com/tiki-read_article.php?articleId=14)
* [Installing ssh and rsync on a Windows machine: minimalist approach](http://optics.ph.unimelb.edu.au/help/rsync/rsync_pc1.html)
* [Using rsync and cygwin to Sync Files from a Linux Server to a Windows Notebook PC](http://www.trueblade.com/knowledge/using-rsync-and-cygwin-to-sync-files-from-a-linux-server-to-a-windows-notebook-pc)
* [Rsync from Windows](http://terokarvinen.com/rsync_from_windows.html)



[01]:http://www.techrepublic.com/blog/10-things/10-outstanding-linux-backup-utilities/
[02]:http://rsync.samba.org/
[03]:http://en.wikipedia.org/wiki/Rsync
[04]:http://www.opbyte.it/grsync/
[05]:http://www.seagate.com/external-hard-drives/desktop-hard-drives/backup-plus-desk/
[06]:http://en.wikipedia.org/wiki/USB_3.0
[07]:http://www.diffen.com/difference/USB_2.0_vs_USB_3.0
[08]:http://www.rsnapshot.org/
[09]:http://www.thegeekstuff.com/2011/07/rsync-over-ssh-without-password/
[10]:http://en.wikipedia.org/wiki/NTFS
[11]:https://help.ubuntu.com/community/LinuxFilesystemsExplained
[12]:http://www.itechlounge.net/2012/01/linux-partition-and-format-external-hard-drive-as-ext3-filesystem/
[13]:http://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/
[14]:http://www.linfo.org/hard_link.html
[15]:http://en.wikipedia.org/wiki/Cron
[16]:https://help.ubuntu.com/community/CronHowto
[17]:http://www.thegeekstuff.com/2011/05/anacron-examples/
[18]:http://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html
[19]:http://xmodulo.com/2013/05/how-to-accept-ssh-host-keys-automatically-on-linux.html
[20]:https://help.ubuntu.com/community/RootSudo
[21]:http://www.garron.me/en/linux/remove-offending-key-ssh.html
[22]:http://stackoverflow.com/questions/9299651/warning-permanently-added-to-the-list-of-known-hosts-message-from-git
[23]:http://www.sudo.ws/sudo/sudoers.man.html
[24]:http://www.sudo.ws/visudo.man.html
[25]:http://www.cyberciti.biz/faq/howto-change-rename-user-name-id/
[26]:http://lifehacker.com/205090/geek-to-live--set-up-a-personal-home-ssh-server
[27]:http://www.cygwin.com/
[28]:http://www.howtogeek.com/howto/windows-vista/run-a-command-as-administrator-from-the-windows-vista-run-box/
[29]:http://cygwin.com/cgi-bin2/package-cat.cgi?file=x86%2Frsync%2Frsync-3.0.9-1&grep=rsync
[30]:http://windows.microsoft.com/en-us/windows/open-port-windows-firewall#1TC=windows-7
[31]:http://en.wikipedia.org/wiki/Inode
[32]:http://en.wikipedia.org/wiki/Block_(data_storage)
[33]:http://www.lostsaloon.com/technology/understanding-file-linking-hard-link-vs-symbolic-link-in-linux/
[34]:http://en.wikipedia.org/wiki/Symbolic_link
[35]:http://wiki.r1soft.com/display/TP/rsync+Backup
[36]:https://digitaldj.net/blog/2011/04/07/rsync-3-0-8-windows-and-chown/
[37]:http://security.stackexchange.com/questions/10532/ecdsa-keys-changed-ssh-insecure-now
[38]:
[39]:
[40]:
