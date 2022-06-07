#! /bin/bash
CONTAINER_NAME=$(ctx node properties container_ID)
#CONTAINER_ID=$1
#IMAGE_NAME=$(ctx node properties image_name)
LIBRARY_NAME=$(ctx node properties lib_name)
sudo docker exec -it CONTAINER_NAME apt-get update -y install ${LIBRARY_NAME} #pip install pika

