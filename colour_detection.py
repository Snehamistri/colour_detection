#!/usr/bin/env python
# coding: utf-8

# ## The Sparks Foundation
# ## Domain : IOT & Computer Vision
# ## Name : Sneha Mistri
# 
# ## Task 01 : Colour Detecting In An Image Using Opencv and Python 
#  

# In[ ]:





# In[ ]:


import cv2 ## importing required libraries
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


path=(r'C:\Users\Amar\Downloads\colours.jpg')##defining path for image
img = cv2.imread(path) 


# In[ ]:


plt.figure(figsize=(20,8))  ##output will be in GBR FORM
plt.imshow(img)


# In[ ]:


grid_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) ##coverting BGR TO RGB


# In[ ]:


plt.figure(figsize=(20,8))
plt.imshow(grid_rgb)


# In[ ]:


grid_hsv=cv2.cvtColor(grid_rgb,cv2.COLOR_RGB2HSV)


# In[ ]:


lower = np.array((45,150,50))## fetching the exact colour
upper = np.array((65,255,255))


# In[ ]:


mask = cv2.inRange(grid_hsv,lower,upper)


# In[ ]:


plt.figure(figsize=(20,8))
plt.imshow(mask)


# In[ ]:


res = cv2.bitwise_and(grid_rgb,grid_rgb,mask=mask)


# In[ ]:


plt.figure(figsize=(20,8))
plt.imshow(res)

