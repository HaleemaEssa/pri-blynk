# print('Hello, world!')
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import pika
import random
import os
import BlynkLib
####Hum & Temp ###
import adafruit_dht
from board import *
BLYNK_TEMPLATE_ID = "TMPLwRnu6EOo"
BLYNK_DEVICE_NAME = "MonitorControl"
BLYNK_AUTH_TOKEN = "Nhqs6DflGfI3w7opYwAvaTjVjfDh3MbH"
BLYNK_FIRMWARE_VERSION = "0.1.0"
T_PIN = 0
H_PIN = 1

F_PIN = 2
S_PIN = 3
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)
MSG_NOTIFY = 14
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
channel25 =25
GPIO.setup(channel25, GPIO.OUT)
#channel25 =25 #for relay
credentials = pika.PlainCredentials('haleema', '4chyst')
parameters = pika.ConnectionParameters('192.168.0.191',
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
        blynk.log_event('sound_event', 'Sound Detected')
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
        #blynk.log_event('flame_event', 'Hello') #flame_event
        GPIO.output(25,GPIO.HIGH)
        blynk.log_event('flame_event', 'Flame Detected') #flame_event
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
    for i in range(20):
        try:
            h, t =callback4()
            sound=callback1(channel1)
            flame=callback2(channel12)
######
            blynk.run()
            blynk.virtual_write(T_PIN, t)
            blynk.virtual_write(H_PIN, h)
            blynk.virtual_write(F_PIN, flame*255)
            blynk.virtual_write(S_PIN, sound*100)
            if t > 28:
                blynk.log_event('temp_event', 'Humidity is High')
            if h > 50:
                blynk.log_event('humidity_event', 'Temperature is High')
        #    if flame == 1:
         #       blynk.log_event('flame_event', 'Flame Notification')
          #  if sound == 1:
           #     blynk.log_event('sound_event', 'Sound Notification')  

            message=str(sound)+":"+str(flame)+":"+str(h)+":"+str(t)
            channel.basic_publish(exchange='logs', routing_key='', body= message)
            print ("sent %r" %message) 
########
            #blynk.run()
            #blynk.virtual_write(T_PIN, t)
            #blynk.virtual_write(H_PIN, h)
            #blynk.virtual_write(F_PIN, flame*255)
            #blynk.virtual_write(S_PIN, sound*100)
            #if t > 20:
            #    blynk.log_event('temp_event', 'Hello')
            #if h > 27:
            #    blynk.log_event('humidity_event', 'Hello')  
            #print('Temperature: ',t,'\tHumidity: ',h,'\t\tFlame: ',flame,'\tSound: ',sound)

        except RuntimeError:
            pass
        time.sleep(5)

while True:
    checkdht()

connection.close()

