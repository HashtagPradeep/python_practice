#!/usr/bin/env python
# coding: utf-8

# ---
# ---
# 
# <center><h1>📍 📍 Assignment: Control Flow 📍 📍</h1></center>
# 
# ---
# 
# ***Take 3 inputs from the user***
# 
#  -  **What is your Age?**    (Answer will be an Intger value)
#  -  **Do you eat Pizza?**    (Yes/No)
#  -  **Do you do exercise?**  (Yes/No)
# 
# #### `Write the if else condition for the given flow chart.`
# 
# ![](image/control-flow.png)

# In[17]:


# What is your Age?
Age=int(input('What\'s your age?'))


# In[11]:


# Do you eat Pizza?
pizza=input('Do you eat pizza?')


# In[5]:


# Do you do exercise? 
exercise=input('Do you exercise? ')


# In[18]:


if Age<30:
    if (pizza=='yes'):
        print('1.unfit')
    else: print('1.fit')

else:
    if (exercise=='yes'):
        print('2.fit')
    else: print('2.unfit')
        


# In[ ]:



        


# In[ ]:



    
    
    


# In[ ]:




