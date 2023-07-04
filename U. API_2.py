#!/usr/bin/env python
# coding: utf-8

# # Simple APIs 
# ## Random User and Fruitvice API Examples
# 
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Load and use RandomUser API, using `RandomUser()` Python library
# *   Load and use Fruitvice API, using `requests` Python library

# The purpose of this notebook is to provide more examples on how to use simple APIs. As you have already learned from previous videos and notebooks, API stands for Application Programming Interface and is a software intermediary that allows two applications to talk to each other. 
# 
# The advantages of using APIs:
#  *   **Automation**. Less human effort is required and workflows can be easily updated to become faster and more      
#      productive.
#  *   **Efficiency**. It allows to use the capabilities of one of the already developed APIs than to try to 
#      independently implement some functionality from scratch.
#  
# The disadvantage of using APIs:
#  *   **Security**. If the API is poorly integrated, it means it will be vulnerable to attacks, resulting in data breeches or losses having financial or reputation implications.
# 
# One of the applications we will use in this notebook is Random User Generator. RandomUser is an open-source, free API providing developers with randomly generated users to be used as placeholders for testing purposes. This makes the tool similar to Lorem Ipsum, but is a placeholder for people instead of text. The API can return multiple results, as well as specify generated user details such as gender, email, image, username, address, title, first and last name, and more. More information on [RandomUser](https://randomuser.me/documentation?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2023-01-01#intro) can be found here.
# 
# Another example of simple API we will use in this notebook is Fruitvice application. The Fruitvice API webservice which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The webservice is completely free to use and contribute to.
# 

# ## Example 1: RandomUser API
# Bellow are Get Methods parameters that we can generate. For more information on the parameters, please visit this [documentation](https://randomuser.me/documentation?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2023-01-01) page.
# 

# ## **Get Methods**
# 
# - get_cell()
# - get_city()
# - get_dob()
# - get_email()
# - get_first_name()
# - get_full_name()
# - get_gender()
# - get_id()
# - get_id_number()
# - get_id_type()
# - get_info()
# - get_last_name()
# - get_login_md5()
# - get_login_salt()
# - get_login_sha1()
# - get_login_sha256()
# - get_nat()
# - get_password()
# - get_phone()
# - get_picture()
# - get_postcode()
# - get_registered()
# - get_state()
# - get_street()
# - get_username()
# - get_zipcode()
# 

# To start using the API you can install the `randomuser` library running the `pip install` command.
# 

# In[1]:


get_ipython().system('pip install randomuser')


# Then, we will load the necessary libraries.
# 

# In[2]:


from randomuser import RandomUser
import pandas as pd


# First, we will create a random user object, r.
# 

# In[3]:


r = RandomUser()


# Then, using `generate_users()` function, we get a list of random 10 users.
# 

# In[4]:


some_list = r.generate_users(10)


# In[5]:


some_list


# The **"Get Methods"** functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset. For example, to get full name, we call `get_full_name()` function.
# 

# In[6]:


name = r.get_full_name()


# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
# 

# In[7]:


for user in some_list:
    print (user.get_full_name()," ",user.get_email())


# ## Exercise 1
# In this Exercise, generate photos of the random 5 users.
# 

# In[9]:


## Write your code here
for user in some_list:
    print (user.get_picture())


# To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
# 

# In[10]:


def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     


# In[11]:


get_users()


# In[12]:


df1 = pd.DataFrame(get_users())  


# Now we have a *pandas* dataframe that can be used for any testing purposes that the tester might have.
# 

# ## Example 2: Fruitvice API
# 
# Another, more common way to use APIs, is through `requests` library. The next lab, Requests and HTTP, will contain more information about requests.
# 
# We will start by importing all required libraries.
# 

# In[13]:


import requests
import json


# We will obtain the [fruitvice](https://www.fruityvice.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2023-01-01) API data using `requests.get("url")` function. The data is in a json format.
# 

# In[14]:


data = requests.get("https://fruityvice.com/api/fruit/all")


# We will retrieve results using `json.loads()` function.
# 

# In[15]:


results = json.loads(data.text)


# We will convert our json data into *pandas* data frame. 
# 

# In[16]:


pd.DataFrame(results)


# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
# 

# In[17]:


df2 = pd.json_normalize(results)


# In[18]:


df2


# Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
# 

# In[19]:


cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])


# ## Exercise 2
# In this Exercise, find out how many calories are contained in a banana.
# 

# In[20]:


# Write your code here

cal_banana = df2.loc[df2["name"] == 'Banana']
cal_banana.iloc[0]['nutritions.calories']


# ## Exercise 3
# 
# This [page](https://github.com/public-apis/public-apis#animals) contains a list of free public APIs. Choose any API of your interest and use it to load/extract some information, as shown in the example above.
# 1. Using `requests.get("url")` function, load your data.
# 

# In[24]:


# Write your code here
data2 = requests.get("https://www.fishwatch.gov/api/species")


# 2. Retrieve results using `json.loads()` function.
# 

# In[27]:


# Write your code here
results2 = json.loads(data2.text)


# 3. Convert json data into *pandas* data frame. 
# 

# In[28]:


# Write your code here
df3 = pd.DataFrame(results2)
df3


# # Congratulations! - You have completed the lab
# 
