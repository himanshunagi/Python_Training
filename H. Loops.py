#!/usr/bin/env python
# coding: utf-8

# # Loops in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * work with the loop statements in Python, including for-loop and while-loop.

# <h1>Loops</h1>

# <h3 id="range">Range</h3>

# Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by <b>loops</b>. We will look at two types of loops, <code>for</code> loops and <code>while</code> loops.
# 
# Before we discuss loops lets discuss the <code>range</code> object. It is helpful to think of the range object as an ordered list. For now, let's look at the simplest case. If we would like to generate an object that contains elements ordered from 0 to 2 we simply use the following command:

# In[1]:


# Use the range

range(3)


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/range.PNG" width="300">

# <h3 id="for">What is <code>for</code> loop?</h3>

# The <code>for</code> loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.    
# Let's try to use a <code>for</code> loop to print all the years presented in the list <code>dates</code>:

# In[2]:


# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])   


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/LoopsForRange.gif" width="800">

# In[3]:


# Example of for loop

for i in range(0, 8):
    print(i)


# In[4]:


# Exmaple of for loop, loop through list

for year in dates:  
    print(year)  


# For each iteration, the value of the variable <code>year</code> behaves like the value of <code>dates[i]</code> in the  first example:

# In[5]:


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])


# In[6]:


# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# <h3 id="while">What is <code>while</code> loop?</h3>

# As you can see, the <code>for</code> loop is used for a controlled flow of repetition. However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The <code>while</code> loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a **False** boolean value.

# #### Here's how a while loop works:
# 
# 1. First, you specify a condition that the loop will check before each iteration (repetition) of the code block.
# 2. If the condition is initially true, the code block is executed.
# 3. After executing the code block, the condition is checked again.
# 4. If the condition is still true, the code block is executed again.
# 5. Steps 3 and 4 repeat until the condition becomes false.
# 6. Once the condition becomes false, the loop stops, and the program continues with the next line of code after the loop.

# In[7]:


count = 1
while count <= 5:
    print(count)
    count += 1


# In this example, the condition **count <= 5** is checked before each iteration. As long as count is less than or equal to 5, the code block inside the loop is executed. After each iteration, the value of count is incremented by 1 using count += 1. Once count reaches 6, the condition becomes false, and the loop stops.
# 

# In[8]:


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/LoopsWhile.gif" width="650">

# 
# **The main difference between a while loop and a for loop in Python is how they control the flow of execution and handle iterations.**

# ### Key point of While Loop:
# 
# 1. A while loop repeatedly executes a block of code as long as a given condition is true.
# 2. It does not have a fixed number of iterations but continues executing until the condition becomes false.
# 3. The condition is checked before each iteration, and if it's false initially, the code block is skipped entirely.
# 4. The condition is typically based on a variable or expression that can change during the execution of the loop.
# 5. It provides more flexibility in terms of controlling the loop's execution based on dynamic conditions.
# 

# ### Key point of For Loop:
# 
# 1. A for loop iterates over a sequence (such as a list, string, or range) or any object that supports iteration.
# 2. It has a predefined number of iterations based on the length of the sequence or the number of items to iterate over.
# 3. It automatically handles the iteration and does not require maintaining a separate variable for tracking the iteration count.
# 4. It simplifies the code by encapsulating the iteration logic within the loop itself.
# 5. It is commonly used when you know the exact number of iterations or need to iterate over each item in a collection.

# <h2 id="quiz">Practise Exercises on Loops</h2>

# Write a <code>for</code> loop the prints out all the element between <b>-5</b> and <b>5</b> using the range function.

# In[9]:


for i in range(-4, 5):
    print(i)


# Print the elements of the following list:
# <code>Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']</code>
# Make sure you follow Python conventions.

# In[10]:


Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)


# Write a for loop that prints out the following list: <code>squares=['red', 'yellow', 'green', 'purple', 'blue']</code>

# In[13]:


squares=['red', 'yellow', 'green', 'purple', 'blue']
for squares in squares:
    print(squares)


# Write a while loop to display the values of the Rating of an album playlist stored in the list <code>PlayListRatings</code>. If the score is less than 6, exit the loop. The list <code>PlayListRatings</code> is given by: <code>PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]</code>

# In[17]:


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1 
    rating = PlayListRatings[i]   


# Write a while loop to copy the strings <code>'orange'</code> of the list <code>squares</code> to the list <code>new_squares</code>. Stop and exit the loop if the value on the list is not <code>'orange'</code>:

# In[18]:


squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)


# Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. Help him memorise both the tables by printing them using <code>for</code> loop.

# In[21]:


print("Multiplication table of 6:")
for i in range (10):
    print("6*",i,"=",6*i)
print("Multiplication table of 7:")
for i in range (10):
    print("7*",i,"=",7*i)


# The following is a list of animals in a National Zoo. 
# <code>Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]</code>
# 
# Your brother needs to write an essay on the animals whose names are made of 7 letters. Help him find those animals through a <code>while</code> loop and create a separate list of such animals.

# In[22]:


Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
New = []
i=0
while i<len(Animals):
    j=Animals[i]
    if(len(j)==7):
        New.append(j)
    i=i+1
print(New)


# <hr>
# 
# <h3>Congratulations, you have completed lab on loops<h3> 
# <hr>

# In[ ]:




