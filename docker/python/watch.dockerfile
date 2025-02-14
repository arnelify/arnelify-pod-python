FROM gcc:14.2.0

WORKDIR /var/www/python

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install sudo tzdata nano wget gnupg curl zip unzip -y
RUN apt-get install libjsoncpp-dev inotify-tools -y

RUN apt-get install python3.11-venv -y
RUN sudo ln -sf $(which python3) /usr/bin/python

COPY ./.env ./.env
COPY ./.gitignore ./.gitignore
COPY ./LICENSE ./LICENSE
COPY ./Makefile ./Makefile
COPY ./README.md ./README.md
COPY ./requirements.txt ./requirements.txt

RUN python -m venv venv && venv/bin/pip install -r requirements.txt

EXPOSE 3001