#!/usr/bin/env python
# coding: utf-8

# In[13]:


abc=open("letsupgrade.txt",'w')
abc.write("I LOVE LETSUPGRADE")
abc.close()


# In[14]:


abc=open("letsupgrade.txt",'r')
content=abc.read()
abc.close()


# In[15]:


content


# In[16]:


abc=open("letsupgrade.txt",'a')
abc.write("very much")
abc.close()


# In[17]:


abc=open("letsupgrade.txt",'r')
content=abc.read()
abc.close()


# In[18]:


content


# In[19]:


#assigment 2


# In[36]:


num = int(input("Enter a Number: "))
import math
def factorial(num):
    fac= math.factorial(num)
    print(fac)
    return fac

print("Factorial of number", factorial(num))
    


# In[ ]:





# In[ ]:





# In[ ]:



    


# In[ ]:




