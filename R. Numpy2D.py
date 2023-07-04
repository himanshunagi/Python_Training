#!/usr/bin/env python
# coding: utf-8

# # 2D Numpy in Python
#     
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * Operate comfortably with `numpy`
# * Perform complex operations with `numpy`
# 

# <h2 id="create">Create a 2D Numpy Array</h2>
# 

# In[1]:


# Import the libraries

import numpy as np 
import matplotlib.pyplot as plt


# Consider the list <code>a</code>, which contains three nested lists **each of equal size**. 
# 

# In[2]:


# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a


# We can cast the list to a Numpy Array as follows:
# 

# In[3]:


# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A


# We can use the attribute <code>ndim</code> to obtain the number of axes or dimensions, referred to as the rank. 
# 

# In[4]:


# Show the numpy array dimensions

A.ndim


# Attribute <code>shape</code> returns a tuple corresponding to the size or number of each dimension.
# 

# In[5]:


# Show the numpy array shape

A.shape


# The total number of elements in the array is given by the attribute <code>size</code>.
# 

# In[6]:


# Show the numpy array size

A.size


# <hr>
# 

# <h2 id="access">Accessing different elements of a Numpy Array</h2>
# 

# We can use rectangular brackets to access the different elements of the array. The correspondence between the rectangular brackets and the list and the rectangular representation is shown in the following figure for a 3x3 array:  
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoEg.png" width="500">
# 

# We can access the 2nd-row, 3rd column as shown in the following figure:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoFT.png" width="400">
# 

#  We simply use the square brackets and the indices corresponding to the element we would like:
# 

# In[7]:


# Access the element on the second row and third column

A[1, 2]


#  We can also use the following notation to obtain the elements: 
# 

# In[8]:


# Access the element on the second row and third column

A[1][2]


#  Consider the elements shown in the following figure 
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoFF.png" width="400">
# 

# We can access the element as follows: 
# 

# In[9]:


# Access the element on the first row and first column

A[0][0]


# We can also use slicing in numpy arrays. Consider the following figure. We would like to obtain the first two columns in the first row
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoFSF.png" width="400">
# 

#  This can be done with the following syntax: 
# 

# In[10]:


# Access the element on the first row and first and second columns

A[0][0:2]


# Similarly, we can obtain the first two rows of the 3rd column as follows:
# 

# In[11]:


# Access the element on the first and second rows and third column

A[0:2, 2]


# Corresponding to the following figure: 
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/2D_numpy.png" width="550"><br />
# 

# <h2 id="op">Basic Operations</h2>
# 

# We can also add arrays. The process is identical to matrix addition. Matrix addition of <code>X</code> and <code>Y</code> is shown in the following figure:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoAdd.png" width="500">
# 

# The numpy array is given by <code>X</code> and <code>Y</code>
# 

# In[12]:


# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X


# In[13]:


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y


#  We can add the numpy arrays as follows.
# 

# In[14]:


# Add X and Y

Z = X + Y
Z


# Multiplying a numpy array by a scaler is identical to multiplying a matrix by a scaler. If we multiply the matrix <code>Y</code> by the scaler 2, we simply multiply every element in the matrix by 2, as shown in the figure.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoDb.png" width="500">
# 

# We can perform the same operation in numpy as follows 
# 

# In[15]:


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y


# In[16]:


# Multiply Y with 2

Z = 2 * Y
Z


# Multiplication of two arrays corresponds to an element-wise product or <em>Hadamard product</em>. Consider matrix <code>X</code> and <code>Y</code>. The Hadamard product corresponds to multiplying each of the elements in the same position, i.e. multiplying elements contained in the same color boxes together. The result is a new matrix that is the same size as matrix <code>Y</code> or <code>X</code>, as shown in the following figure.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumTwoMul.png" width="500">
# 

# We can perform element-wise product of the array <code>X</code> and <code>Y</code> as follows:
# 

# In[17]:


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y


# In[18]:


# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X


# In[19]:


# Multiply X with Y

Z = X * Y
Z


# We can also perform matrix multiplication with the numpy arrays <code>A</code> and <code>B</code> as follows:
# 

# First, we define matrix <code>A</code> and <code>B</code>:
# 

# In[20]:


# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
A


# In[21]:


# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])
B


# We use the numpy function <code>dot</code> to multiply the arrays together.
# 

# In[22]:


# Calculate the dot product

Z = np.dot(A,B)
Z


# In[23]:


# Calculate the sine of Z

np.sin(Z)


# We use the numpy attribute <code>T</code> to calculate the transposed matrix
# 

# In[24]:


# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
C


# In[25]:


# Get the transposed of C

C.T


# <h2>Quiz on 2D Numpy Array</h2>
# 

# Consider the following list <code>a</code>, convert it to Numpy Array. 
# 

# In[26]:


# Write your code below and press Shift+Enter to execute

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
A


# Calculate the numpy array size.
# 

# In[27]:


# Write your code below and press Shift+Enter to execute
A.size


# Access the element on the first row and first and second columns.
# 

# In[28]:


# Write your code below and press Shift+Enter to execute
A[0][0:2]


# Perform matrix multiplication with the numpy arrays <code>A</code> and <code>B</code>.
# 

# In[29]:


# Write your code below and press Shift+Enter to execute

B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
X = np.dot(A,B)
X


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>
# 
