#!/usr/bin/env python
# coding: utf-8

# # Practice Lab: Selecting data in a Dataframe
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Use Pandas Library to create DataFrame and Series
# *   Locate data in the DataFrame using <code>loc()</code> and <code>iloc()</code> functions
# *   Use slicing

# ### Exercise 1: Pandas: DataFrame and Series 
# 
# **Pandas** is a popular library for data analysis built on top of the Python programming language. Pandas generally provide two data structures for manipulating data, They are: 
#  
# * DataFrame
# * Series
# 
# A **DataFrame** is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# 
# * A Pandas DataFrame will be created by loading the datasets from existing storage. 
# * Storage can be SQL Database, CSV file, Excel file, etc. 
# * It can also be created from the lists, dictionaries, and from a list of dictionaries.
# 
# **Series** represents a one-dimensional array of indexed data.
# It has two main components :
# 1. An array of actual data.
# 2. An associated array of indexes or data labels.
# 
# The index is used to access individual data values. You can also get a column of a dataframe as a **Series**. You can think of a Pandas series as a 1-D dataframe. 

# In[1]:


# let us import the Pandas Library
import pandas as pd


# Let us consider a dictionary 'x' with keys and values as shown below.
# 
# We then create a dataframe from the dictionary using the function pd.DataFrame(dict)

# In[2]:


#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df


# #### Column Selection:
# 
# To select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name. 
# 
# Let's Retrieve the data present in the <code>ID</code> column.

# In[3]:


#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x


# Let's use the <code>type()</code> function and check the type of the variable.

# In[4]:


#check the type of x
type(x)


# #### Access to multiple columns
# 
# Let us retrieve the data for <code>Department</code>, <code>Salary</code> and <code>ID</code> columns

# In[6]:


#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z


# ##### Problem 1: Create a dataframe to display the result as below:

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/Student_data.png" width="300" alt="Student Data">
# </center>

# In[7]:


a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df1 = pd.DataFrame(a)
df1


# ##### Problem 2: Retrieve the Marks column and assign it to a variable b

# In[8]:


b = df1[['Marks']]
b


# ##### Problem 3: Retrieve the Country and Course columns and assign it to a variable c

# In[9]:


c = df1[['Country','Course']]
c


# #### To view the column as a series, just use one bracket:

# In[10]:


# Get the Student column as a series Object

x = df1['Student']
x


# In[11]:


#check the type of x
type(x)


# ### Exercise 2: <code>loc()</code> and <code>iloc()</code> functions
# 
# <code>loc()</code> is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. This method includes the last element of the range passed in it.
# 
# Simple syntax for your understanding: 
# 
#  - loc[row_label, column_label]
# 
# <code>iloc()</code> is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it.
# 
# Simple syntax for your understanding: 
#    
#  - iloc[row_index, column_index]
# 
# <h4 id="data">Let us see some examples on the same.</h4>

# In[12]:


# Access the value on the first row and the first column

df.iloc[0, 0]


# In[13]:


# Access the value on the first row and the third column

df.iloc[0,2]


# In[14]:


# Access the column using the name

df.loc[0, 'Salary']


# In[15]:


df2=df
df2=df2.set_index("Name")


# In[16]:


#To display the first 5 rows of new dataframe
df2.head()


# In[17]:


#Now, let us access the column using the name
df2.loc['Jane', 'Salary']


# In[18]:


df2.loc['Jane', 'Department']


# In[19]:


df2.iloc[3,2]


# ### Exercise 3: Slicing
# 
# Slicing uses the [] operator to select a set of rows and/or columns from a DataFrame.
# 
# To slice out a set of rows, you use this syntax: data[start:stop], 
# 
# here the start represents the index from where to consider, and stop represents the index one step BEYOND the row you want to select. You can perform slicing using both the index and the name of the column.
# 
# > NOTE: When slicing in pandas, the start bound is included in the output.
# 
# So if you want to select rows 0, 1, and 2 your code would look like this: df.iloc[0:3].
# 
# It means you are telling Python to start at index 0 and select rows 0, 1, 2 up to but not including 3.
# 
# > NOTE: Labels must be found in the DataFrame or you will get a KeyError.
# 
# Indexing by labels(i.e. using <code>loc()</code>) differs from indexing by integers (i.e. using <code>iloc()</code>). With <code>loc()</code>, both the start bound and the stop bound are inclusive. When using <code>loc()</code>, integers can be used, but the integers refer to the index label and not the position. 
# 
# For example, using <code>loc()</code> and select 1:4 will get a different result than using <code>iloc()</code> to select rows 1:4.
# 
# <h4 id="data">We can also select a specific data value using a row and column location within the DataFrame and iloc indexing.
# 

# In[20]:


# let us do the slicing using old dataframe df

df.iloc[0:2, 0:3]


# In[21]:


#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']


# In[22]:


#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']


# using <code>loc()</code> function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3

# In[23]:


df.loc[2:3,'Name':'Department']


# <h3 id="quiz">Congratulations, you have completed this lesson and the practice lab on Pandas</h3>

# In[ ]:




