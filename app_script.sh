#! /bin/bash
CONTAINER_NAME=$(ctx node properties container_ID)
#CONTAINER_ID=$1
#IMAGE_NAME=$(ctx node properties image_name)
APP_NAME=$(ctx node properties app_name)
sudo docker exec -it CONTAINER_NAME CMD ["APP_NAME"]

