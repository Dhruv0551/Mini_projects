#!/usr/bin/env python
# coding: utf-8

# In[134]:


from tkinter import *


# Defining The Conversion Function

# In[135]:


def conversion(miles_entry=0):
    try:
        miles = float(miles_entry.get())
        km = round(miles * 1.609344, 2)  # More accurate conversion factor
        return km
    except ValueError:
        return "Invalid input"


# In[136]:


def onConvert():
    result=conversion(miles)
    kms.config(text=result)


# Starting Code

# In[137]:


window = Tk()


# In[138]:


miles = Entry(width=10)
miles.grid(column=1,row=0)


# In[139]:


label = Label(text="Miles")
label.grid(column=2,row=0) 


# Middle Grid

# In[140]:


label2 = Label(text="Is Equal to: ")
label2.grid(column=0,row=1)


# In[141]:


kms = Label(text="0")
kms.grid(column=1,row=1)


# In[142]:


label3 = Label(text="KM")
label3.grid(column=0,row=2)


# Last Row

# In[143]:


calc = Button(text="Calculate",command=onConvert)
calc.grid(column=1,row=2)
window.mainloop()

