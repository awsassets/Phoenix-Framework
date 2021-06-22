#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import sys
import pyfiglet
import time
from time import sleep
from pyfiglet import Figlet


f = Figlet(font='digital')
print(f.renderText('Phoenix Framework'), end = '')

#Path
path = os.getcwd()
core = (path+'/core')


#check version
with open(core + "/VERSION", 'r') as f:
    version = f.read()
    print("\033[32m[VERSION]\033[0m",version, end = '')

from core import pefcore
