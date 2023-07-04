#!/usr/bin/env python
# coding: utf-8

# <h2><strong>Say "Hello" to the world in Python</strong></h2>

# When learning a new programming language, it is customary to start with an "hello world" example. As simple as it is, this one line of code will ensure that we know how to print a string in output and how to execute code within cells in a notebook.

# In[7]:


# Try your first Python output

print('Hello, Python!')


# <h3 id="version">What version of Python are we using?</h3>

# <p>
#     There are two popular versions of the Python programming language in use today: Python 2 and Python 3. The Python community has decided to move on from Python 2 to Python 3, and many popular libraries have announced that they will no longer support Python 2.
# </p>
# <p>
#     Since Python 3 is the future, in this course we will be using it exclusively. How do we know that our notebook is executed by a Python 3 runtime? We can look in the top-right hand corner of this notebook and see "Python 3".
# </p>
# <p>
#     We can also ask Python directly and obtain a detailed answer. Try executing the following code:
# </p>

# In[8]:


# Check the Python Version

import sys
print(sys.version)


# <h3 id="comments">Writing comments in Python</h3>

# <p>
#     In addition to writing code, note that it's always a good idea to add comments to your code. It will help others to understand what you were trying to accomplish (the reason why you wrote a given snippet of code). Not only does this help <strong>other people</strong> understand your code, it can also serve as a reminder <strong>to you</strong> when you come back to it weeks or months later.</p>
# 
# <p>
#     To write comments in Python, use the number symbol <code>#</code> before writing your comment. When you run your code, Python will ignore everything past the <code>#</code> on a given line.
# </p>

# In[10]:


# Practice on writing comments

print('Hello, Python!') # This line prints a string
# print('Hi')


# <h3 id="errors">Errors in Python</h3>

# <p>Everyone makes mistakes. For many types of mistakes, Python will tell you that you have made a mistake by giving you an error message. It is important to read error messages carefully to really understand where you made a mistake and how you may go about correcting it.</p>
# <p>For example, if you spell <code>print</code> as <code>frint</code>, Python will display an error message. Give it a try:</p>
# 

# In[12]:


# Print string as error message

frint("Hello, Python!")


# <p>The error message tells you: 
# <ol>
#     <li>where the error occurred (more useful in large notebook cells or scripts), and</li> 
#     <li>what kind of error it was (NameError)</li> 
# </ol>
# <p>Here, Python attempted to run the function <code>frint</code>, but could not determine what <code>frint</code> is since it's not a built-in function and it has not been previously defined by us either.</p>
# 

# <p>
#     //"You'll notice that if we make a different type of mistake, by forgetting to close the string, we'll obtain a different error (i.e., a <code>SyntaxError</code>). Try it below:"//
# </p>
# 

# In[13]:


# Try to see built-in error message

