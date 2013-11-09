import time

def launch(N,lc):
   i = N
   while i > 0:
      time.sleep(1)
      print str(i) + '...'
      i = i - 1
        
launch(10)
