#!/usr/bin/env python
# coding: utf-8

# # Introduction to Pandas in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * Use Pandas to access and view data

# The table has one row for each album and several columns.
# 
# <ul>
#     <li><b>artist</b>: Name of the artist</li>
#     <li><b>album</b>: Name of the album</li>
#     <li><b>released_year</b>: Year the album was released</li>
#     <li><b>length_min_sec</b>: Length of the album (hours,minutes,seconds)</li>
#     <li><b>genre</b>: Genre of the album</li>
#     <li><b>music_recording_sales_millions</b>: Music recording sales (millions in USD) on <a href="http://www.song-database.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2023-01-01">[SONG://DATABASE]</a></li>
#     <li><b>claimed_sales_millions</b>: Album's claimed sales (millions in USD) on <a href="http://www.song-database.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2023-01-01">[SONG://DATABASE]</a></li>
#     <li><b>date_released</b>: Date on which the album was released</li>
#     <li><b>soundtrack</b>: Indicates if the album is the movie soundtrack (Y) or (N)</li>
#     <li><b>rating_of_friends</b>: Indicates the rating from your friends from 1 to 10</li>
# </ul>
# 
# You can see the dataset here:
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
#     <td>Fleetwood Mac</td>
#     <td>Rumours</td> 
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

# <h2 id="pandas">Introduction of <code>Pandas</code></h2>

# In[2]:


# Dependency needed to install file 

get_ipython().system('pip install xlrd')
get_ipython().system('pip install openpyxl')


# In[3]:


# Import required library

import pandas as pd


# After the import command, we now have access to a large number of pre-built classes and functions. This assumes the library is installed; in our lab environment all the necessary libraries are installed. One way pandas allow you to work with data is a dataframe. Let's go through the process to go from a comma separated values (<b>.csv</b>) file to a dataframe. This variable <code>csv_path</code> stores the path of the <b>.csv</b>, which is used as an argument to the <code>read_csv</code> function. The result is stored in the object <code>df</code>, this is a common short form used for a variable referring to a Pandas dataframe.

# In[4]:


# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)


# In[5]:


# Print first five rows of the dataframe

df.head()


# In[6]:


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()


# In[7]:


# Access to the column Length

x = df[['Length']]
x


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/DataEgOne.png" width="750">

# <h2 id="data">Viewing Data and Accessing Data</h2>

# In[8]:


# Get the column as a series

x = df['Length']
x


# In[9]:


# Get the column as a dataframe

x = df[['Artist']]
type(x)


# In[10]:


# Access to multiple columns

y = df[['Artist','Length','Genre']]
y


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/DataEgTwo.png" width="1100">

# In[11]:


# Access the value on the first row and the first column

df.iloc[0, 0]


# In[12]:


# Access the value on the second row and the first column

df.iloc[1,0]


# In[13]:


# Access the value on the first row and the third column

df.iloc[0,2]


# In[14]:


# Access the value on the second row and the third column
df.iloc[1,2]


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/2_loc.PNG" width="750">

# In[15]:


# Access the column using the name

df.loc[0, 'Artist']


# In[16]:


# Access the column using the name

df.loc[1, 'Artist']


# In[17]:


# Access the column using the name

df.loc[0, 'Released']


# In[18]:


# Access the column using the name

df.loc[1, 'Released']


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/1_loc.png" width="750">
# 

# In[19]:


# Slicing the dataframe

df.iloc[0:2, 0:3]


# In[20]:


# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']


# Use a variable <code>q</code> to store the column <b>Rating</b> as a dataframe
# 

# In[21]:


q = df[['Rating']]
q


# In[22]:


q = df[['Released', 'Artist']]
q


# Access the 2nd row and the 3rd column of <code>df</code>:
# 

# In[23]:


df.iloc[1, 2]


# Use the following list to convert the dataframe index <code>df</code> to characters and assign it to <code>df_new</code>; find the element corresponding to the row index <code>a</code> and column  <code>'Artist'</code>. Then select the rows <code>a</code> through <code>d</code> for the column  <code>'Artist'</code>
# 

# In[24]:


new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>
# 

# In[ ]:




