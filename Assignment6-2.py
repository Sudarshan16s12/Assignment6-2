#!/usr/bin/env python
# coding: utf-8

# In[20]:


class dog:
    def __init__(self,name,age,coat_colour):
        self.name=name
        self.age=age
        self.coat_colour=coat_colour
    def description(self):
        print("Name of dog is: ",self.name)
        print("Age of dog is: ",self.age)
    
    def get_info(self):
        print("Coat_colour of dog is: ",self.coat_colour)

class JackRussellTerrier(dog):
    def description(self):
        print("Dog is JackRusselTerrier")

class Bulldog(dog):
    def description(self):
        print("Dog is Bulldog")
       
    
my_dog=dog(" Julie ", 8 ," Red ")
my_dog.description( )
my_dog.get_info( )
       


# In[ ]:




