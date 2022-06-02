# print('Hello, world!')
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import pika
import random
import os
####Hum & Temp ###
import adafruit_dht
from board import *

# GPIO17

SENSOR_PIN = D5
#def callback4():

 #   dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)

  #  temperature = dht11.temperature
   # humidity = dht11.humidity
   # return(humidity,temperature)
   # print(f"Humidity= {humidity:.2f}")
   # print(f"Temperature= {temperature:.2f}°C")

#GPIO SETUP
channel1 = 27 #for sound
channel12 = 22 #for flame
#channel14=4
GPIO.setmode(GPIO.BCM)  
GPIO.setup(channel1, GPIO.IN)
GPIO.setup(channel12, GPIO.IN)
#GPIO.setup(channel14, GPIO.IN)
GPIO.setup(channel25, GPIO.OUT)
channel25 =25 #for relay
credentials = pika.PlainCredentials('haleema', '4chyst')
parameters = pika.ConnectionParameters('192.168.0.126',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

#channel.queue_declare(queue='task_queue', durable=True)
channel.exchange_declare(exchange='logs', exchange_type='fanout')

def callback1(channel1):
    if GPIO.input(channel1):
        return('0')
    else:
        return('1')
    return sound    #
    sound=0
GPIO.add_event_detect(channel1, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel1, callback1)  # assign function to GPIO PIN, Run function on change

def callback2(channel12):
    if GPIO.input(channel12):
        GPIO.output(25,GPIO.LOW)
        time.sleep(2)    
        return('0')
        
    else:
        print("led on")
        GPIO.output(25,GPIO.HIGH)
        time.sleep(2)
        return('1')
    return flame    #
    flame=0
GPIO.add_event_detect(channel12, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel12, callback2)  # assign function to GPIO PIN, Run function on change


def callback4():

    dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)
   # dht11 = adafruit_dht.DHT11(channel14, use_pulseio=False)

    temperature = dht11.temperature
    humidity = dht11.humidity
    return(humidity,temperature)
    print(f"Humidity= {humidity:.2f}")
    print(f"Temperature= {temperature:.2f}°C")

#GPIO.add_event_detect(channel14, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(channel14, callback4)  # assign function to GPIO PIN, Run function on change



#def callback4():
 #   h = random.randint(0,100)
  #  t = random.randint(-40,80)
   # return(h,t)
#while True:
###for x in range (10):
#   try:
   ###     h, t =callback4()
   ###     sound=callback1(channel1)
   ###     flame=callback2(channel12)
   ###     message=str(sound)+":"+str(flame)+":"+str(h)+":"+str(t)
   ###     channel.basic_publish(exchange='logs', routing_key='', body= message)
   ###     print ("sent %r" %message) 
#print(" [x] Sent 'Hello World!'")
#        time.sleep(0.5)
 #       print('Interrupted')
#        sys.exit(0)
 #  except SystemExit:
#        connection.close()
  #      os._exit(0)
###connection.close()

###@# infinite loop
#while True:
 #       time.sleep(3)

def checkdht():
    for i in range(10):
        try:
            h, t =callback4()
            sound=callback1(channel1)
            flame=callback2(channel12)
            message=str(sound)+":"+str(flame)+":"+str(h)+":"+str(t)
            channel.basic_publish(exchange='logs', routing_key='', body= message)
            print ("sent %r" %message) 

        except RuntimeError:
            pass
        time.sleep(5)

while True:
    checkdht()

connection.close()
