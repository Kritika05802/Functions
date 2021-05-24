#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#prints the letters in a string in decreasing order of frequency


# In[4]:


a=input("Please enter a string: ")
def most_frequent(string):
    mydict=dict()
    for key in string:
        if key not in mydict:
            mydict[key]=1
        else:
            mydict[key]+=1
    q=mydict.items()
    n=sorted(q, key=lambda x: x[1], reverse=True)
    return n
print(most_frequent(a))


# In[ ]:




