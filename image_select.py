# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:58:51 2021

@author: chong
"""

from PIL import Image
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

import os


def display_pic_metadata(imagename):
    image = Image.open(imagename)
    exifdata = image.getexif()
    exifdic = {}
    
    for tag_id in exifdata:
        tag = TAGS.get(tag_id,tag_id)
        data= exifdata.get(tag_id)
        if isinstance(data,bytes):
            data = data.decode()
        # print(f"{tag:25}:{data}")
        exifdic[tag]=data
    return exifdic


def listdir(directory):
    allsub = os.listdir(directory)
    subdir = []
    files = []    
    for s in allsub:
        if os.path.isdir(os.path.join(directory,s)):
            subdir.append(s)
        else:
            files.append(s)
    return (subdir,files)


def add_direc(direc,*names):
    for name in names:
        p = os.path.join(direc,name)
        if not os.path.isdir(p):
            os.mkdir(p)
    return p
          
def datetime_to_str(datetime):
    d = datetime.split(':')
    return d[0]+'_'+d[1]

def pic_to_month(directory,fn):
    oldname = os.path.join(directory,fn)
    d = display_pic_metadata(oldname)
    if 'DateTime' in d.keys():
        foldername = datetime_to_str(d['DateTime'])
    else:
        foldername = 'unknown_date'
        print("======= fn =======")
        print(d)
        
        
    folderpath = add_direc(directory,foldername)
    newname = os.path.join(folderpath,fn)
    os.rename(oldname,newname)


Tk().withdraw()

directory = askdirectory()

# monthlist = ['january','feb','march','april']

# for month in monthlist:
#     add_direc(directory,month)

# subdir,files = listdir(directory)

# print(subdir)
# print(files)


subdir,files = listdir(directory)

for fn in files:    
    pic_to_month(directory,fn)













