[![CircleCI](https://circleci.com/gh/greenbone/ospd-debsecan.svg?style=svg)](https://circleci.com/gh/greenbone/ospd-debsecan)

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

Please follow the general usage guide for ospd-based scanners:

  https://github.com/greenbone/ospd/blob/master/doc/USAGE-ospd-scanner

Noteworthy is that starting a scan requires a ssh credential parameter because
ospd-debsecan needs to log into the target systems to run the locally installed
debsecan tool.

