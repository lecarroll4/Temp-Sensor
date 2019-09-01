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


while humidity is not None and temperature is not None:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    temperature = temperature * 9/5.0 + 32

    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

    if temperature > 50:
        print ("Too hot!")
        GPIO.output(21,GPIO.HIGH)
    else:
        print ("Tempurature Normal")
        GPIO.output(21,GPIO.LOW)
    time.sleep(30)   

print('Failed to get reading. Try again! Dont give up!')
GPIO.output(21,GPIO.LOW)