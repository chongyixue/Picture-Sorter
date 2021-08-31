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
from useful_functions import *



Tk().withdraw()

directory = askdirectory()

# monthlist = ['january','feb','march','april']

# for month in monthlist:
#     add_direc(directory,month)

# subdir,files = listdir(directory)

# print(subdir)
# print(files)



unpack_deduplicate(directory)
        
# unpack_subdirectories(directory)
        




# subdir,files = listdir(directory)

# for fn in files:    
#     pic_to_month(directory,fn)

# subdir,_ = listdir(directory)
# for direc in subdir:
#     delete_duplicate(os.path.join(directory,direc))












