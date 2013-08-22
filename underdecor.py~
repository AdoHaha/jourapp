from threading import Timer

import time 
 
def debounce(wait):
    """ Decorator that will postpone a functions
        execution until after wait seconds
        have elapsed since the last time it was invoked. """
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = Timer(wait, call_it)
            debounced.t.start()
        return debounced
    return decorator
    
    
    
      
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

               
            
                        
