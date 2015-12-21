import Adafruit_BBIO.ADC as ADC
import time
ADC.setup()
f = open("test1.dat", "w")
f.write("The Voltage Monitor")
start = time.time()
while True:
  try:
    voltage = ADC.read_raw("P9_40")
    elapsed_time = time.time() - start
    f.write(str(voltage))
    f.write(str(elapsed_time))
    f.write('\n')
    print voltage
  except KeyboardInterrupt:
    f.close()
    break
