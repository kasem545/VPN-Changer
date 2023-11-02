# VPN-Changer
VPN-Changer is a proton vpn script that automatically change VPN's based on input time

## usage

```
usage: vpnchanger.py [-h] [-f] [-r] [-t] interval {tcp,udp}

Change ProtonVPN connection at specified intervals.

positional arguments:
  interval      Time interval in the format 'Ns' for seconds or 'Nm' for
                minutes.
  {tcp,udp}     Specify the protocol (TCP or UDP) to use.

options:
  -h, --help    show this help message and exit
  -f, --faster  Use the faster server option (-f or --faster).
  -r, --random  Use the random server option (-r or --random).
  -t, --tor     Use the Tor connection option (-t or --tor) with ProtonVPN.
```
