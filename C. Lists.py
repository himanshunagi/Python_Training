#!/usr/bin/env python
# coding: utf-8

# # Lists in Python
# Perform list operations in Python, including indexing, list manipulation, and copy/clone list.

# <h2 id="#dataset">About the Dataset</h2>

# Imagine you received album recommendations from your friends and compiled all of the recommandations into a table, with specific information about each album.
# 
# The table has one row for each movie and several columns:
# 
# *   **Artist** - Name of the artist
# *   **Album** - Name of the album
# *   **Released_year** - Year the album was released
# *   **Length_min_sec** - Length of the album (hours,minutes,seconds)
# *   **Genre** - Genre of the album
# *   **Music_recording_sales_millions** - Music recording sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01)
# *   **Claimed_sales_millions** - Album's claimed sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01)
# *   **Released** - Date on which the album was released
# *   **Soundtrack** - Indicates if the album is the movie soundtrack (Y) or (N)
# *   **Rating_of_friends** - Indicates the rating from your friends from 1 to 10
# 
# <br>
# <br>
# 
# The Dataset can be seen below:
# 
# <font size="1">
# <table font-size:xx-small>
#   <tr>
#     <th>Artist</th>
#     <th>Album</th> 
#     <th>Released</th>
#     <th>Length</th>
#     <th>Genre</th> 
#     <th>Music recording sales (millions)</th>
#     <th>Claimed sales (millions)</th>
#     <th>Released</th>
#     <th>Soundtrack</th>
#     <th>Rating (friends)</th>
#   </tr>
#   <tr>
#     <td>Michael Jackson</td>
#     <td>Thriller</td> 
#     <td>1982</td>
#     <td>00:42:19</td>
#     <td>Pop, rock, R&B</td>
#     <td>46</td>
#     <td>65</td>
#     <td>30-Nov-82</td>
#     <td></td>
#     <td>10.0</td>
#   </tr>
#   <tr>
#     <td>AC/DC</td>
#     <td>Back in Black</td> 
#     <td>1980</td>
#     <td>00:42:11</td>
#     <td>Hard rock</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td></td>
#     <td>8.5</td>
#   </tr>
#     <tr>
#     <td>Pink Floyd</td>
#     <td>The Dark Side of the Moon</td> 
#     <td>1973</td>
#     <td>00:42:49</td>
#     <td>Progressive rock</td>
#     <td>24.2</td>
#     <td>45</td>
#     <td>01-Mar-73</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Whitney Houston</td>
#     <td>The Bodyguard</td> 
#     <td>1992</td>
#     <td>00:57:44</td>
#     <td>Soundtrack/R&B, soul, pop</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td>Y</td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Meat Loaf</td>
#     <td>Bat Out of Hell</td> 
#     <td>1977</td>
#     <td>00:46:33</td>
#     <td>Hard rock, progressive rock</td>
#     <td>20.6</td>
#     <td>43</td>
#     <td>21-Oct-77</td>
#     <td></td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Eagles</td>
#     <td>Their Greatest Hits (1971-1975)</td> 
#     <td>1976</td>
#     <td>00:43:08</td>
#     <td>Rock, soft rock, folk rock</td>
#     <td>32.2</td>
#     <td>42</td>
#     <td>17-Feb-76</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Bee Gees</td>
#     <td>Saturday Night Fever</td> 
#     <td>1977</td>
#     <td>1:15:54</td>
#     <td>Disco</td>
#     <td>20.6</td>
#     <td>40</td>
#     <td>15-Nov-77</td>
#     <td>Y</td>
#     <td>9.0</td>
#   </tr>
#     <tr>
#     <td>Fleet wood Mac</td>
#     <td> Rumours </td> 
#     <td>1977</td>
#     <td>00:40:01</td>
#     <td>Soft rock</td>
#     <td>27.9</td>
#     <td>40</td>
#     <td>04-Feb-77</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
# </table></font>
# 

# <h2 id="list">Lists</h2>

# <h3 id="index">Indexing</h3>

# We are going to take a look at lists in Python. A list is a sequenced collection of different objects such as integers, strings, and even other lists as well. The address of each element within a list is called an <b>index</b>. An index is used to access and refer to items within a list.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsIndex.png" width="1000">
# 

