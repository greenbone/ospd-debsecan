# -*- coding: utf-8 -*-
# Description:
# Test-Suite for the debsecan processing
#
# Authors:
# Benoît Allard <benoit.allard@greenbone.net>
#
# Copyright:
# Copyright (C) 2015 Greenbone Networks GmbH
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

import unittest

from ospd_debsecan.wrapper import process_output

class testProcessOutput(unittest.TestCase):

    def testCVENoComment(self):
        res = list(process_output(["CVE-2014-5044 gcc-4.6"]))
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0], dict(name='CVE-2014-5044', value='CVE-2014-5044 gcc-4.6'))

    def testCVEWithComment(self):
        res = list(process_output(["CVE-2002-2439 gcc-4.6 (low urgency)"]))
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0], dict(name='CVE-2002-2439', value='CVE-2002-2439 gcc-4.6 (low urgency)'))

    def testNoCVE(self):
        res = list(process_output(["TEMP-0000000-EA424A libbluray1"]))
        self.assertEqual(len(res), 0)
       
