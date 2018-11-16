#!/usr/bin/env python3
import os
from distutils.dir_util import copy_tree
import subprocess

BASE_DIR = os.path.join('/', 'opt', 'music_app', 'music')
MUSIC_DIR = os.path.join('/', 'code', 'music')
MEDIA_DIR = os.path.join('/', 'code', 'media')
SONG_DIR = os.path.join('/', 'code', 'song')

cmd1 = ['python3 /opt/music_app/music/manage.py makemigrations song']
cmd2 = ['python3 /opt/music_app/music/manage.py migrate']
cmd3 = ['python3 /opt/music_app/music/manage.py runserver 0.0.0.0:8000']

copy_tree(MUSIC_DIR, os.path.join(BASE_DIR, 'music'))
copy_tree(MEDIA_DIR, os.path.join(BASE_DIR, 'media'))
copy_tree(SONG_DIR, os.path.join(BASE_DIR, 'song'))

p1 = subprocess.Popen(cmd1, shell=True)
p2 = subprocess.Popen(cmd2,shell=True)
p3 = subprocess.Popen(cmd3,shell=True)

while True:
    pass
