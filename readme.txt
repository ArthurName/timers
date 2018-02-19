Timers
------

Purpose: To measure execution time for any method.

Implementation: By using a decorator you don't need to add code to the
methods themselves. Both time.time() (@timer) and time.clock() (@clocker) are
supported.

Usage (as example.py):

    from timers import timer

    @timer
    def example():
        print "Hello world!"

> python example.py
Hello world!
Wall-clock time for example(): 0.30 ms
