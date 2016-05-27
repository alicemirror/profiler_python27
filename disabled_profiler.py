##
# @file disabled_profiler.py
# @package profiler
# @brief Helper methods doing nothing when profiler is disabled
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n
#
# Copyright NXP PLMA.  All Rights Reserved.\n
#
# Licensed under the Apache License, Version 2.0 (the "License");\n
# you may not use this file except in compliance with the License.\n
# You may obtain a copy of the License at\n
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.  See the License for the specific language
# governing permissions and limitations under the License.
#
# @date March 2016
# @author Enrico Miglino <enrico.miglino@gmail.com>
# @version 0.1.5
# @version documentation version 0.5

class DisabledProfiler:
    ##
    # The disabledProfiler class exposes null methos for the case the profiling is not enabled by
    # the calling application.

    def __init__(self):
        pass

    def mem_used(self):
        pass

    def memory(self, interval = 1, comment = ''):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def create_stats(self):
        pass

    def print_stats(self):
        pass

    def dump_stats(self):
        pass

    def run(self, command = None):
        pass

    def runctx(self, command = None, globals = None, locals = None):
        pass

    def runcall(self, func = None, args = None, kwargs = None):
        pass

    def statistics(self):
        pass

    def module_stats(self, module = None):
        pass

    def statistics_calls(self):
        pass

    def module_stats_calls(self, module = None):
        pass
