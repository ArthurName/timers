"""Decorators to measure execution time of methods.

Probably you'd want to put a copy of this file in your personal user site
directory (you can get the directory by running 'python -m site --user-site').
That way you can always import it without messing with sys.path.

Usage:

    @timer
    def method_x(...)
        ...

    @clocker
    def method_y(...)
        ...
"""

import time
from functools import wraps


def timer(method):
    """Decorator to measure execution (wall-clock) time of a method."""
    @wraps(method)
    def time_it(*args, **kwargs):
        """Measure execution time and report."""
        start_time = time.time()
        method_result = method(*args, **kwargs)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print 'Wall-clock time for %s(): %2.2f ms' % (method.__name__,
                                                      duration)
        return method_result
    return time_it


def clocker(method):
    """Decorator to measure execution time (CPU time) of a method."""
    @wraps(method)
    def time_it(*args, **kwargs):
        """Measure execution time and report."""
        start_time = time.clock()
        method_result = method(*args, **kwargs)
        end_time = time.clock()
        duration = end_time - start_time
        print 'CPU time for %s(): %2.2f s' % (method.__name__, duration)
        return method_result
    return time_it
