# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 09:07:31 2023

@author: chong
"""

from PIL import Image
from PIL.ExifTags import TAGS
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from useful_functions import *
import time, datetime
import shutil

d = {} # '2022-01': [time,filename,dattimestring]
# picpath = 'C:/Users/chong/Desktop/duppics'
# (subdir,files) = listdir(picpath)
# print(subdir)
# print(files)

def scan_candidate(filename):
    dm = display_pic_metadata(filename)
    dt = dm.get('DateTime')
    if not dt:
        return
    key = ''.join(dt.split(' ')[0].split(':')[:2])
    date_format = datetime.datetime.strptime(dt, "%Y:%m:%d %H:%M:%S")
    unix_time = datetime.datetime.timestamp(date_format)
    existing = d.get(key)
    valpotential = [unix_time,filename,dt]
    if not existing:
        d[key] = valpotential
    else:
        if unix_time < existing[0]:
            d[key] = valpotential
    return
        
def scan_folder_update_dic(picfolder):
    (subdir,files) = listdir(picfolder)
    for file in files:
        path  = os.path.join(picfolder,file)
        try:
            dm = display_pic_metadata(path)
            # print(dm.get('Model'), dm.get('DateTime'))
            scan_candidate(path)
        except:
            print('SKIP ',path)
    for sd in subdir:
        newpicfolder = os.path.join(picfolder,sd)
        scan_folder_update_dic(newpicfolder)

def copy_files_to(path,foldername):
    folder = os.path.join(path,foldername)
    Q = add_direc(path,foldername)
    for k,v in d.items():
        try:
            fn = v[1]
            oldname = fn.split('\\')[-1]
            shutil.copy(fn,folder)
            tempname = os.path.join(folder,oldname)
            newname = os.path.join(folder,k+'_'+oldname)
            os.rename(tempname,newname)
        except:
            print(oldname, ' previously copied')
            
            
picpath = "D:/Photos"
montlypath = 'C:/Users/chong/Desktop'
scan_folder_update_dic(picpath)
# print(d)
copy_files_to(montlypath,'first_pic_month2')
    


# Cannot read  D:/Photos\California 2022\IMG_7821.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7821.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7823.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7823.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7824.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7824.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7825.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7825.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7826.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7826.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7830.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7830.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7831.HEIC
# Cannot read  D:/Photos\California 2022\IMG_7831.HEIC

# # # path  = os.path.join(picfolder,file)
# # path = "D:/Photos\winter hols 2010\solar eclipse\solar eclipse-66 chosen\IMG_1838.JPG"
# path = "D:/Photos\California 2022\IMG_7831.HEIC"
# # # path = "C:/Users\chong\Desktop\\first_pic_month\\202205_IMG_8316.JPG"
# dm = display_pic_metadata(path)
# print(dm)
