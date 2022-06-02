FROM python:3
WORKDIR /usr/app/
COPY . .
#########
#########
RUN apt-get clean
##########
RUN apt-get update -y
RUN pip install RPi.GPIO
RUN pip install pika
#RUN pip3 install --upgrade setuptools
RUN python3 -m pip install --upgrade pip setuptools wheel                                                                                                                                                                                                
RUN pip3 install adafruit-circuitpython-dht
RUN pip3 install https://github.com/vshymanskyy/blynk-library-python/archive/master.tar.gz
#RUN python3 -m pip install Adafruit_DHT
#RUN pip install python3-dev
#RUN pip3 install adafruit-dht
#RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git && \
#	cd Adafruit_Python_DHT && \
#	python setup.py install
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y python3-pip libpq-dev python-dev
RUN python -m pip install --upgrade pip setuptools wheel
RUN apt-get update -qy && apt-get install -qy \
git \
python3 \
python3-rpi.gpio
#RUN pip3 install pandas
COPY . .
#CMD ["sensorbooth.py"]
#CMD ["sensorbth.py"]
#CMD ["onec.py"]
#CMD ["msg.py"]
CMD ["p.py"]
ENTRYPOINT ["python3"]




########
#######






# RUN python3 -m pip install pika --upgrade
## RUN apt-get clean
RUN apt-get update -y
# RUN apt-get -oDebug::pkgAcquire::Worker=1 update
# RUN python3 -m pip install --upgrade pip setuptools wheel                                                                                                                                                                                                
# RUN apt-get update --allow-unauthenticated -y
## CMD ["p.py"]
## ENTRYPOINT ["python3"]
