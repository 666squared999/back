FROM ubuntu

RUN mkdir ./app

# copy only static data needed to build
COPY ./requirements.txt ./app/requirements.txt
COPY ./scripts/docker_entry.sh ./app/entry.sh
COPY ./.env ./app/.env

RUN apt update; yes Yes | apt install python3-pip;

WORKDIR /app

RUN /bin/bash -c "pip3 install -r requirements.txt;"

RUN apt-get install build-essential -y \
    && apt-get clean

RUN ["chmod", "+x", "./entry.sh"]
ENTRYPOINT ["./entry.sh"]
