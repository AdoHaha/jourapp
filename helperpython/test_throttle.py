#!/usr/bin/python
import unittest
import time
from throttle import throttle
 
 
class TestThrottle(unittest.TestCase):
 
    @throttle(1)
    def increment(self):
        """ Simple function that
            increments a counter when
            called, used to test the
            debounce function decorator """
        self.count += 1
 
    def setUp(self):
        self.count = 0
 
    def test_throttle(self):
        """ Test that the increment
            function is being debounced.
            Function should be used only once a second (and used at start)"""
        self.assertTrue(self.count == 0)
        self.increment()
        self.assertTrue(self.count == 1)
        self.increment()
        self.increment()
        self.increment()
        self.increment()
        self.increment()
        time.sleep(0.25)
        self.increment()
        self.increment()
        self.increment()
        self.increment()
        self.increment()
        self.increment()
        
        self.assertTrue(self.count == 1)
        
        self.increment()
        self.increment()
        self.increment()
        self.increment()
        self.assertTrue(self.count == 1)
        time.sleep(1)
        self.assertTrue(self.count == 2)
        time.sleep(10)
        self.assertTrue(self.count == 2)
 
if __name__ == '__main__':
    unittest.main()