print("Hello, Python!)


# <h3 id="python_error">Does Python know about your error before it runs your code?</h3>

# Python is what is called an <em>interpreted language</em>. Compiled languages examine your entire program at compile time, and are able to warn you about a whole class of errors prior to execution. In contrast, Python interprets your script line by line as it executes it. Python will stop executing the entire program when it encounters an error (unless the error is expected and handled by the programmer, a more advanced subject that we'll cover later on in this course).
# 

# In[14]:


# Print string and error to see the running order

print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")


# <h3 id="exercise">Exercise: Your First Program</h3>

# Generations of programmers have started their coding careers by simply printing "Hello, world!". You will be following in their footsteps.
# 
# In the code cell below, use the print() function to print out the phrase: Hello, world!

# In[15]:


# Write your code below.

print("Hello, world!")


# <p>Now, let's enhance your code with a comment. In the code cell below, print out the phrase: <code>Hello, world!</code> and comment it with the phrase <code>Print the traditional hello world</code> all in one line of code.</p>
# 

# In[16]:


# Write your code below.

print("Hello world!") #print the traditional hello world


# <h2 id="types_objects" align="center">Types of objects in Python</h2>

# <p>Python is an object-oriented language. There are many different types of objects in Python. Let's start with the most common object types: <i>strings</i>, <i>integers</i> and <i>floats</i>. Anytime you write words (text) in Python, you're using <i>character strings</i> (strings for short). The most common numbers, on the other hand, are <i>integers</i> (e.g. -1, 0, 100) and <i>floats</i>, which represent real numbers (e.g. 3.14, -42.0).</p>

# <a align="center">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/TypesObjects.png" width="600">
# </a>

# In[18]:


# Integer

11


# In[19]:


# Float

2.14


# In[20]:


# String

"Hello, Python 101!"


# <p>You can get Python to tell you the type of an expression by using the built-in <code>type()</code> function. You'll notice that Python refers to integers as <code>int</code>, floats as <code>float</code>, and character strings as <code>str</code>.</p>
# 

# In[21]:


# Type of 12

type(12)


# In[22]:


# Type of 2.14

type(2.14)


# In[23]:


# Type of "Hello, Python 101!"

type("Hello, Python 101!")


# <p>In the code cell below, use the <code>type()</code> function to check the object type of <code>12.0</code>.

# In[24]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(12.0)


# <h3 id="int">Integers</h3>

# <p>Here are some examples of integers. Integers can be negative or positive numbers:</p>

# <a align="center">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/TypesInt.png" width="600">
# </a>

# In[25]:


# Print the type of -1

type(-1)


# In[26]:


# Print the type of 4

type(4)


# In[27]:


# Print the type of 0

type(0)


# <h3 id="float">Floats</h3> 

# <p>Floats represent real numbers; they are a subset of all integers. but also include "numbers with decimals". There are some limitations when it comes to machines representing real numbers, but floating point numbers are a good representation in most cases. You can learn more about the specifics of floats for your runtime environment, by checking the value of <code>sys.float_info</code>. This will also tell you what's the largest and smallest number that can be represented with them.</p>
# 
# <p>Once again, can test some examples with the <code>type()</code> function:
# 

# In[28]:


# Print the type of 1.0

type(1.0) # Notice that 1 is an int, and 1.0 is a float


# In[29]:


# Print the type of 0.5

type(0.5)


# In[30]:


# Print the type of 0.56

type(0.56)


# In[31]:


# System settings about float type

sys.float_info


# <h3 id="convert">Converting from one object type to a different object type</h3>

# <p>You can change the type of the object in Python; this is called typecasting. For example, you can convert an <i>integer</i> into a <i>float</i> (e.g. 2 to 2.0).</p>
# <p>Let's try it:</p>
# 

# In[32]:


# Verify that this is an integer

type(2)


# <h4>Converting integers to floats</h4>
# <p>Let's cast integer 2 to float:</p>

# In[33]:


# Convert 2 to a float

float(2)


# In[34]:


# Convert integer 2 to a float and check its type

type(float(2))


# <p>When we convert an integer into a float, we don't really change the value (i.e., the significand) of the number. However, if we cast a float into an integer, we could potentially lose some information. For example, if we cast the float 1.1 to integer we will get 1 and lose the decimal information (i.e., 0.1):</p>
# 

# In[35]:


# Casting 1.1 to integer will result in loss of information

int(1.1)


# <h4>Converting from strings to integers or floats</h4>

# <p>Sometimes, we can have a string that contains a number within it. If this is the case, we can cast that string that represents a number into an integer using <code>int()</code>:</p>
# 

# In[38]:


# Convert a string into an integer

int('1')


# <p>But if you try to do so with a string that is not a perfect match for a number, you'll get an error. Try the following:</p>
# 

# In[39]:


# Convert a string into an integer with error

int('1 or 2 people')


# <p>You can also convert strings containing floating point numbers into <i>float</i> objects:</p>

# In[40]:


# Convert the string "1.2" into a float

float('1.2')


# <h4>Converting numbers to strings</h4>

# <p>If we can convert strings to numbers, it is only natural to assume that we can convert numbers to strings, right?</p>

# In[42]:


# Convert an integer to a string

str(1)


# <h3 id="bool">Boolean data type</h3>

# <p><i>Boolean</i> is another important type in Python. An object of type <i>Boolean</i> can take on one of two values: <code>True</code> or <code>False</code>:</p>

# In[43]:


# Value true

True


# <p>Notice that the value <code>True</code> has an uppercase "T". The same is true for <code>False</code> (i.e. you must use the uppercase "F").</p>
# 

# In[44]:


# Value false

False


# <p>When you ask Python to display the type of a boolean object it will show <code>bool</code> which stands for <i>boolean</i>:</p> 
# 

# In[45]:


# Type of True

type(True)


# In[46]:


# Type of False

type(False)


# <p>We can cast boolean objects to other data types. If we cast a boolean with a value of <code>True</code> to an integer or float we will get a one. If we cast a boolean with a value of <code>False</code> to an integer or float we will get a zero. Similarly, if we cast a 1 to a Boolean, you get a <code>True</code>. And if we cast a 0 to a Boolean we will get a <code>False</code>. Let's give it a try:</p> 
# 

# In[47]:


# Convert True to int

int(True)


# In[48]:


# Convert 1 to boolean

bool(1)


# In[49]:


# Convert 0 to boolean

bool(0)


# In[50]:


# Convert True to float

float(True)


# <h3 id="exer_type">Exercise: Types</h3>

# <p>What is the data type of the result of: <code>6 / 2</code>?</p>
# 

# In[51]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6/2)


# <p>What is the type of the result of: <code>6 // 2</code>? (Note the double slash <code>//</code>.)</p>

# In[53]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6//2)


# <hr>

# <h2 id="expressions">Expression and Variables</h2>

# <h3 id="exp">Expressions</h3>

# <p>Expressions in Python can include operations among compatible types (e.g., integers and floats). For example, basic arithmetic operations like adding multiple numbers:</p>
# 

# In[54]:


# Addition operation expression

43 + 60 + 16 + 41


# In[55]:


# Subtraction operation expression

50 - 60


# In[56]:


# Multiplication operation expression

5 * 5


# In[57]:


# Division operation expression

25 / 5


# In[58]:


# Division operation expression

25 / 6


# <p>we can use the double slash for integer division, where the result is rounded down to the nearest integer

# In[59]:


# Integer division operation expression

25 // 5


# In[60]:


# Integer division operation expression

25 // 6


# <h3 id="exer_exp">Exercise: Expression</h3>
# 

# <p>Let's write an expression that calculates how many hours there are in 160 minutes:

# In[63]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
160/60


# <p>Python follows well accepted mathematical conventions when evaluating mathematical expressions. In the following example, Python adds 30 to the result of the multiplication (i.e., 120).
# 

# In[64]:


# Mathematical expression

30 + 2 * 60


# In[65]:


# Mathematical expression

(30 + 2) * 60


# <h3 id="var">Variables</h3>
# 

# <p>Just like with most programming languages, we can store values in <i>variables</i>, so we can use them later on. For example:</p>

# In[67]:


# Store value into variable

x = 43 + 60 + 16 + 41


# In[68]:


# Print out the value in variable

x


# In[69]:


# Use another variable to store the result of the operation between variable and value

y = x / 60
y


# In[70]:


# Overwrite variable with new value

x = x / 60
x


# In[71]:


# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min


# In[72]:


# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours 
total_hours


# In[73]:


# Complicate expression

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours


# <p>If you'd rather have total hours as an integer, you can of course replace the floating point division with integer division (i.e., <code>//</code>).</p>
# 

# <h3 id="exer_exp_var">Exercise: Expression and Variables in Python</h3>
# 

# <p>What is the value of <code>x</code> ?<br> where, <code>x = 3 + 2 * 2</code></p>
# 

# In[74]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
x=3+2*2
x


# <p>What is the value of <code>y</code> where <code>y = (3 + 2) * 2</code>?</p>
# 

# In[75]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
y=(3+2)*2
y


# <p>What is the value of <code>z</code> where <code>z = x + y</code>?</p>
# 

# In[76]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
z=x+y
z


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python.
# <hr>
# 
