# init.py

import json
import _thread,time
config = json.loads(open("config.json").read())

park_slot = [False,False,False,False,False,False,False]

def monitor_thr():
  while (True):
    time.sleep(2)
    print("Monitoring...")
  
_thread.start_new_thread(monitor_thr,())

