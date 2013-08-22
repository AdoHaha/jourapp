from threading import Timer

import time 
    
      
def throttle(mindelta):
    def decorator(fn):
        def throttled(*args,**kwargs):
            def call_it():
                        throttled.lastTimeExecuted=time.time()
                   
                        fn(*args, **kwargs)
                        
                        
            if hasattr(throttled,"lastTimeExecuted"):
               
                lasttime=throttled.lastTimeExecuted
               
            else: #just execute fction
                
                try:
                        throttled.t.cancel()
                except(AttributeError):
                        pass
                call_it()
                return throttled
                    
            delta=time.time()-throttled.lastTimeExecuted
            try:
                        throttled.t.cancel()
            except(AttributeError):
                        
                        pass
            if delta>mindelta:
                
                call_it()
            else:
                timespot=mindelta-delta
                timespot=timespot
                throttled.t=Timer(timespot,call_it)
                throttled.t.start()
        return throttled
    return decorator           

               
            
                        
