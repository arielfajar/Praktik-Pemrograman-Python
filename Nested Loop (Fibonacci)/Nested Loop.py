#!/usr/bin/env python
# coding: utf-8

# In[11]:


fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

for i in range(len(fibonacci_numbers)):
    print(*fibonacci_numbers[:i+1])

