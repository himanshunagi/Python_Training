#!/usr/bin/env python
# coding: utf-8

# # Tuples in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Perform the basics tuple operations in Python, including indexing, slicing and sorting

# <h2 id="tuple">Tuples</h2>

# In Python, there are different data types: String, Integer, and Float. These data types can all be contained in a tuple as follows:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesType.png" width="750" align="center">
# 

# In[2]:


# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1


# In[3]:


# Print the type of the tuple you created

type(tuple1)


# <h3 id="index">Indexing</h3>
# 

# Each element of a tuple can be accessed via an index. The following table represents the relationship between the index and the items in the tuple. Each element can be obtained by the name of the tuple followed by a square bracket with the index number:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesIndex.gif" width="750" align="center">
# 

# In[5]:


# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


# In[6]:


# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesNeg.png" width="750" align="center">
# 

# In[7]:


# Use negative index to get the value of the last element

tuple1[-1]


# In[8]:


# Use negative index to get the value of the second last element

tuple1[-2]


# In[9]:


# Use negative index to get the value of the third last element

tuple1[-3]


# <h3 id="concate">Concatenate Tuples</h3>
# 

# We can concatenate or combine tuples by using the **+** sign:
# 

# In[10]:


# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesSlice.gif" width="750" align="center">
# 

# <h3 id="slice">Slicing</h3>
# 

# In[11]:


# Slice from index 0 to index 2

tuple2[0:3]


# In[12]:


# Slice from index 3 to index 4

tuple2[3:5]


# In[13]:


# Get the length of tuple

len(tuple2)


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesElement.png" width="750" align="center">
# 

# <h3 id="sort">Sorting</h3>

# Consider the following tuple:

# In[15]:


# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)


# In[16]:


# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted


# <h3 id="nest">Nested Tuple</h3>
# 

# A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. Consider the following tuple with several elements:
# 

# In[18]:


# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesNestOne.png" width="750" align="center">
# 

# In[19]:


# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesNestTwo.png" width="750" align="center">
# 

# In[20]:


# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


# In[21]:


# Print the first element in the second nested tuples

NestedT[2][1][0]


# In[22]:


# Print the second element in the second nested tuples

NestedT[2][1][1]


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesNestThree.gif" width="750" align="center">

# In[23]:


# Print the first element in the second nested tuples

NestedT[4][1][0]


# In[24]:


# Print the second element in the second nested tuples

NestedT[4][1][1]


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/TuplesNestFour.gif" width="750" align="center">

# <h2 id="quiz">Quiz on Tuples</h2>

# In[25]:


# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple


# Find the length of the tuple, <code>genres_tuple</code>:

# In[27]:


len(genres_tuple)


# Access the element, with respect to index 3:

# In[29]:


genres_tuple[3]


# Use slicing to obtain indexes 3, 4 and 5:

# In[30]:


genres_tuple[3:6]


# Find the first two elements of the tuple <code>genres_tuple</code>:

# In[31]:


genres_tuple[0:2]


# Find the first index of <code>"disco"</code>:

# In[32]:


genres_tuple.index("disco")


# Generate a sorted List from the Tuple <code>C_tuple=(-5, 1, -3)</code>:

# In[33]:


C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
C_list


# In[ ]:




