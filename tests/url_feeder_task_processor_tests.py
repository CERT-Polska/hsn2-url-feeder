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

import unittest
from hsn2urlfeedertaskprocessor import UrlFeederTaskProcessor
from hsn2taskprocessor import ParamException


class MockObject:

    def __init__(self):
        self.added = {}

    def addString(self, parameter, value):
        self.added[parameter] = value


class MockTask:

    def __init__(self, url=None, referrer=None):
        self.parameters = []
        if url is not None:
            self.parameters.append(MockParameter('url', url))
        if referrer is not None:
            self.parameters.append(MockParameter('referrer', referrer))
        self.job = 123
        self.task_id = 321


class MockParameter:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class MockOsAdapter(object):

    def __init__(self):
        self.objects = []

    def objectsPut(self, job, task, objects):
        if job == 123 and task == 321:
            self.objects.extend(objects)
            return [987] * len(objects)
        else:
            raise Exception()


class UrlFeederTaskProcessorTest(unittest.TestCase):

    def testExceptionWhenNoUrl(self):
        urlFeeder = UrlFeederTaskProcessor(None, None, "bogusServiceName", "bogusQueue", "bogusOsQueue")
        urlFeeder.currentTask = MockTask()
        self.assertRaises(ParamException, urlFeeder.taskProcess)

    def checkCommonAttributes(self, newObject):
        self.assertEquals(newObject.origin, "input")
        self.assertEquals(newObject.type, "url")

    def testCorrectProcessing(self):
        urlFeeder = UrlFeederTaskProcessor(None, None, "bogusServiceName", "bogusQueue", "bogusOsQueue")
        mockObject = MockObject()
        urlFeeder.objects = [mockObject]
        urlFeeder.currentTask = MockTask("http://example.com", "http://www.google.com")
        urlFeeder.osAdapter = MockOsAdapter()
        urlFeeder.newObjects = []

        urlFeeder.taskProcess()

        self.assertEquals(mockObject.added, {})
        self.assertEquals(len(urlFeeder.newObjects), 1)
        self.assertEqual(urlFeeder.newObjects[0], 987)
        self.assertEquals(len(urlFeeder.osAdapter.objects), 1)
        newObject = urlFeeder.osAdapter.objects[0]
        self.assertEquals(newObject.url_original, "http://example.com")
        self.assertEquals(newObject.referrer, "http://www.google.com")
        self.checkCommonAttributes(newObject)

    def testCorrectProcessingWithoutReferrer(self):
        urlFeeder = UrlFeederTaskProcessor(None, None, "bogusServiceName", "bogusQueue", "bogusOsQueue")
        mockObject = MockObject()
        urlFeeder.objects = [mockObject]
        urlFeeder.currentTask = MockTask("http://www.wp.pl")
        urlFeeder.osAdapter = MockOsAdapter()
        urlFeeder.newObjects = []

        urlFeeder.taskProcess()

        self.assertEquals(mockObject.added, {})
        self.assertEquals(len(urlFeeder.newObjects), 1)
        self.assertEqual(urlFeeder.newObjects[0], 987)
        self.assertEquals(len(urlFeeder.osAdapter.objects), 1)
        newObject = urlFeeder.osAdapter.objects[0]
        self.assertEquals(newObject.url_original, "http://www.wp.pl")
        self.checkCommonAttributes(newObject)

if __name__ == "__main__":
    #import sys
    #sys.argv = ['', 'Test.testName']
    unittest.main()
