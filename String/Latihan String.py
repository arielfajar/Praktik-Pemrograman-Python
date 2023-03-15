#!/usr/bin/env python
# coding: utf-8

# In[2]:


nama = "Ariel Fajar Herdanto"

#Menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama.replace(" ",""))
print("Jumlah huruf dari nama (Ariel Fajar Herdanto) adalah : ", jumlah_huruf)

# Menghitung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len([char for char in nama if char in huruf_vokal])
print("Jumlah huruf vokal dari nama (Ariel Fajar Herdanto) adalah : ", jumlah_vokal)

# Menghitung jumlah huruf konsonan dari nama lengkap
huruf_konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
jumlah_konsonan = len([huruf for huruf in nama if huruf in huruf_konsonan])

#pakai (jumlah_konsonan = jumlah_huruf - jumlah vokal) juga bisa

print("Jumlah huruf konsonan dari nama (Ariel Fajar Herdanto) adalah : ", jumlah_konsonan)


# In[ ]:




