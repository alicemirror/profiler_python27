##
# @file profile.py
# @package profiler
# @brief Profiler class for application timing statistics
#
#	@mainpage Profiler package
#	The profiler package includes a wrapper for the case when the profile should be disabled, calling a set of methods
#	doing nothing, for a maximum reduction of the extra processing time when the profiled program runs.\n
#	Methods of the profiler package replicates some methods exposed by the Python profiler cProfile, plus other high
#   level methods producing statistical reporting on the profiler instance and memory analisys.
#	Any of these methods are working only when the Profiler package instance has been called with the enable flag
#   is_enabled set to True else have no effect.
#
#   @note The profile methods integrates the memory profiling package memory_profiler. The memory profiling methods
#   can be used together or independently by the timing profiling as well. Take in account that the memory usage profiling
#   consumes its own minimal resources so it is suggested that the better timing profile is reached when the memory
#   profiling methods are not used.
#
#   @section extra_memory_profiler Memory profiler extra packages
#   The profiles packge needs the memory_profiler 0.41 package (documentation is here: https://pypi.python.org/pypi/memory_profiler
#   To run properly the Profiler package you should install memory_profiler with the following command:
#   \code
#   pip install -U memory_profiler
#   \endcode
#   Memory profiler sources are available on GitHub: https://github.com/fabianp/memory_profiler
#
#   To run under the Windows environment, also the psutil module should be installed. Psutil (python system and process
#   utilities) is a cross-platform library for retrieving information on running processes and system utilization
#   (CPU, memory, disks, network) in Python; For more details on how this module works and last sources and documentation
#   the link is here: https://pypi.python.org/pypi/psutil \n
#   To install this package use the following command:
#   \code
#   pip install psutil
#   \endcode
#   Anyway it is strongly suggested to install the psutils package also when working on different platforms.
#
#   \note The memory sampling mechanism can be called once. Multiple calls of the memory sampling api has no effect
#   after the first call. If the mem_used() API is called but the memory sampling has not been initialised the call
#   has no effect and no output is generated.
#
#   @section howto Using the profiler package
#   To use the profiler package APIs the package should be installed and imported in the application. when the instance of
#   the main class is created if it is passed the parameter False then the profiling system APIs are disabled in the
#   program. An example of installation is shown below:
#   \code
#   from profiler import profile
#
#   profiler = profile.Profile(True)
#   class MyClass(self):
#       ...
#       def method_to_profile(self):
#           ...
#           prfoiler.[Profiling API call]
#           ...
#   \endcode
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version. \n
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.\n
#
# You should have received a copy of the GNU LGPL along with this program.
# If not, see <http://www.gnu.org/licenses/ \n
#
# @date March 2016
# @author Enrico Miglino <enrico.miglino@gmail.com>
# @version 0.1.4
# @version documentation version 0.4

##
# Class Profile is the main class managing the profiler framework
#
#   The Profiler class should be instantiated in the pythong sources to be profiled. The profiling features are based
#   on the cProfiler Python native component and can be disabled at a source level. To minimze the impact of the
#   profiler calls when the features are disabled empty functions are called at import level avoiding many conditional
#   selections.
class Profile:

    ##  Profiler class instance, or dummy class depending on the is_enabled flag state
    profiler = None
    ##  Profiler file where data are saved
    profile_file = None

    ##
    # Initialization method. The boolean is_enabled flag determine the kind of imports that should be applied
    # is_enabled: Profiling enable flag, enabled by default
    #
    # @param is_enabled If set to false, the profiling is inactive
    # @param filename The (optional) name of the profiling results, when needed
    def __init__(self, is_enabled = True, filename = 'profile.txt'):

        self.profile_file = filename

        if is_enabled:
            import enabled_profiler
            self.profiler = enabled_profiler.EnabledProfiler()
        else:
            import disabled_profiler
            self.profiler = disabled_profiler.DisabledProfiler()

    ## Start profiling the source
    def enable(self):
        self.profiler.enable()

    ##
    # Start sampling memory usage. Sampling frequency is fixed every 1 second
    def sample_memory(self, comment = ''):
        self.profiler.memory(1, comment)

    ## Stop profiling the source
    def disable(self):
        self.profiler.disable()

    ## Create statistic object internally to the profiled blocks
    def create_stats(self):
        self.profiler.create_stats()

    ## Show the used memory in the requested block
    def memory_usage(self):
        self.profiler.mem_used()

    ## Print the statistics to the stdout
    def print_stats(self):
        self.profiler.print_stats()

    ##
    # Dump the statistics to the file fname
    #
    # @todo ISSUE: The generated statistic file is not text readable.
    def dump_stats(self):
        self.profiler.dump_stats(self.profile_file)

    ## Profile the command parameter
    def run(self, command):
        self.profiler.run(command)

    ## Profile the command via exec() specifying the global and local environmnet
    def run(self, command, globals, locals):
        self.profiler.run(command, globals, locals)

    ## Profile the specified function with arguments
    def runcall(self, func, args, kwargs):
        self.profiler.runcall(func, args, kwargs)

    ## Generates a report with the profiled statistics
    # (Shows the global collected statistics)
    def stats(self):
        self.profiler.statistics()

    ##
    # Generates a report with the profiled statistics for the specific module
    def profile_module(self, module = None, comment = None):
        self.profiler.module_stats(module, comment)

    ##
    # Generates a report with the profiled statistics based on callers and callees
    def profile_module_calls(self, module = None, comment = None):
        self.profiler.module_stats_calls(module, comment)
