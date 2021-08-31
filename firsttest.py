# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:58:15 2021

@author: chong
"""

from PIL import Image
from PIL.ExifTags import TAGS
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from useful_functions import *

# def display_pic_metadata(imagename):
#     image = Image.open(imagename)
#     exifdata = image.getexif()
#     print("hello")
#     print(exifdata,"hello")
#     exifdic = {}
    
#     for tag_id in exifdata:
#         tag = TAGS.get(tag_id,tag_id)
#         data= exifdata.get(tag_id)
#         if isinstance(data,bytes):
#             data = data.decode()
#         # print(f"{tag:25}:{data}")
#         exifdic[tag]=data
#     return exifdic
        
# name = 'IMG_5476.jpg'

# imagename = picpath + '/' + name
# display_pic_metadata(imagename)


def delete_duplicate(picpath):
    (subdir,files) = listdir(picpath)
    print(subdir)
    print(files)
    
    dic = {}
    
    # def getdic
    
    for (i,filename) in enumerate(files):
        # print("===================  ",i,"  ===============")
    
        path  = os.path.join(picpath,filename)
        dm = display_pic_metadata(path)
    
        img = mpimg.imread(path)
        identifier = tuple(img[1:4,0,0])
        if dic.get(identifier,0)!=0:
            dic[identifier] = dic[identifier] + ';' + filename
            # print('repeat\n')
        else:
            dic[identifier] = filename
        
    
    for k,v in dic.items():
        arr = v.split(';')
        if len(arr)>1:
            print(arr)
            for i in range(1,len(arr)):
                p = os.path.join(picpath,arr[i])
                print("removing ",p)
                os.remove(p)
picpath = 'C:/Users/chong/Desktop/duppics/unknown_date'
    
delete_duplicate(picpath)
# plt.imshow(img[:,:,1])
















