Title: HowTo: Using Xephyr to Create a New Display in a Window
Date: 2100-01-01 00:00
Category: Software
Tags: X Window System, Xnest, Xephyr
Slug: howto-using-xephyr-to-create-a-new-display-in-a-window
Author: "Jeff Irland"
Image: DRAFT_stamp.svg
Summary: bla bla bla
Status: You might want to run one X Window System desktop environment on your local computer while accessing second computer, including its own desktop environment, using the first computer’s screen and keyboard.  This is known as "X nesting".  Open-source clients such as Xnest and Xephyr support such X nesting.

You might want to run one X Window System desktop environment on your local computer while accessing second computer,
including its own desktop environment, using the first computer’s screen and keyboard.
This sounds like multiple X Servers running, one for the monitor and
the other managing a graphics window as if it were a second monitor. 
Fortunately, X Window System provides tools to do exactly this.
An X client can be designed to emulate an X Server by providing display services to other clients.
This is known as "X nesting".
Open-source clients such as `Xnest` and `Xephyr` support such X nesting.

`Xnest` is a display server implementing the X11 display server protocol that shows its output in a window.
`Xnest` is a standard part of the XFree86 and X.org X Servers,
and provides an X server that runs inside a standard X Window. 
In other words, `Xnest` opens a window that works like another screen in which the user can open windows, etc.
At the X Protocol level, `Xnest` works like a X Client of the X server hosting the window,
and as a X Server with respect to the X Window Manager
(i.e.applications that opens windows) within the `Xnest` session.
Therefore, `Xnest` can be used to run a virtual desktop of another computer
(which is running X Window) within a window. 

# My Native Desktop Environment
For my X Window System, I'm running Lightweight X11 Desktop Environment (LXDE)
which has `lxdm` as its X Display Manager (aka GUI Login Manager),
and uses `lxsession` as it X Session Manager,
and the `Metacity` X Window Manager.
In the examples below, I sometimes use other compoents to demonstrate the robustness of the approach.
Speicfically, I'm using the [Awesome X Windows Manager][01]/
This can be load with the following:

```
sudo apt-get install awesome awesome-extra
```

# Xnest
`Xnest` might come pre-installed in the Ubunutu X Window System
but it's easy to install and is [easy to use][02].
Sinply install the package.  No special configuration is require.

```
sudo apt-get install xnest
```

### Simple Test of Xnest
To open a window containing a new X Display (i.e. display :3) and running xclock,
execute the following commands in an `xterm`.

```
Xnest :1 -geometry 1280x1024+200+200 -name "Xnest Test Window" 2> /dev/null &
xclock -display :1 &
```

The options have the following purpose:

* **:1** is your display (displays are numbered starting with 0)
* **-geometry 1280x1024+200+200** sets the window size and position
* **-name "Xnest Test Window"** is the title of the Xnest window
* **2> /dev/null** redirects trace and error messages

In the above, there isn't a window manager.
To include a window manager, you simple need to start one up, but again, within display :3.
And you can tile on a `xterm` and the `xeye`.

```
DISPLAY=:1 awesome &
DISPLAY=:1 xterm &
DISPLAY=:1 xeyes &
```

# Xephyr
You can think of [`Xephyr`][03] as an improved `Xnest`
and the use of the `Xephyr` X Server instead of `Xnest` is generally recommended.
You can install `Xephyr` with the following.

```
sudo apt-get install xserver-xephyr
```

### Simple Test of Xephyr
To open a `Xephyr` window with a specific size and surpress trace / error messaging,
do the following:

```
Xephyr -ac -screen 1280x1024 -br -reset -terminate 2> /dev/null :1 &
```

The options have the following purpose:

* **:1** is your display (displays are numbered starting with 0)
* **-ac** disable access control restrictions (allow you to forward X)
* **-screen 1280x1024** sets the window size
* **-br** set the background to black
* **-reset** reset after last client exists
* **-terminate** terminate `Xephyr` at server reset (does not always work)
* **2> /dev/null** redirects trace and error messages

To add a `xterm` into another account amd a and the Genome Window Manager, you could do the following:

```
Xephyr -ac -screen 1280x1024 -br -reset -terminate 2> /dev/null :1 &
DISPLAY=:1.0 gnome-wm &
DISPLAY=:1.0 ssh -X jennie@desktop xterm
```

Or you could start a Gnome Desktop session, and this will being with it its display manager

```
Xephyr -ac -screen 1280x1024 -br -reset -terminate 2> /dev/null :1 &
DISPLAY=:1 gnome-session &
DISPLAY=:1.0 ssh -XfC jennie@desktop xterm
```

