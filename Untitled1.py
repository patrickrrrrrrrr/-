#!/usr/bin/env python
# coding: utf-8

# In[2]:


password = "594"
times = 0
while times<= 3:
    answer = input("enter ur password:")
    if answer==password:
        print("entered")
        break
    else:
        times = times + 1
        chance = 3 - times
        print("incorrect!u have",chance,"chances")
        
        


# In[ ]:




