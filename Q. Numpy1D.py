#!/usr/bin/env python
# coding: utf-8

# # 1D Numpy in Python
# 
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Import and use the `numpy` library
# *   Perform operations with `numpy`
# 

# ### Create a Python List as follows:
# 

# In[1]:


# Create a python list

a = ["0", 1, "two", "3", 4]


# We can access the data via an index:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumOneList.png" width="660">
# 

# We can access each element using a square bracket as follows:
# 

# In[2]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# <hr>
# 

# <h2 id="numpy">What is Numpy?</h2>
# 

# NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices.A numpy array is similar to a list. NumPy stands for Numerical Python and it is an open source project.The array object in NumPy is called **ndarray**, it provides a lot of supporting functions that make working with ndarray very easy.
# 
# Arrays are very frequently used in data science, where speed and resources are very important.
# 
# NumPy is usually imported under the np alias.
# 
# It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing `numpy`:
# 

# In[3]:


# import numpy library

import numpy as np 


# We then cast the list as follows:
# 

# In[4]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# Each element is of the same type, in this case integers:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumOneNp.png" width="500">
# 

# As with lists, we can access each element via a square bracket:
# 

# In[5]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# ### Checking NumPy Version
# 
# The version string is stored under __version__ attribute.
# 

# In[6]:


print(np.__version__)


# <h3 id="type">Type</h3>
# 

# If we check the type of the array we get <b>numpy.ndarray</b>:
# 

# In[7]:


# Check the type of the array

type(a)


# As numpy arrays contain data of the same type, we can use the attribute "dtype" to obtain the data type of the array’s elements. In this case, it's a 64-bit integer:
# 

# In[8]:


# Check the type of the values stored in numpy array

a.dtype


# ### Try it yourself
# 
# Check the type of the array and Value type for the given array **c**
# 

# In[10]:


b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Enter your code here
b.dtype


# <h3 id="val">Assign value</h3>
# 

# We can change the value of the array. Consider the array <code>c</code>:
# 

# In[11]:


# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c


# We can change the first element of the array to 100 as follows:
# 

# In[12]:


# Assign the first element to 100

c[0] = 100
c


# We can change the 5th element of the array to 0 as follows:
# 

# In[13]:


# Assign the 5th element to 0

c[4] = 0
c


# ### Try it yourself
# 
# Assign the value 20 for the second element in the given array.
# 

# In[16]:


a = np.array([10, 2, 30, 40,50])

# Enter your code here
a[1] = 20 
a


# <h3 id="slice">Slicing</h3>
# 

# Like lists, we can slice the numpy array. Slicing in python means taking the elements from the given index to another given index.
# 
# We pass slice like this: [start:end].The element at end index is not being included in the output.
# 
# We can select the elements from 1 to 3 and assign it to a new numpy array <code>d</code> as follows:
# 

# In[17]:


# Slicing the numpy array

d = c[1:4]
d


# We can assign the corresponding indexes to new values as follows:
# 

# In[18]:


# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c


# We can also define the steps in slicing, like this: [start:end:step].
# 

# In[19]:


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


# If we don't pass start its considered 0
# 

# In[20]:


print(arr[:4])


# If we don't pass end it considers till the length of array.
# 

# In[21]:


print(arr[4:])


# If we don't pass step its considered 1
# 

# In[22]:


print(arr[1:5:])


# ### Try it yourself
# 
# Print the even elements in the given array.
# 

# In[24]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Enter your code here
print(arr[1:8:2])


# <h3 id="list">Assign Value with List</h3>
# 

# Similarly, we can use a list to select more than one specific index.
# The list `select` contains several values:
# 

# In[25]:


# Create the index list

select = [0, 2, 3, 4]
select


# We can use the list as an argument in the brackets. The output is the elements corresponding to the particular indexes:
# 

# In[26]:


# Use List to select elements

d = c[select]
d


# We can assign the specified elements to a new value. For example, we can assign the values to 100 000 as follows:
# 

# In[27]:


# Assign the specified elements to new value

c[select] = 100000
c


# <h3 id="other">Other Attributes</h3>
# 

# Let's review some basic array attributes using the array <code>a</code>:
# 

# In[28]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# The attribute <code>size</code> is the number of elements in the array:
# 

# In[29]:


# Get the size of numpy array

a.size


# The next two attributes will make more sense when we get to higher dimensions but let's review them. The attribute <code>ndim</code> represents the number of array dimensions, or the rank of the array. In this case, one:
# 

# In[30]:


# Get the number of dimensions of numpy array

a.ndim


# The attribute <code>shape</code> is a tuple of integers indicating the size of the array in each dimension:
# 

# In[31]:


# Get the shape/size of numpy array

a.shape


# ### Try it yourself
# 
# Find the size ,dimension and shape for the given array **b**
# 

# In[33]:


b = np.array([10, 20, 30, 40, 50, 60, 70])

# Enter your code here
b.size

b.ndim

b.shape


# ### Numpy Statistical Functions
# 

# In[34]:


# Create a numpy array

a = np.array([1, -1, 1, -1])


# In[35]:


# Get the mean of numpy array

mean = a.mean()
mean


# In[36]:


# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation


# In[37]:


# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b


# In[38]:


# Get the biggest value in the numpy array

max_b = b.max()
max_b


# In[39]:


# Get the smallest value in the numpy array

min_b = b.min()
min_b


# ### Try it yourself
# 
# Find the sum of maximum and minimum value in the given numpy array
# 

# <hr>
# 

# In[40]:


c = np.array([-10, 201, 43, 94, 502])

# Enter your code here
max_c = c.max()
max_c
    
min_c = c.min()
min_c
    
    
Sum = (max_c +min_c)
Sum


# <h2 id="op">Numpy Array Operations</h2>
# 
# You could use arithmetic operators directly between NumPy arrays
# 

# <h3 id="add">Array Addition</h3>
# 
# 

# Consider the numpy array <code>u</code>:
# 

# In[41]:


u = np.array([1, 0])
u


# Consider the numpy array <code>v</code>:
# 

# In[42]:


v = np.array([0, 1])
v


# We can add the two arrays and assign it to z:
# 

# In[43]:


# Numpy Array Addition

z = np.add(u, v)
z


# The operation is equivalent to vector addition:
# 

# In[44]:


# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

  


# In[45]:


# Plot numpy arrays

Plotvec1(u, z, v)


# ### Try it yourself
# 
# Perform addition operation on the given numpy array arr1 and arr2:
# 

# In[47]:


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# Enter your code here
arr3 = arr1+arr2
arr3


# ### Array Subtraction
# 

# Consider the numpy array a:
# 

# In[48]:


a = np.array([10, 20, 30])
a


# Consider the numpy array b:
# 

# In[49]:


b = np.array([5, 10, 15])
b


# We can subtract the two arrays and assign it to c:
# 

# In[50]:


c = np.subtract(a, b)

print(c)


# ### Try it yourself
# 
# Perform subtraction operation on the given numpy array arr1 and arr2:
# 

# In[51]:


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# Enter your code here
arr3 = arr1-arr2
arr3


# <h3 id="multi">Array Multiplication</h3>
# 

# Consider the vector numpy array <code>y</code>:
# 

# In[52]:


# Create a numpy array

x = np.array([1, 2])
x


# In[53]:


# Create a numpy array

y = np.array([2, 1])
y


# We can multiply every element in the array by 2:
# 

# In[54]:


# Numpy Array Multiplication

z = np.multiply(x, y)
z


# This is equivalent to multiplying a vector by a scaler:
# 

# ### Try it yourself
# 
# Perform multiply operation on the given numpy array arr1 and arr2:
# 

# In[55]:


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])

# Enter your code here
arr3 = np.multiply(arr1, arr2)
arr3


# ### Array Division
# 

# Consider the vector numpy array a:
# 

# In[56]:


a = np.array([10, 20, 30])
a


# Consider the vector numpy array b:
# 

# In[57]:


b = np.array([2, 10, 5])
b


# We can divide the two arrays and assign it to c:
# 

# In[58]:


c = np.divide(a, b)
c


# ### Try it yourself
# 
# Perform division operation on the given numpy array arr1 and arr2:
# 

# In[59]:


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

# Enter your code here
arr3 = np.divide(arr1, arr2)
arr3


# <h3 id="dot">Dot Product</h3>
# 

# The dot product of the two numpy arrays <code>u</code> and <code>v</code> is given by:
# 

# In[60]:


X = np.array([1, 2])
Y = np.array([3, 2])


# In[61]:


# Calculate the dot product

np.dot(X, Y)


# In[62]:


#Elements of X
print(X[0])
print(X[1])


# In[63]:


#Elements of Y
print(Y[0])
print(Y[1])


# We are performing the dot product which is shown as below
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/dot1.png">
# 

# ### Try it yourself
# 
# Perform dot operation on the given numpy array ar1 and ar2:
# 

# In[64]:


arr1 = np.array([3, 5])
arr2 = np.array([2, 4])

# Enter your code here
arr3 = np.dot(arr1, arr2)
arr3


# <h3 id="cons">Adding Constant to a Numpy Array</h3>
# 

# Consider the following array:
# 

# In[65]:


# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u


# Adding the constant 1 to each element in the array:
# 

# In[66]:


# Add the constant to array

u + 1


# The process is summarised in the following animation:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/NumOneAdd.gif" width="500">
# 

# ### Try it yourself
# 
# Add Constant 5 to the given numpy array ar:
# 

# In[68]:


arr = np.array([1, 2, 3, -1]) 

# Enter your code here
arr+5


# <hr>
# 

# <h2 id="math">Mathematical Functions</h2>
# 

# We can access the value of <code>pi</code> in numpy as follows :
# 

# In[69]:


# The value of pi

np.pi


# We can create the following numpy array in Radians:
# 

# In[70]:


# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])


# We can apply the function <code>sin</code> to the array <code>x</code> and assign the values to the array <code>y</code>; this applies the sine function to each element in the array:
# 

# In[71]:


# Calculate the sin of each elements

y = np.sin(x)
y


# <hr>
# 

# <h2 id="lin">Linspace</h2>
# 

# A useful function for plotting mathematical functions is <code>linspace</code>.   Linspace returns evenly spaced numbers over a specified interval. 
# 
#  **numpy.linspace(start, stop, num = int value)**
#  
# start  :  start of interval range
# 
# stop   :  end of interval range
# 
# num    :  Number of samples to generate.
# 

# In[72]:


# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)


# If we change the parameter <code>num</code> to 9, we get 9 evenly spaced numbers over the interval from -2 to 2:
# 

# In[73]:


# Make a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)


# We can use the function <code>linspace</code> to generate 100 evenly spaced samples from the interval 0 to 2π:
# 

# In[74]:


# Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)


# We can apply the sine function to each element in the array <code>x</code> and assign it to the array <code>y</code>:
# 

# In[75]:


# Calculate the sine of x list

y = np.sin(x)


# In[76]:


# Plot the result

plt.plot(x, y)


# ### Try it yourself
# 
#  Make a numpy array within [5, 4] and 6 elements
# 

# In[77]:


# Enter your code here
np.linspace(5, 4, num=6)


# <hr>
# 

# ### Iterating 1-D Arrays
# 
# Iterating means going through elements one by one.
# 
# If we iterate on a 1-D array it will go through each element one by one.
# 

# If we execute the numpy array, we get in the array format
# 

# In[78]:


arr1 = np.array([1, 2, 3])
print(arr1)


# But if you want to result in the form of the list, then you can use for loop:
# 

# In[79]:


for x in arr1:
  print(x)


# <h2 id="quiz">Quiz on 1D Numpy Array</h2>
# 

# Implement the following vector subtraction in numpy: u-v
# 

# In[83]:


# Write your code below and press Shift+Enter to execute

u = np.array([1, 0])
v = np.array([0, 1])
f = np.subtract(u, v)
f


# <hr>
# 

# Multiply the numpy array z with -2:
# 

# In[85]:


# Write your code below and press Shift+Enter to execute

z = np.array([2, 4])
a = np.multiply(z, -2)
a


# <hr>
# 

# Consider the list <code>\[1, 2, 3, 4, 5]</code> and <code>\[1, 0, 1, 0, 1]</code>. Cast both lists to a numpy array then multiply them together:
# 

# In[86]:


# Write your code below and press Shift+Enter to execute
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
a * b


# <hr>
# 

# In[87]:


# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    
    


# Convert the list <code>\[-1, 1]</code> and <code>\[1, 1]</code> to numpy arrays <code>a</code> and <code>b</code>. Then, plot the arrays as vectors using the fuction <code>Plotvec2</code> and find their dot product:
# 

# In[88]:


# Write your code below and press Shift+Enter to execute
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))


# <hr>
# 

# Convert the list <code>\[1, 0]</code> and <code>\[0, 1]</code> to numpy arrays <code>a</code> and <code>b</code>. Then, plot the arrays as vectors using the function <code>Plotvec2</code> and find their dot product:
# 

# In[89]:


# Write your code below and press Shift+Enter to execute
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))


# <hr>
# 

# Convert the list <code>\[1, 1]</code> and <code>\[0, 1]</code> to numpy arrays <code>a</code> and <code>b</code>. Then plot the arrays as vectors using the fuction <code>Plotvec2</code> and find their dot product:
# 

# In[90]:


# Write your code below and press Shift+Enter to execute
a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))


# <hr>
# 

# Why are the results of the dot product for <code>\[-1, 1]</code> and <code>\[1, 1]</code> and the dot product for <code>\[1, 0]</code> and <code>\[0, 1]</code> zero, but not zero for the dot product for <code>\[1, 1]</code> and <code>\[0, 1]</code>? <p><i>Hint: Study the corresponding figures, pay attention to the direction the arrows are pointing to.</i></p>
# 

# In[92]:


# Write your code below and press Shift+Enter to execute
The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero. 


# Convert the list <code>\[1, 2, 3]</code> and <code>\[8, 9, 10]</code> to numpy arrays <code>arr1</code> and <code>arr2</code>. Then perform <code>Addition</code> , <code>Subtraction</code> , <code>Multiplication</code> , <code>Division</code> and <code>Dot Operation</code> on the <code>arr1</code> and <code>arr2</code>.
# 
# 

# In[93]:


# Write your code below and press Shift+Enter to execute
arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
arr3

arr4 = np.subtract(arr1, arr2)
arr4

arr5 = np.multiply(arr1, arr2)
arr5


arr6 = np.divide(arr1, arr2)
arr6

arr7 = np.dot(arr1, arr2)
arr7


# Convert the list <code>\[1, 2, 3, 4, 5]</code> and <code>\[6, 7, 8, 9, 10]</code> to numpy arrays <code>arr1</code> and <code>arr2</code>. Then find the even and odd numbers from <code>arr1</code> and <code>arr2</code>.
# 

# In[94]:


# Write your code below and press Shift+Enter to execute

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

#Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1",even_arr1)
    
#Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1=arr1[0:5:2]
print("odd for array1",odd_arr1)

#Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2",even_arr2)
    
    
#Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>
# 

# In[ ]:




