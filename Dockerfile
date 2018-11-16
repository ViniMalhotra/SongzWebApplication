From ubuntu:16.04

MAINTAINER Vini Malhotra "malhotvi@mail.uc.edu"

RUN apt-get update && apt-get -y install python python-pip python3 python3-pip nano

RUN pip2 install --upgrade pip
RUN pip2 install --upgrade setuptools

RUN pip3 install --upgrade pip

RUN mkdir -p /opt/music_app/music/ /code /opt/music_app/logs/supervisor/ /opt/music_app/run

ADD requirements.txt /opt/music_app
RUN pip2 install supervisor

RUN pip3 install -r /opt/music_app/requirements.txt

RUN django-admin startproject music /opt/music_app/music/ 

ADD music/media/ /code/media/
ADD music/song/ /code/song/
ADD music/music/settings.py music/music/urls.py /code/music/
ADD docker-essentials/supervisor/supervisord.conf /etc/supervisor/
ADD docker-essentials/bin/start docker-essentials/bin/copy_files.py /opt/music_app/bin/

WORKDIR /opt/music_app/

CMD python3 /opt/music_app/bin/copy_files.py
