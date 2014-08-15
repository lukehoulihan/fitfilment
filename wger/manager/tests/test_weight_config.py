# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

import logging

from wger.core.tests import api_base_test
from wger.manager.models import WeightConfig


logger = logging.getLogger('wger.custom')


class WeightConfigApiTestCase(api_base_test.ApiBaseResourceTestCase):
    '''
    Tests the schedule weight config resource
    '''
    pk = 1
    resource = WeightConfig
    private_resource = True
    data = {"schedule_step": 4,
            "setting": 3,
            "start": 3,
            "increment": 2}