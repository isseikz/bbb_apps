#Beagle Bone Black用 電圧測定プログラム dev1
-*- coding: utf-8 -*-
import time
import Adafruit_BBIO.ADC as ADC
f = open("data.dat","w")
f.write("電圧測定プログラム")
ADC.setup()
start = time.time()
while true:
  try:
    voltage = ADC.read("P9_39")
    elapsed_time = time.time() - start
    f.write(elapsed_time,voltage)
    print voltage
  except KeyboardInterrupt:
    break
f.close()