This doesn't give you the full desktop envinronment.
The best way to do this is to go throught the X Display Manager (aka GUI Login Manager).
This is shown below in the next section.

### Remote Login
`Xephyr` and `Xnest` can also be used to [remotely login to a desktop session][05].
When remotely starting a X Window System desktop,
[XDMCP (X Display Manager Control Protocol)][04] is typically used to establish
the connection between the remote's X Display Manager (XDM) daemon
and the local X Server.
Once the connection has been established, and the user has successfully authenticated,
the XDM daemon launches the X client session, which is displayed on the user's workstation.

XDMCP suffers from some of the same security problem as all the X Protocals,
but unfortunately, cannot be tunnelled over SSH due to it's use of UDP.
Attempts to use XDMCP to connect to a remote system
via SSH will fail and an error message will be displayed.

For security reasons,
XDMCP is not enabled by default on most modern UNIX distributions.
You will have to enable remote logins to your X Display Manager.
To enable XDMCP on my LXDE based system,
I configuring the file `/etc/lightdm/lightdm.conf` so it contains

```
[SeatDefaults]
user-session=ubuntu
autologin-user=false
xserver-allow-tcp=true
greeter-session=unity-greeter

[XDMCPServer]
enabled=true
port=177
#key=
```

The key enabler here is the term `enabled=true`.

Now get out of X Window and restart the lightdm with `sudo restart lightdm`
or reboot your system so the changes take effect.
To log into into my Ubunutu system, from the say system as if they are remote to each other,
I used the following command works well. 

```
Xephyr -ac -screen 1280x1024 -br -reset -terminate -query desktop 2> /dev/null :1 &
```

The new option **-query desktop** cause `Xephyr` to contact the host computer `desktop` via XDMCP.

I attempted to do the same with `Xnest` via the command
`Xnest :1 -geometry 1280x1024+200+200 -query desktop &`
and found that it didn't fully work.

[Ubuntu – Secure Remote Desktop Connectivity](http://blog.linuxacademy.com/linux/ubuntu-secure-remote-desktop-connectivity/)
[Linux-Based X Terminals with XDMCP](http://www.linuxjournal.com/article/6713)
[Setting Up an X Terminal](http://zweije.home.xs4all.nl/xauth-9.html)

[The Tiny X Server Fork Is Still Being Maintained](http://www.phoronix.com/scan.php?page=news_item&px=MTU2NzA)

[Can I run a remote X session in windowed mode?](http://askubuntu.com/questions/60364/can-i-run-a-remote-x-session-in-windowed-mode)

[Remote x-server with ssh -X](http://www.answeredubuntu.com/175902/remote_x_server_with_ssh_x#sthash.ifsk3uxx.dpbs)
[How to try the GDM login screen in many resolutions](http://ptspts.blogspot.com/2010/02/how-to-try-gdm-login-screen-in-many.html)
[Remote sessions via XDMCP](http://x.cygwin.com/docs/ug/using-remote-session.html)
[X without Display Manager](http://wiki.gentoo.org/wiki/X_without_Display_Manager)


[Remote Graphical Desktops and XDMCP](https://www.centos.org/docs/5/html/5.2/Installation_Guide/s2-trouble-remotex.html)
[Starting a Remote X session using XDMCP](http://forums.opensuse.org/showthread.php/466709-Starting-a-Remote-X-session-using-XDMCP)
[Starting a UNIX/Linux Desktop Using SSH](http://support.attachmate.com/techdocs/1818.html)


[How to use XDMCP+GDM and Xnest?](http://askubuntu.com/questions/11189/how-to-use-xdmcpgdm-and-xnest)
[xdmcp](https://wiki.ubuntu.com/xdmcp)
[Windows Managers vs Login Managers Vs Display Managers Vs Session Manager Vs Desktop Environment](http://unix.stackexchange.com/questions/20385/windows-managers-vs-login-managers-vs-display-managers-vs-desktop-environment)
[Multiseat Configuration/Xnest](http://en.wikibooks.org/wiki/Multiseat_Configuration/Xnest)



[01]:http://awesome.naquadah.org/
[02]:http://box.matto.nl/xnest.html
[03]:http://nims11.wordpress.com/2012/06/24/nested-x-servers-with-xephyr/
[04]:http://www.x.org/releases/X11R7.7/doc/libXdmcp/xdmcp.html
[05]:http://techpad.co.uk/content.php?sid=72
[06]:
[07]:
[08]:
[09]:
[10]:
