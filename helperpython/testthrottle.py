#!/usr/bin/python

import underdecor
import time

@underdecor.throttle(1)
def printprint():
        print time.time()
        

while(True):
        printprint()
        time.sleep(0.01)        
        
        

