Title: HOWTO: Setup SIP Phone/Multimedia Service
Date: 2014-02-21 18:20
Category: HowTo, Software
Tags: VoIP, SIP, Multimedia 
Slug: howto-setup-sip-phone-multimedia-service
Author: Jeff Irland
Image: how-too.jpg
Summary: bla bla bla
Status: draft

The [Session Initiation Protocol (SIP)][01] is a signaling communications protocol,
widely used for controlling multimedia communication sessions such as
voice (VoIP), video calls, instant messaging (IM), presence information,
and other media over Internet Protocol (IP) networks.
It is an application layer protocol designed to be independent of the underlying transport layer.
it can run on Transmission Control Protocol (TCP), User Datagram Protocol (UDP)
or Stream Control Transmission Protocol (SCTP).
It is a text-based protocol,
incorporating many elements of the Hypertext Transfer Protocol (HTTP)
and the Simple Mail Transfer Protocol (SMTP).
SIP works in conjunction with several other protocols, such as the
Real-time Transport Protocol (RTP) and Real-time Transport Protocol (RTP),
that identify and carry the session for the media.
To establish a SIP enabled application, you'll need to stand-up a SIP Server
or subscribe to a [SIP Service Provider][02].

In this article, I will first show how to leverage a SIP Service Provider
to support your voice/multimedia application.

## Establishing a SIP Account With Service Provider
I'm using SIP2SIP as my service provider ([wiki here][03] and [registration here][04]).
SIP2SIP supports audio, video, presence, chat, file transfer, and multiparty conferencing
based on SIP signaling and related media protocols (RTP, MSRP and XCAP).
Many SIP Service Providers only support VoIP, but that not the case with SIP2SIP.
The service is free to use based on a fair-use policy and federates with external SIP and XMPP domains.

Registering with SIP2SIP is simple to do and requires no instructions here.
I established multiple SIP accounts so that I could test conferancing.

## Installing SIP Client
As an initial test, I'll install a SIP client on my Linux desktop and
another client on 
#### Blink
There are many [SIP clients][^A] that I could choose from.
SIP2SIP recommends [Blink][05] for its client.
The [Linux version of Blink][06] comes in executable and source code[^B]
and has a sparce amount of [documentation][08].
Blink supports VoIP, chat, and file transfer, but not video.
Blink is not part of the standard software packages on my Linux box,
so I need to add the package archive location into my Linux package resource list.
To make it part of the package resource list, you need to update the `/etc/apt/sources.list` file.
To do this, do the following:

[^A]:
    A SIP client is a RTC (real-time communications) client that uses SIP (Session Initiation Protocol)
    to establish and maintain RTC sessions via a SIP server.
[^B]:
    They also supply [SIP SIMPLE client Software Development Kit (SDK)][07]
    for easy development of SIP multimedia end-points with features beyond VoIP
    like Session based Instant Messaging, File Transfers, Desktop Sharing and Presence.

```shell
sudo vim /etc/apt/sources.list
```

Scroll to the bottom of the file and enter the following information and then save:

```shell
## The SIP client Blink is not part of Ubuntu archives, but is offered by AG Projects
deb http://ag-projects.com/ubuntu saucy main 
```

Install AG Projects software signing key:

```shell
wget http://download.ag-projects.com/agp-debian-gpg.key 
sudo apt-key add agp-debian-gpg.key
```

Now install the Blink software package:

```shell
sudo apt-get update
sudo apt-get install blink
```

#### Getting Linphone Operational
On the Unbuntu Linux systems `desktop`

* **Install WebCam -** Using a Logitech QuickCam Sphere MP (aka QuickCam Orbit MP). This device has a microphone but no speaker.
* **Test Speaker -** Test the speaker out by `speaker-test -t sine -f 440 -c 2 -s 1`.
* **Test WebCam -** Test the webcam's video and microphone by recording a short video with (see [post][23] to find the audio device, [man page][25] and [documentation][24]). Once recorded, play the video and make sure its captured and it has audio. You can record a video with:

```shell
avconv -f video4linux2 -r 25 -i /dev/video0 -f alsa -i plughw:U0x46d0x994,0 -ar 22050 -ab 64k -strict experimental -acodec aac -vcodec mpeg4 -y ~/tmp/webcam_test.mp4
```

>NOTE: For the Logitech QuickCam Pro 9000, the replace `plughw:U0x46d0x994,0` with `plughw:Q9000,0`.

* **Install Linphone -** You can install the linphone software via `sudo apt-get install linphone`
* **Standalone Linphone Test -**

On the Raspberry Pi system `BlackRPi` 

* **Install Tools -** The `avconv` tool needs to be installed via `sudo apt-get install ffmpeg`. THe video play can be installed with `sudo apt-get install omxplayer`.
* **Install Speaker -** Plug in a speak into the audio jack of the RPi.
* **Test Speaker -** Test the speaker out by `speaker-test -t sine -f 440 -c 2 -s 1`.
* **Install WebCam -** Using a Logitech QuickCam Pro 9000. This device has a microphone but no speaker.
* **Test WebCam -** Using the same procedure as above for recording a video but replace `plughw:U0x46d0x994,0` with `plughw:Q9000,0`. To play back this recording, use the following:

```shell
mplayer ~/tmp/webcam_test.mp4
```

>NOTE: I did get complaints from mplayer that the harware was too slow for the video format.

>NOTE: For playing the video out the HDMI port on the Raspberry Pi, use `omxplayer -o hdmi ~/tmp/webcam_test.mp4`.

* **Install Linphone -** You can install the linphone software via `sudo apt-get install linphone`
* **Standalone Linphone Test -**

## Zeroconf plugin for sipwitch
This plugin activates zeroconf network services for sipwitch and publishes sipwitch as a sip service. In theory zeroconf aware SIP user agents should then be able to automatically connect to sipwitch without configuration.
http://packages.ubuntu.com/lucid/sipwitch-plugin-zeroconf

[01]:http://en.wikipedia.org/wiki/Session_Initiation_Protocol
[02]:http://en.wikipedia.org/wiki/SIP_provider
[03]:http://wiki.sip2sip.info/projects/sip2sip
[04]:https://mdns.sipthor.net/register_sip_account.phtml
[05]:http://icanblink.com/
[06]:http://projects.ag-projects.com/projects/documentation/wiki/Repositories
[07]:http://sipsimpleclient.org/
[08]:http://icanblink.com/help-qt.phtml
[09]:
[10]:
