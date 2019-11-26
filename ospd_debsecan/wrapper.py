# -*- coding: utf-8 -*-
# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.

""" Setup for the OSP Debsecan Server. """

from ospd.ospd_ssh import OSPDaemonSimpleSSH
from ospd.main import main as daemon_main
from ospd_debsecan import __version__

OSPD_DESC = """
This scanner runs the tool 'debsecan' (Debian Security Analyzer) on the target hosts via a ssh connection.

This tool is available for Debian GNU/Linux systems and can create a list of vulnerabilities the present system is subject to.
The tool goes beyond a simple match about which package updates are missing.
It rather does an online query to learn about software packages where security problems are identified, but not yet been finally processed to become a security update.

A QoD of 97% (QoD type 'package' for authenticated package-based checks) is applied to any results.

Further details about the tool are available on the debsecan homepage:

http://www.enyo.de/fw/software/debsecan/

For executing debsecan a low privileged user account is sufficient on the respective target systems.
Also the tool 'debsecan' needs to be installed on the target systems.
"""


def process_output(output):
    """ Generates values for the add_scan_alarm method """
    for line in output:
        if not line.startswith('CVE-'):
            continue
        yield dict(name=line.split()[0], value=line)


class OSPDdebsecan(OSPDaemonSimpleSSH):

    """ Class for ospd-debsecan daemon. """

    def __init__(self, **kwargs):
        """ Initializes the ospd-debsecan daemon's internal data. """
        super().__init__(**kwargs)

        self.server_version = __version__
        self.scanner_info['name'] = 'debsecan'
        self.scanner_info[
            'version'
        ] = 'depends on the local installation at the target host'
        self.scanner_info['description'] = OSPD_DESC

    def check(self):
        """
        Checks that debsecan command line tool is found and is executable.
        Since this osp scanner uses local installations on many systems
        where on some systems it might be available and on others not be present,
        we simply return True.
        """

        return True

    def finish_host(self, scan_id, target):
        """ Set the host progress to 100 and the status to finished."""
        self.set_scan_host_progress(scan_id, target, target, 100)
        self.set_scan_host_finished(scan_id, target, target)

    def exec_scan(self, scan_id, target):
        """ Starts the debsecan scanner for scan_id scan. """

        result = self.run_command(scan_id=scan_id, host=target, cmd="debsecan")
        if result is None:
            self.add_scan_error(
                scan_id,
                host=target,
                value="A problem occurred trying to execute 'debsecan'.",
            )

            self.finish_host(scan_id, target)
            return 2

        for alarm in process_output(result):
            self.add_scan_alarm(
                scan_id,
                host=target,
                hostname='',
                **alarm,
                port='',
                test_id='',
                severity='',
                qod='97',
            )

        self.finish_host(scan_id, target)
        return 1


def main():
    """ OSP debsecan main function. """
    daemon_main('OSPD - debsecan wrapper', OSPDdebsecan)


if __name__ == '__main__':
    main()
