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


import sys
from hsn2objectwrapper import Object
sys.path.append("/opt/hsn2/python/commlib")
from hsn2taskprocessor import HSN2TaskProcessor, ParamException

class UrlFeederTaskProcessor(HSN2TaskProcessor):
	
	ORIGIN = 'input'

	def paramsToDictionary(self):
		result = {}
		for param in self.currentTask.parameters:
			result[param.name] = param.value
		return result
	
	def taskProcess(self):
		parameters = self.paramsToDictionary()
		if 'url' not in parameters:
			raise ParamException
		urlObject = Object()
		urlObject.addString('url_original', parameters['url'])
		urlObject.addString('origin', self.ORIGIN)
		urlObject.addString('type', 'url')
		if 'referrer' in parameters:
			urlObject.addString('referrer', parameters['referrer'])
		newObjectId = self.osAdapter.objectsPut(self.currentTask.job, self.currentTask.task_id, [urlObject])
		self.newObjects.extend(newObjectId)
			
	def cleanup(self):
		pass
