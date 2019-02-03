# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:58:35 2019

@author: Raghav
"""
from PIL import Image
def merge (imagePath1,imagePath2):
    
    #Open Images, dont load yet
    img1 = Image.open(imagePath1)
    img2 = Image.open(imagePath2)
        
    #To ensure main image is bigger than the one being merged
    if img2.size > img1.size:
        raise Exception('Size of 1st/Main Image is smaller then 2nd')
        
    #Get the pixel map of the two images 
    #Load returns a pixel access object that can be used to read and modify pixels.
    #The access object behaves like a 2-dimensional array
    pixel_map1 = img1.load()
    pixel_map2 = img2.load()
    
    #path name for testing
    path1='C:/Users/Raghav/Desktop/steganography-master/images/enigma.jpg'
    path2='C:/Users/Raghav/Desktop/steganography-master/images/forest_hidden.png'

    #Lets try to create a new image
    newImage = Image.new('RGB',img1.size)
    pixelNew = newImage.load()
    
    #trying to convert int to binary for R G B...but how?

    
    
    
    
    
    
    
    
    
    
merge(path1,path2)