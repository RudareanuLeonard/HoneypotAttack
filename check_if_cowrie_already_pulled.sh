#!/bin/bash

IMAGE_NAME="cowrie/cowrie"
IMAGE_TAG="latest"

if sudo docker image inspect "$IMAGE_NAME:$IMAGE_TAG" &> /dev/null; then
    echo "Cowrie honeypot image $IMAGE_NAME:$IMAGE_TAG is already pulled."
else
    echo "Cowrie honeypot image $IMAGE_NAME:$IMAGE_TAG is not pulled yet. We will pull it now."
    sudo docker pull "$IMAGE_NAME:$IMAGE_TAG"
    echo "Image pulled"
fi
