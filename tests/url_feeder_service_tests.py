# Copyright (c) NASK
#
# This file is part of HoneySpider Network 2.1.
#
# This is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from hsn2_url_feeder.hsn2urlfeederservice import UrlFeederService


class UrlFeederTest(unittest.TestCase):

    def testSanityChecks(self):
        self.assertTrue(UrlFeederService(None).sanityChecks(None), True)

    def testExtraOptions(self):
        parser = object()
        self.assertTrue(UrlFeederService(None).extraOptions(parser), parser)


if __name__ == "__main__":
    #import sys
    #sys.argv = ['', 'Test.testName']
    unittest.main()
