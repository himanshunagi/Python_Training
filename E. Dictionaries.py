#!/usr/bin/env python
# coding: utf-8

# # Dictionaries in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *  Create a Dictionary and perform operations on the Dictionary

# <a id="dic"></a>
# ## Dictionaries

# <a id="content"></a>
# ## What are Dictionaries?

# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.   
# 
# 
# The best example of a dictionary can be accessing person's detais using the **social security number**.   
# Here the social security number which is a unique number will be the **key** and the details of the people will be the **values** associated with it.

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsList.png" width="650">

# ### Create a Dictionary and access the elements

# An example of a Dictionary <code>Dict</code>:
# Here we are creating a dictionary named **Dict** with he following details
# 
# * Keys are **key1, key2, key3, key4, key5**.
# * Values are {1,2,[3,3,3],(4,4,4),5,(0,1):6} corresponding to the keys
# 

# In[1]:


# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


# In[2]:


# Access to the value by the key

Dict["key1"]


# In[3]:


# Access to the value by the key

Dict[(0, 1)]


# Each key is separated from its value by a colon "<code>:</code>".  Commas separate the items, and the whole dictionary is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this  "<code>{}</code>".

# In[4]:


# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsStructure.png" width="650">

# <a id="keys"></a>
# ## Keys

# In[5]:


# Get value by keys

release_year_dict['Thriller'] 


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsKeyOne.png" width="500">

# In[7]:


# Get value by key

release_year_dict['The Bodyguard'] 


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsKeyTwo.png" width="500">

# In[8]:


# Get all the keys in dictionary

release_year_dict.keys()


# In[9]:


# Get all the values in dictionary

release_year_dict.values() 


# We can add an entry:

# In[10]:


# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# In[11]:


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


# In[12]:


# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict


# <hr>

# <a id="quiz"></a>
# ## Quiz on Dictionaries

# In[13]:


# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 


# a) In the dictionary <code>soundtrack_dic</code> what are the keys ?

# In[17]:


soundtrack_dic.keys()


# b) In the dictionary <code>soundtrack_dic</code> what are the values ?

# In[18]:


soundtrack_dic.values()


# The Albums <b>Back in Black</b>, <b>The Bodyguard</b> and <b>Thriller</b> have the following music recording sales in millions 50, 50 and 65 respectively:

# a) Create a dictionary <code>album_sales_dict</code> where the keys are the album name and the sales in millions are the values.

# In[19]:


album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}


# b) Use the dictionary to find the total sales of <b>Thriller</b>:

# In[20]:


album_sales_dict["Thriller"]


# c) Find the names of the albums from the dictionary using the method <code>keys()</code>:

# In[21]:


album_sales_dict.keys()


# d) Find the values of the recording sales from the dictionary using the method <code>values</code>:
# 

# In[23]:


album_sales_dict.values()


# <a id="Scenario"></a>
# ## Scenario:Inventory Store

# The inventory store scenario project utilizes a dictionary-based approach to develop a robust system for managing and tracking inventory in a retail store.
# <br>
# **Note:- You will be working with two product details.**

# ## Task-1 Create an empty dictionary 
# 

# In[25]:


inventory ={}


# ## Task-2 Store the first product details in variable
# * Product Name= Mobile phone
# * Product Quantity= 5
# * Product price= 20000
# * Product Release Year= 2020

# In[29]:


ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020


# ## Task-3 Add the details in inventory

# In[30]:


inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_releaseYear"]=ProductNo1_releaseYear


# ## Task-4 Store the second product details in a variable.
# * Product Name= "Laptop"
# * Product Quantity= 10
# * Product price = 50000
# * Product Release Year= 2023

# In[31]:


ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023


# ## Task-5 Add the item detail into the inventory.
# 

# In[32]:


inventory["ProductNo2"]= ProductNo2
inventory["ProductNo2_quantity"]= ProductNo2_quantity
inventory["ProductNo2_price"]= ProductNo2_price
inventory["ProductNo2_releaseYear"]=ProductNo2_releaseYear


# ## Task-6 Display the Products present in the inventory
# 

# In[33]:


print(inventory)


# ## Task-7 Check if `ProductNo1_releaseYear` and `ProductNo2_releaseYear` is in the inventory

# In[35]:


"ProductNo1_releaseYear" in inventory
"ProductNo2_releaseYear" in inventory


# ## Task-8 Delete release year of both the products from the inventory
# 

# In[36]:


del(inventory["ProductNo1_releaseYear"])
del(inventory["ProductNo2_releaseYear"])


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>
# 
