# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:51:19 2021

@author: chong
"""



from PIL import Image
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
# import pyheif 

import os, shutil

def guess_heic_date(filename):
    with open(filename,mode='rb') as file:
        f1 = file.read()
        f2 = f1.decode(encoding='UTF-8',errors='replace')
    for i,l in enumerate(f2):
        if l == ':' and f2[i+3] == ':' and f2[i+9]==':' and f2[i+12] == ':':
            return f2[i-4:i+15]
    return

def display_pic_metadata(imagename):
    try:
        if imagename.split('.')[-1] == 'heic':
            exifdic = {}
            exifdic['DateTime'] = guess_heic_date(imagename)
            return exifdic
        else:
            image = Image.open(imagename)
    except:
        print("Cannot read ",imagename)
        return {}
    exifdata = image.getexif()
    exifdic = {}
    
    for tag_id in exifdata:
        tag = TAGS.get(tag_id,tag_id)
        data= exifdata.get(tag_id)
        if isinstance(data,bytes):
            try:
                data = data.decode('UTF8','replace')
            except Exception as e: print(e)

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
        try:
            img = mpimg.imread(path)
            identifier = tuple(img[1:4,0,0])
            if dic.get(identifier,0)!=0:
                dic[identifier] = dic[identifier] + ';' + filename
                # print('repeat\n')
            else:
                dic[identifier] = filename
        except:
            print("cannot read ",path)
            
        
    
    for k,v in dic.items():
        arr = v.split(';')
        if len(arr)>1:
            print(arr)
            for i in range(1,len(arr)):
                p = os.path.join(picpath,arr[i])
                print("removing ",p)
                os.remove(p)
    
def makefullpath(subdirlist,directory):
    subdirlistnew = []
    for (i,s) in enumerate(subdirlist):
        subdirlistnew.append(os.path.join(directory,s))    
    return subdirlistnew

def unpack_subdirectories(directory):
    subdir,_ = listdir(directory)    
    subdir = makefullpath(subdir,directory)
    subdiroriginal = subdir[:]
    counter =  0
    while len(subdir) > 0:
        counter += 1
        sd = subdir.pop()
        subsub,files = listdir(sd)
        for file in files:
            fullfilepath = os.path.join(sd,file)
            print("moving ",fullfilepath," to ",directory)
            try:
                shutil.move(fullfilepath,directory)
            except:
                pass
        subsub = makefullpath(subsub,sd)
        subdir = subdir + subsub
    
    for s in subdiroriginal:
        try:
            os.remove(s)
        except PermissionError:
            print('Cannot delete ',s,' Please do so manually')
            


def unpack_subdirectories_old(directory):
    subdir,files = listdir(directory)
    count = 0
    while len(subdir)>0:
        sd = subdir.pop()
        sd2,f2 = listdir(os.path.join(directory,sd))
        sf = sd2 + f2
        for s in sf:        
            oldname = os.path.join(directory,sd,s)
            newname = os.path.join(directory,s)
            os.rename(oldname,newname)
        try:
            os.remove(os.path.join(directory,sd))
        except OSError:
            count += 1
            print('Cannot delete ',os.path.join(directory,sd),'Please do so manually')
    
    subdir,_= listdir(directory)
    if len(subdir) > count:
        unpack_subdirectories(directory)

def unpack_deduplicate(directory):
    unpack_subdirectories(directory)
    subdir,files = listdir(directory)
    for fn in files:    
        pic_to_month(directory,fn)
    
    subdir,_ = listdir(directory)
    for direc in subdir:
        delete_duplicate(os.path.join(directory,direc))


