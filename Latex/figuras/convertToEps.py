#!/usr/bin/env python
from os import walk
import os

mypath = '/media/andre/01D0C0D790865A10/Dropbox/unb/TCC/Latex/figuras'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
for i in f:
	print i