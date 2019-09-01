import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=17
 
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
temperature = temperature * 9/5.0 + 32

while True:
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again! Dont give up!')
        GPIO.output(21,GPIO.LOW)
    
    if temperature > 75:
        print ("Too hot!")
        GPIO.output(21,GPIO.HIGH)
    else:
        print ("Tempurature Normal")
        GPIO.output(21,GPIO.LOW)
    
    if humidity is None and temperature is None:
        GPIO.output(21,GPIO.LOW)
        print ("No Data")
    time.sleep(30)    