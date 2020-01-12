#!/usr/bin/env python
# coding: utf-8

# In[166]:


import cv2
import numpy as np

# Let's load a simple image with 3 black squares 
image = cv2.imread('6.png') 
cv2.waitKey(0) 
  
# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  
# Find Canny edges 
#edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0) 


# In[164]:


image = cv2.resize(im_bw, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
image = cv2.medianBlur(image, 3)
image = cv2.GaussianBlur(image,(5,5),0)
#image = cv2.addWeighted(image,1.5,image,-0.5,0)
#image[image >= 80] = 255
#cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imwrite("new6.jpg",image)


# In[89]:


contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# In[90]:


print("Number of Contours found = " + str(len(contours)))


# In[91]:


cv2.drawContours(image, contours, -1, (255, 255, 255), thickness=cv2.FILLED) 


# In[92]:


#image = cv2.GaussianBlur(image,(5,5),0.7)
#image = cv2.addWeighted(image,1.5,image,-0.5,0)
#image[image != 255] = 0 #
cv2.imwrite("new6.jpg",image)


# In[165]:


import pytesseract
from PIL import Image
img = Image.open("new6.jpg") 
pytesseract.image_to_string(img, lang= 'tur')


# In[21]:





# In[ ]:




