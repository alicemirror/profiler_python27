##
# @file disabled_profiler.py
# @package profiler
# @brief Helper methods doing nothing when profiler is disabled
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version. \n
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.\n
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/ \n
#
# @date March 2016
# @author Enrico Miglino <enrico.miglino@gmail.com>
# @version 0.1.3
# @version documentation version 0.4

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

    def module_stats(self, module = None, comment = None):
        pass

    def statistics_calls(self):
        pass

    def module_stats_calls(self, module = None, comment = None):
        pass