# To create a list, type the list within square brackets <b>\[ ]</b>, with your content inside the parenthesis and separated by commas. Let us try it!

# In[1]:


# Create a list

L = ["Michael Jackson", 10.1, 1982]
L


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsNeg.png" width="1000">
# 

# In[2]:


# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


# <h3 id="content">List Content</h3>

# Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. The same indexing conventions apply for nesting:

# In[4]:


# Sample List

["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]


# <h3 id="op">List Operations</h3>

# We can also perform slicing in lists. For example, if we want the last two elements, we use the following command:

# In[6]:


# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
L


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsSlice.png" width="1000">

# In[7]:


# List slicing

L[3:5]


# We can use the method <code>extend</code> to add new elements to the list:

# In[8]:


# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L


# Another similar method is <code>append</code>. If we apply <code>append</code> instead of <code>extend</code>, we add one element to the list:

# In[9]:


# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L


# If we append the list  <code>\['a','b']</code> we have one new element consisting of a nested list:

# In[10]:


# Use append to add elements to list

L.append(['a','b'])
L


# As lists are mutable, we can change them. For example, we can change the first element as follows:
# 

# In[11]:


# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


# We can also delete an element of a list using the <code>del</code> command:
# 

# In[13]:


# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)


# In[14]:


# Split the string, default is by space

'hard rock'.split()


# In[15]:


# Split the string by comma

'A,B,C,D'.split(',')


# <h3 id="co">Copy and Clone List</h3>

# When we set one variable <b>B</b> equal to <b>A</b>, both <b>A</b> and <b>B</b> are referencing the same list in memory:

# In[17]:


# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsRef.png" width="1000" align="center">

# In[18]:


# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsRefGif.gif" width="1000">

# In[19]:


# Clone (clone by value) the list A

B = A[:]
B


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsVal.gif" width="1000">

# In[20]:


print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])


# <h2 id="quiz">Quiz on List</h2>

# Create a list <code>a_list</code>, with the following elements <code>1</code>, <code>hello</code>, <code>\[1,2,3]</code> and <code>True</code>.

# In[21]:


a_list = ["1","hello",[1,2,3],"True"]


# In[22]:


a_list[1]


# Retrieve the elements stored at index 1, 2 and 3 of <code>a_list</code>.

# In[23]:


a_list[1:4]


# Concatenate the following lists <code>A = \[1, 'a']</code> and <code>B = \[2, 1, 'd']</code>:

# In[25]:


A = [1, 'a']
B = [2, 1, 'd']
A+B


# <center> 
# 
# # Scenario : Shopping list 
#     
# </center>

# # Task-1  Create an empty list
# At first we need to create a empty list for storing the items to buy in Shopping list.
# 

# In[26]:


Shopping_list=[]


# # Task-2 Now store the number of items to the shopping_list
# * Watch
# * Laptop
# * Shoes
# * Pen
# * Clothes
# 
# 
# <br>

# In[27]:


Shopping_list=['Watch','Laptop','Shoes','Pen','Clothes']


# # Task-3 Add a new item to the shopping_list
# Seems like I missed one item "Football" to add in the shopping list.
# <br>
# 

# In[28]:


Shopping_list=['Watch','Laptop','Shoes','Pen','Clothes']
Shopping_list.extend(['Football'])
Shopping_list


# # Task-4 Print First item from the shopping_list
# Let's check the first item that we need to buy.
# <br>

# In[29]:


Shopping_list[0]


# # Task-5 Print Last item from the shopping_list
# Let's check the last time that we need to buy.
# <br>

# In[31]:


Shopping_list[-1]


# # Task-6 Print the entire Shopping List

# In[32]:


Shopping_list


# # Task-7 Print the item that are important to buy from the Shopping List
# Print "Laptop" and "shoes"

# In[33]:


Shopping_list[1:3]


# # Task-8 Change the item from the shopping_list 
# Instead of <u>"Pen"</u> I want to buy <u>"Notebook"</u>
# let's change the item stored in the list.
# <br>

# In[35]:


Shopping_list[3]='Notebook'
Shopping_list


# # Task-9 Delete the item from the shopping_list that is not required
# Let's delete items that are unimportant, such as; I don't want to buy <u>Clothes</u>, let's delete it.
# <br>

# In[39]:


del(Shopping_list[4])
Shopping_list


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>

# In[ ]:




