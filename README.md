About OSPD-DEBSECAN
-------------------

This is a OSP server implementation to allow GVM to remotely control
a debsecan scanner, see http://www.enyo.de/fw/software/debsecan/
OSPD-DEBSECAN identifies vulnerable packages on the Debian system it is
executed on.

Once running, you need to configure the Scanner for Greenbone Vulnerability
Manager, for example via the web interface Greenbone Security Assistant.
Then you can create scan tasks to use this scanner.

OSPD-DEBSECAN is licensed under GNU General Public License Version 2 or
any later version.  Please see file COPYING for details.

All parts of OSPD-DEBSECAN are Copyright (C) by Greenbone Networks GmbH
(see http://www.greenbone.net).


How to start OSPD-DEBSECAN
--------------------------

There are no special usage aspects for this module
beyond the generic usage guide.

The only exception is that starting a scan requires some more
paramaters:

$ gvm-cli socket --sockpath <prefix>/var/run/ospd-debsecan.sock \
  --xml "<start_scan target='127.0.0.1' ports=''><scanner_params/></start_scan>"


Generic usage guide for OSPD-based scanners
-------------------------------------------

Replace "scanner" by the name of the actual OSPD scanner.

All OSPD servers share a set of command-line options such as
--help, --bind-address, --port, --key-file, --timeout etc.

For example to see the command line options you can run

$ ospd-scanner --help


To run a test instance of ospd-scanner on unix socket:

$ ospd-scanner -u <prefix>/var/run/ospd-scanner.sock &

To run a test instance of ospd-scanner on local port 1234:

$ ospd-scanner -b 127.0.0.1 -p 1234 &

Add "--log-level=DEBUG" to enable maximum debugging output.

Parameter for --log-level can be one of debug, info, warnings, error, or
critical (in order of priority).


Controlling a OSP daemon
------------------------

You can use command line tools of "gvm-tools" module to send to and
receive information from the scanners.

Get a description of the interface:

$ gvm-cli socket --sockpath <prefix>/var/run/ospd-scanner.sock --xml "<help/>"

or

$ gvm-cli --use-certs -p 1234 -i --xml="<help/>"


Starting a scan (scanner parameters can be added according to the description
printed upon the command "<help/>":

$ gvm-cli socket --sockpath <prefix>/var/run/ospd-scanner.sock --xml="<start_scan target='www.example.com'></start_scan>"


Show the list of scans, their status and results:

$ gvm-cli socket --sockpath <prefix>/var/run/ospd-scanner.sock --xml="<get_scans/>"
