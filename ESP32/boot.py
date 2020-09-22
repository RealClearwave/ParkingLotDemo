# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import gc
import os
#import webrepl
#webrepl.start()
gc.collect()


Wifi_SSID = "Hiwifi_218EB2"
Wifi_PSWD = "1977103027"



html404= """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>404 - Not Found</title>
    </head>
    <body> 
            <h1>404 Not Found</h1>
            <p>MicroPy Esp8266 Server</p>
    </body>
</html>
"""



def __fileExist(path):
    try:
        stat = os.stat(path)
        # stat[0] bit 15 / 14 -> file/dir
        if stat[0] & 0x8000 == 0x8000: # file
            return True
        else:  # Dir
            return False
    except:
        return False
       
       
  
  
#----------------------------------------main-----------------------------------------------
#post check
import micropython
print ("****************************************")
print ("*------------EspWebSrv-----------------*")
print ("****************************************")
print ("FreeMem:%d" % gc.mem_free())

print(os.listdir())
exec(open("init.py").read(),globals())

#init Wifi
import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect(Wifi_SSID, Wifi_PSWD) # Connect to an AP
while not sta_if.isconnected():                      # Check for successful connection
  pass

print ("Wifi Connected,IP:")
print (sta_if.ifconfig()[0])
gc.collect()

import socket
addr = socket.getaddrinfo(sta_if.ifconfig()[0], 80)[0][-1]  

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Server Running On', addr)

while True:
    cl, addr = s.accept()
    request = cl.recv(1024)
    try:
      Args = request.decode().split()[1].split(":")
    except:
      continue
    print (Args)
    Fpth = Args[0]
    
    cl.send("HTTP/1.1 200 OK\r\n")
    cl.send("Content-Type: text/html\r\n\r\n")
    
    if not __fileExist(Fpth):
      if __fileExist(Fpth + "index.html"):
        Fpth = Fpth + "index.html"
      else:
        cl.send(html404)
        continue
        
    if 'py' in Fpth:
      try:
        exec(open(Fpth).read(),globals())
      except:
        pass
    else:
      try:
        f = open(Fpth,'rb')
        for i in f:
          cl.send(i)
        f.close()
      except:
        pass
   
    cl.close() 
    gc.collect()

