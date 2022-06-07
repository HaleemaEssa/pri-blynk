#!/bin/bash -e

CONTAINER_NAME=$(ctx node properties container_ID)
IMAGE_NAME=$(ctx node properties image_name)
#**** from dr.rawaa github***
ctx logger info "Download ${IMAGE_NAME}"
sudo docker pull ${IMAGE_NAME}
ctx logger info "Creating Container ${CONTAINER_NAME}"

#sudo docker run --name ${CONTAINER_NAME} -it -d ${IMAGE_NAME} bin/bash
#sudo docker run -v "${PWD}:/data" --name ${CONTAINER_NAME} -it -d ${IMAGE_NAME} bin/bash
##***###sudo docker run -v "${PWD}:/data" --name container1 -it -d python3 bin/bash
sudo docker run -P --name ${CONTAINER_NAME} -v "${PWD}:/data" -it -d ${IMAGE_NAME} bin/bash
