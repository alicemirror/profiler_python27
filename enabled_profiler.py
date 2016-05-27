## @file enabled_profiler.py
# @package profiler
# @brief Helper methods managing the cProfile package
#
# cProfile provide deterministic profiling of Python programs.\n\n
# The profiler modules are designed to provide an execution profile for a given program. The profiler introduce a small
# overhead to the Python code execution so it is not reliable for a production environment. Anyway, instantiating the
# Profiler class with with the enable flag set to false this overhead is reduced to a very low impact to the program
# flow execution timing.\n\n
# For details on how the cProfile Python component works, theck the Python documentation "The Pythong Profilers"
# (link: https://docs.python.org/2/library/profile.html#module-cProfile)
#
# In addition to the time profiler the memory profile is also available as an option. For more information on the
# memory_profile package works see the package details on pythong.org: https://pypi.python.org/pypi/memory_profiler
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

import cProfile, pstats
from memory_profiler import memory_usage

## The timing profiler class instance
timingProf = cProfile.Profile()

##
# EnabledProfiler class exposes the methods for the profiling when the Profiling is enabled
#
class EnabledProfiler:

    ##
    # Constructor
    def __init__(self, outFilename = None):
        ## Initialises the flag to avoid multiple instances of the memory sampling class
        self.is_sammpling_memory = False

        # Check for filename if reqiored
        if outFilename is not None:
            self.streamFile = outFilename
            self.streaming = True
        else:
            self.streaming = False

    ## Start profiling the code execution.
    def enable(self):
        timingProf.enable()

    ##
    # Start memory usage sampling instantiating the memory usage class
    #
    # In the low level function memory_usage from the same module the timout
    # is set to none, allowing the memory profiling in long execution time
    # functions. In this last case the default sample frequency of 1 second
    # returns a good indication of the memory usage along the time.\n\n
    # Accordingly with the source method definition in the memory_usage module as shown below
    # \code
    #    memory_usage(proc=-1, interval=.1, timeout=None, timestamps=False,
    #                 include_children=False, max_usage=False, retval=False,
    #                 stream=None)
    #\endcode
    # the \b memory_usage call preset values:\n
    # <ul>
    # <li>\e Process: always refers to the current calling process</li>
    # <li>\e Timeout: set to false, no limit for the sampling period</li>
    # <li>\e Timestamp: set to false. Need to be true for having the time of every sample</li>
    # <li>\e Include \e Childrens: the associted childern functions. Set to false</li>
    # <li>\e Max \e Usage: set to false, no limit of max usage memory to sample</li>
    # <li>\e Return \e Value: set to true, to get the total sampled value as the return call</li>
    # <li>\e Stream: set to false, data are not streamed on an opene file channel</li>
    # </ul>
    #
    # @todo Implement a parsing of the memory data array for better reporting
    #
    # @param interval The frequency the amount of memory should be sampled
    # @param comment An optional comment stamped when the memory usage is shown
    def memory(self, interval = 1, comment = ''):
        if not self.is_sammpling_memory:
            self.is_sammpling_memory = True
            self.comment = comment
            self.memoryProf = memory_usage(-1, interval, None, False, False, False, True, None)

    ## Stop collecting data
    def disable(self):
        timingProf.disable()

    ## Stop collecting data and record the results internally as the current profile.
    def create_stats(self):
        timingProf.create_stats()

    ## Create a stats object based on the current profile and print the results to stdout.
    def print_stats(self):
        timingProf.print_stats()

    ## Write the results of the current profile to fname file
    def dump_stats(self, fname):
        timingProf.dump_stats(fname)

    ## Profile the command via exec()
    # Not used, for cProfile full compatibility only
    # @todo Method not implemented yet
    def run(self, command):
        pass

    ## Profile the command via exec() with the specified global and local environment.
    # Not used, for cProfile full compatibility only
    # @todo Method not implemented yet
    def runctx(self, command, globals, locals):
        pass

    ##
    # Profile a function call. Not used, for cProfile full compatibility only
    # @todo Method not implemented yet
    def runcall(self, func, args, kwargs):
        pass

    ## Stop collecting profiling data and generates a satistics report
    #
    # After the statistics object has been created, some adjustments are done for better readability of the
    # results: \n
    # long directory names are stripped from the modules (file names)\n
    # statistics are sorted based on the followind keys (from left to right, by level sorting)\n\n
    #
    # Module name, Function name, Internal time
    def statistics(self):
        # Check for alternative out than stdout
        if self.streaming:
            # Open stream for writing
            self.streamStats = open(self.streamFile, 'a')
            stats = pstats.Stats(timingProf, stream=self.streamStats)
        else:
            stats = pstats.Stats(timingProf)

        timingProf.create_stats()
        stats.strip_dirs()
        stats.sort_stats('module', 'name', 'time')
        stats.print_stats()

        # close the streaming
        self.streamStats.close()

    ##
    # Stop collecting profiling data and generates a satistics graphic report for callers and callees
    #
    # After the statistics object has been created, some adjustments are done for better readability of the
    # results: \n
    # long directory names are stripped from the modules (file names)\n
    # statistics are sorted based on the followind keys (from left to right, by level sorting)\n\n
    #
    # Module name, Function name, Internal time
    def statistics_calls(self):

        # Check for alternative out than stdout
        if self.streaming:
            # Open stream for writing
            self.streamStats = open(self.streamFile, 'a')
            stats = pstats.Stats(timingProf, stream=self.streamStats)
        else:
            stats = pstats.Stats(timingProf)

        timingProf.create_stats()
        stats.strip_dirs()
        stats.sort_stats('module', 'name', 'time')
        stats.print_callers()
        stats.print_callees()

    ##
    # Generate the output of the acquired memory usage
    # If the memory sampling is not active any output is generated
    def mem_used(self):
        if self.is_sammpling_memory:
            print "------------------------------------------------"
            print "Memory usage (in Mb)"
            print self.comment
            print self.memoryProf
            print "------------------------------------------------"

    ##
    #   Stop collecting profiling data and generates a satistics report for a specific module
    #
    #   After the statistics object has been created, some adjustments are done for better readability of the
    #   results: \n
    #   long directory names are stripped from the modules (file names)\n
    #   statistics are sorted based on the followind keys (from left to right, by level sorting)\n\n
    #
    #   Module name, Function name, Internal time\n\n
    #
    #   At last the statistics report is restricted to the specific module
    #
    #   \note If the module is not specified (default = None) this method has the same effect of statustucs()
    def module_stats(self, module = None):

        if module == None:
            self.statistics()
        else:
            # Check for alternative out than stdout
            if self.streaming:
                # Open stream for writing
                self.streamStats = open(self.streamFile, 'a')
                stats = pstats.Stats(timingProf, stream=self.streamStats)
            else:
                stats = pstats.Stats(timingProf)

            # Generate the statistics output
            timingProf.create_stats()
            stats.strip_dirs()
            stats.sort_stats('name', 'ncalls', 'time')
            stats.print_stats(module)

    ##
    #   Stop collecting profiling data and generates a satistics report for a specific module if needed.
    #   After the statistics object has been created, some adjustments are done for better readability of the
    #
    #   results: \n
    #   long directory names are stripped from the modules (file names)\n
    #   statistics are sorted based on the followind keys (from left to right, by level sorting)\n\n
    #
    #   Module name, Function name, Internal time\n\n
    #
    #   At last the statistics report is restricted to the specific module
    #
    #   \note If the module is not specified (default = None) this method has the same effect of statustucs()
    def module_stats_calls(self, module = None):

        if module == None:
            self.statistics()
        else:
            # Check for alternative out than stdout
            if self.streaming:
                # Open stream for writing
                self.streamStats = open(self.streamFile, 'a')
                stats = pstats.Stats(timingProf, stream=self.streamStats)
            else:
                stats = pstats.Stats(timingProf)

            timingProf.create_stats()
            stats.strip_dirs()
            stats.sort_stats('name', 'ncalls', 'time')
            stats.print_callees(module)
