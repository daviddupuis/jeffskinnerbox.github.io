Title: Tuning the RTL-SDR for Optimal Use
Date: 2100-01-01 00:00
Category: xxx
Tags: Electronics
Slug: RTL-SDR, Software Defined Radio
Author: Jeff Irland
Image: DRAFT_stamp.png
Summary: bla bla bla

You'll find that the dongle is limited by the following:

* frequency offset
* quality of the antenna
* sample rate you can obtain
* bandwidth of the device
* A/D bit resolution

Improving the Quality of the Antenna

* [Antenna-Theory.com][01]
* [Broadband Discone Antenna][02]
* [VE3SQB ANTENNA DESIGN PROGRAMS][03]
* [D.I.Y. Discone for RTLSDR][04]

## Determining Your Dongles Frequency Off-Set
Once you start playing around with any of the RTL-SDR dongles and some of the Software Defined Radio (SDR) tools out there, you observer that the frequency settings/readings your using don't make sense.
In fact, they seem to be way off, like tens of kHz off!  So any attempt to tune into a specific local radio station (like this for example:
`rtl_fm -W -f 99.5M | play -r 32k -t raw -e signed-integer -b 16 -c 1 -V1 -`) can often produce a very noisy / distorted signal or nothing intelligent at all.
One of the root cause of this is the low quality local oscillator used on the dongles.e
These oscillators frequency are engineered for a specific value (28.8MHz in the case of the RTL2832U-based USB DVB-T adapters dongle like mine) but will vary significantly among the device manufactured (it will also drift with temperature).

Now if you know how far off your dongles oscillators frequency was from its specification value, then you could compensate for it.
So in my `rtl_fm` example above, you would adjust the `-f 99.5M` parameter to compensate for the off-set.
Each unique device has its own off-set, so how do you determine your devices off-set?
Thanks to the [work of  Joshua Lackey and Steve Markgraf][05], there exist a tool to calculate this value.
That tool is called [kalibrate, or kal][06] (actually, we be using [kalibrate-rtl][07]
which is a fork of the software from [kalibrate][08]
and specifically designed for the RTL-SDR dongles) uses the precise known frequencies of used within GSM base stations to calculate the local oscillator frequency offset.
GSM base stations timing is required to be very accurate (to within 0.05 ppm), so if we can measure the dongles frequency relative to this very stable GSM frequency, we have an accurate measure of our dongles off-set.

In fact, there is a [video][09] on how to use this tool with RTL-SDR dongles.

``` bash
cd ~/src
git clone git://github.com/steve-m/kalibrate-rtl.git
cd kalibrate-rtl
./bootstrap &amp;&amp; CXXFLAGS='-W -Wall -O3'
./configure
make
```

I did the commands below because "make install" failed

``` bash
cd src
/usr/bin/install -c kal '/home/jeff/bin'
```

Data captured using kalibrate-rtl:

```
kal -s GSM850 --> channel 238 --> kal -c 238 --> -891.2MHz   30.254 ppm, -20.256 ppm
kal -s GSM900 --> channel 989 --> kal -c 989 --> 928.0MHz   26.225 ppm, 26.023 ppm
kal -s GSM900 --> channel 991 --> kal -c 991 --> 928.4MHz   7.793 ppm, -1.919 ppm
kal -s GSM900 --> channel 998 --> kal -c 998 --> 929.8MHz   1.712 ppm, 2.508 ppm
```

Baried with in the http://superkuh.com/

frequency offset

Kalibrate-RTL

[RTLSDR Scanner](http://eartoearoak.com/software/rtlsdr-scanner) is a simple cross platform python based spectrum analyzer for the RTL-SDR. The scanner also has an auto calibration feature which can help find the PPM offset of a dongle.

[HOW TO CALIBRATE RTL-SDR USING KALIBRATE-RTL ON LINUX][10]

<strong>Improving Your Dongles Antenna</strong>

[Home Made Coat Hanger Discone][11]

Improving Your SDR Radio

* [Adding more frequencies to your software defined radio][12]
* [Improving a software defined radio with a few bits of wire][13]
* [RTL-SDR Improvement Tips][14]


[01]:http://www.antenna-theory.com/
[02]:http://www.ramseyelectronics.com/downloads/manuals/DA25.pdf
[03]:http://www.ve3sqb.com/
[04]:http://helix.air.net.au/index.php/d-i-y-discone-for-rtlsdr/
[05]:https://github.com/steve-m/kalibrate-rtl
[06]:http://thre.at/kalibrate/
[07]:https://github.com/steve-m/kalibrate-rtl
[08]:http://thre.at/kalibrate/
[09]:http://www.youtube.com/watch?v=VaKzhaf5iKg
[10]:http://www.securitytube.net/video/7726
[11]:http://www.rtl-sdr.com/home-made-coat-hanger-discone/
[12]:http://hackaday.com/2012/07/08/adding-more-frequencies-to-you-software-defined-radio/
[13]:http://hackaday.com/2012/05/14/improving-a-software-defined-radio-with-a-few-bits-of-wire/
[14]:http://www.ab9il.net/software-defined-radio/rtl2832-sdr.html

