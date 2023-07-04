#!/usr/bin/env python
# coding: utf-8

# # Reading Files Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# -   Read text files using Python libraries
# 

# <h2 id="download">Download Data</h2>
# 

# In[1]:


import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)


# In[3]:


pip install requests


# In[5]:


import requests

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite'
filename = 'm4_survey_data.sqlite'

response = requests.get(url)
with open(filename, 'wb') as file:
    file.write(response.content)


# <hr>
# 

# <h2 id="read">Reading Text Files</h2>
# 

# One way to read or write a file in Python is to use the built-in <code>open</code> function. The <code>open</code> function provides a **File object** that contains the methods and attributes you need in order to read, save, and manipulate the file. In this notebook, we will only cover **.txt** files. The first parameter you need is the file path and the file name. An example is shown as follow:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/ReadOpen.png" width="500">
# 

#  The mode argument is optional and the default value is **r**. In this notebook we only cover two modes: 
# 
# <ul>
#     <li>**r**: Read mode for reading files </li>
#     <li>**w**: Write mode for writing files</li>
# </ul>
# 

# For the next example, we will use the text file **Example1.txt**. The file is shown as follows:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/ReadFile.png" width="100">
# 

#  We read the file: 
# 

# In[6]:


# Read the Example1.txt

example1 = "Example1.txt"
file1 = open(example1, "r")


#  We can view the attributes of the file.
# 

# In[7]:


# Print the path of file

file1.name


#  The mode the file object is in:
# 

# In[8]:


# Print the mode of file, either 'r' or 'w'

file1.mode


# We can read the file and assign it to a variable :
# 

# In[9]:


# Read the file

FileContent = file1.read()
FileContent


# The **/n** means that there is a new line. 
# 

# We can print the file: 
# 

# In[10]:


# Print the file with '\n' as a new line

print(FileContent)


# The file is of type string:
# 

# In[11]:


# Type of file content

type(FileContent)


# It is very important that the file is closed in the end. This frees up resources and ensures consistency across different python versions.
# 

# In[12]:


# Close file after finish

file1.close()


# <hr>
# 

# <h2 id="better">A Better Way to Open a File</h2>
# 

# Using the <code>with</code> statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object. 
# 

# In[13]:


# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)


# The file object is closed, you can verify it by running the following cell:  
# 

# In[14]:


# Verify if the file is closed

file1.closed


#  We can see the info in the file:
# 

# In[15]:


# See the content of file

print(FileContent)


# The syntax is a little confusing as the file object is after the <code>as</code> statement. We also don’t explicitly close the file. Therefore we summarize the steps in a figure:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/ReadWith.png" width="500">
# 

# We don’t have to read the entire file, for example, we can read the first 4 characters by entering three as a parameter to the method **.read()**:
# 

# In[16]:


# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))


# Once the method <code>.read(4)</code> is called the first 4 characters are called. If we call the method again, the next 4 characters are called. The output for the following cell will demonstrate the process for different inputs to the method <code>read()</code>:
# 

# In[17]:


# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))


# The process is illustrated in the below figure, and each color represents the part of the file read after the method <code>read()</code> is called:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/read.png" width="500">
# 

#  Here is an example using the same file, but instead we read 16, 5, and then 9 characters at a time: 
# 

# In[18]:


# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))


# We can also read one line of the file at a time using the method <code>readline()</code>: 
# 

# In[19]:


# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())


# We can also pass an argument to <code> readline() </code> to specify the number of charecters we want to read. However, unlike <code> read()</code>, <code> readline()</code> can only read one line at most.
# 

# In[20]:


with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


#  We can use a loop to iterate through each line: 
# 

# In[21]:


# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1


# We can use the method <code>readlines()</code> to save the text file to a list: 
# 

# In[22]:


# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()


#  Each element of the list corresponds to a line of text:
# 

# In[23]:


# Print the first line

FileasList[0]


# # Print the second line
# 
# FileasList[1]
# 

# In[24]:


# Print the third line

FileasList[2]


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python.
# <hr>
# 
