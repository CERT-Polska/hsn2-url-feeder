#!/usr/bin/python -tt

# Copyright (c) NASK
#
# This file is part of HoneySpider Network 2.0.
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

from hsn2_commons.hsn2service import HSN2Service
from hsn2_commons.hsn2service import startService
from hsn2_url_feeder.hsn2urlfeedertaskprocessor import UrlFeederTaskProcessor


class UrlFeederService(HSN2Service):
    serviceName = "url-feeder"
    description = "HSN 2 URL Feeder Service"

    def extraOptions(self, parser):
        return parser

    def sanityChecks(self, cliargs):
        return True

if __name__ == '__main__':
    startService(UrlFeederService, UrlFeederTaskProcessor)
