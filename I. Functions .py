#!/usr/bin/env python
# coding: utf-8

# # Functions in Python
# 
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Understand functions and variables
# *   Work with functions and variables
# 

# <h2 id="func">Functions</h2>
# 

# A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.
# 
# There are two types of functions :
# 
# *   <b>Pre-defined functions</b>
# *   <b>User defined functions</b>
# 

# <h3 id="content">What is a Function?</h3>
# 

# You can define functions to provide the required functionality. Here are simple rules to define a function in Python:
# 
# *   Functions blocks begin <code>def</code> followed by the function <code>name</code> and parentheses <code>()</code>.
# *   There are input parameters or arguments that should be placed within these parentheses.
# *   You can also define parameters inside these parentheses.
# *   There is a body within every function that starts with a colon (<code>:</code>) and is indented.
# *   You can also place documentation before the body.
# *   The statement <code>return</code> exits a function, optionally passing back a value.
# 
# An example of a function that adds on to the parameter <code>a</code> prints and returns the output as <code>b</code>:
# 

# In[3]:


# First function example: Add 1 to a and store as b

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)


# The figure below illustrates the terminology:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/FuncsDefinition.png" width="500"> 
# 

# We can obtain help about a function :
# 

# In[4]:


# Get a help on add function

help(add)


# We can call the function:
# 

# In[5]:


# Call the function add()

add(1)


# If we call the function with a new input we get a new result:
# 

# In[6]:


# Call the function add()

add(2)


# We can create different functions. For example, we can create a function that multiplies two numbers. The numbers will be represented by the variables <code>a</code> and <code>b</code>:
# 

# In[7]:


# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)


# The same function can be used for different data types. For example, we can multiply two integers:
# 

# In[8]:


# Use mult() multiply two integers

Mult(2, 3)


# Note how the function terminates at the <code> return </code> statement, while passing back a value. This value can be further assigned to a different variable as desired.
# 
# <hr>
# The same function can be used for different data types. For example, we can multiply two integers:
# 

# Two Floats:
# 

# In[9]:


# Use mult() multiply two floats

Mult(10.0, 3.14)


# We can even replicate a string by multiplying with an integer:
# 

# In[10]:


# Use mult() multiply two different type values together

Mult(2, "Michael Jackson ")


# <h3 id="var">Variables</h3>
# 

# The input to a function is called a formal parameter.
# 
# A variable that is declared inside a function is called a  local variable. The parameter only exists within the function (i.e. the point where the function starts and stops).
# 
# A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program. We will discuss more about global variables at the end of the lab.
# 

# In[11]:


# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)


# The labels are displayed in the figure:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/FuncsVar.png" width="500">
# 

# We can call the function  with an input of <b>3</b>:
# 

# In[12]:


# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y


# We can call the function  with an input of <b>2</b> in a different manner:
# 

# In[13]:


# Directly enter a number as parameter

square(2)


# If there is no <code>return</code> statement, the function returns <code>None</code>. The following two functions are equivalent:
# 

# In[14]:


# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)


# In[15]:


# See the output

MJ()


# In[16]:


# See the output

MJ1()


# Printing the function after a call reveals a **None** is the default return statement:
# 

# In[17]:


# See what functions returns are

print(MJ())
print(MJ1())


# Create a function <code>con</code> that  concatenates two strings using the addition operation:
# 

# In[18]:


# Define the function for combining strings

def con(a, b):
    return(a + b)


# In[19]:


# Test on the con() function

con("This ", "is")


# <h3 id="simple">Functions Make Things Simple</h3>
# 

# Consider the two lines of code in <b>Block 1</b> and <b>Block 2</b>: the procedure for each block is identical. The only thing that is different is the variable names and values.
# 

# <h4>Block 1:</h4>
# 

# In[20]:


# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   


# <h4>Block 2:</h4>
# 

# In[21]:


# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   


# We can replace the lines of code with a function. A function combines many instructions into a single line of code. Once a function is defined, it can be used repeatedly. You can invoke the same function many times in your program. You can save your function and use it in another program or use someone else’s function. The lines of code in code <b>Block 1</b> and code <b>Block 2</b> can be replaced by the following function:
# 

# In[22]:


# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


# This function takes two inputs, a and b, then applies several operations to return c.
# We simply define the function, replace the instructions with the function, and input the new values of <code>a1</code>, <code>b1</code> and <code>a2</code>, <code>b2</code> as inputs. The entire process is demonstrated in the figure:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/FuncsPros.gif" width="850">
# 

# Code **Blocks 1** and **Block 2** can now be replaced with code **Block 3** and code **Block 4**.
# 

# <h4>Block 3:</h4>
# 

# In[23]:


a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1


# <h4>Block 4:</h4>
# 

# In[24]:


a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2


# <hr>
# 

# <h2 id="pre">Pre-defined functions</h2>
# 

# There are many pre-defined functions in Python, so let's start with the simple ones.
# 

# The <code>print()</code> function:
# 

# In[25]:


# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)


# The <code>sum()</code> function adds all the  elements in a list or tuple:
# 

# In[26]:


# Use sum() to add every element in a list or tuple together

sum(album_ratings)


# The <code>len()</code> function returns the length of a list or tuple:
# 

# In[27]:


# Show the length of the list or tuple

len(album_ratings)


# <h2 id="if">Using <code>if</code>/<code>else</code> Statements and Loops in Functions</h2>
# 

# The <code>return()</code> function is particularly useful if you have any IF statements in the function, when you want your output to be dependent on some condition:
# 

# In[28]:


# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# We can use a loop in a function. For example, we can <code>print</code> out each element in a list:
# 

# In[29]:


# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)


# In[30]:


# Implement the printlist function

PrintList(['1', 1, 'the man', "abc"])


# <h2 id="if">String comparison in Functions</h2>
# 

# The relational operators compare the Unicode values of the characters of the strings from the zeroth index till the end of the string. It then returns a boolean value according to the operator used.
# 

# In[31]:


#Compare Two Strings Directly using in operator
# add string
string= "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")


# This program uses a user-defined function named compareStrings() to compare two strings. 
# 
# This function receives both strings as its argument and returns 1 if both strings are equal using == operator
# 

# In[32]:


#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")


# **Count the Frequency of Words Appearing in a String Using a Dictionary.** 
# 
# Find the count of occurence of any word in our string using python. This is what we are going to do in this section, count the number of word in a given string and print it.
# 
# Lets suppose we have a ‘string’ and the ‘word’ and we need to find the count of occurence of this word in our string using python. This is what we are going to do in this section, count the number of word in a given string and print it. 
# 
# The first thing, we will do is define a function and and then create a list that will be empty initially.
# 
# Next, we will add a code to convert the string to a list. Python string has a split() method. It takes a string and some separator to return a list.
# 
# Now we will declare an empty dictionary.
# 
# Next we will add code using for loop to iterate the words and value will will count the frequency of each words in the string and store them to the dictionary.
# 
# Finally we will print the dictionary.
# 

# In[33]:


# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")


# <hr>
# 

# <h2 id="default">Setting default argument values in your custom functions</h2>
# 

# You can set a default value for arguments in your function. For example, in the <code>isGoodRating()</code> function, what if we wanted to create a threshold for what we consider to be a good rating? Perhaps by default, we should have a default rating of 4:
# 

# In[34]:


# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)


# In[35]:


# Test the value with default value and with input

isGoodRating()
isGoodRating(10)


# <hr>
# 

# <h2 id="global">Global variables</h2>
# 

# So far, we've been creating variables within functions, but we have not discussed variables outside the function. These are called global variables. <br>
# Let's try to see what <code>printer1</code> returns:
# 

# In[36]:


# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 


# <b>We got a Name Error:  <code>name 'internal_var' is not defined</code>. Why?</b>
# 
# It's because all the variables we create in the function is a <b>local variable</b>, meaning that the variable assignment does not persist outside the function.
# 
# But there is a way to create <b>global variables</b> from within a function as follows:
# 

# In[37]:


artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)


# <h2 id="scope">Scope of a Variable</h2>
# 

# The scope of a variable is the part of that program where that variable is accessible. Variables that are declared outside of all function definitions, such as the <code>myFavouriteBand</code> variable in the code shown here, are accessible from anywhere within the program. As a result, such variables are said to have global scope, and are known as global variables. <code>myFavouriteBand</code> is a global variable, so it is accessible from within the <code>getBandRating</code> function, and we can use it to determine a band's rating. We can also use it outside of the function, such as when we pass it to the print function to display it:
# 

# In[38]:


# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


# Take a look at this modified version of our code. Now the <code>myFavouriteBand</code> variable is defined within the <code>getBandRating</code> function. A variable that is defined within a function is said to be a local variable of that function. That means that it is only accessible from within the function in which it is defined. Our <code>getBandRating</code> function will still work, because <code>myFavouriteBand</code> is still defined within the function. However, we can no longer print <code>myFavouriteBand</code> outside our function, because it is a local variable of our <code>getBandRating</code> function; it is only defined within the <code>getBandRating</code> function:
# 

# In[39]:


# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)


# Finally, take a look at this example. We now have two <code>myFavouriteBand</code> variable definitions. The first one of these has a global scope, and the second of them is a local variable within the <code>getBandRating</code> function. Within the <code>getBandRating</code> function, the local variable takes precedence. **Deep Purple** will receive a rating of 10.0 when passed to the <code>getBandRating</code> function. However, outside of the <code>getBandRating</code> function, the <code>getBandRating</code> s local variable is not defined, so the <code>myFavouriteBand</code> variable we print is the global variable, which has a value of **AC/DC**:
# 

# In[40]:


# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)


# <hr>
# <h2 id ="collec"> Collections and Functions</h2>
# 

# When the number of arguments  are unknown for a function, They can all be packed into a tuple as shown:
# 

# In[41]:


def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


# Similarly, The arguments can also be packed into a dictionary as shown:
# 

# In[42]:


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    


# Functions can be incredibly powerful and versatile. They can accept (and return) data types, objects and even other functions as arguements. Consider the example below:
# 

# In[43]:


def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList
    


# Note how the changes made to the list are not limited to the functions scope. This occurs as it is the lists **reference** that is passed to the function - Any changes made are on the orignal instance of the list. Therefore, one should be cautious when passing mutable objects into functions.
# 
# <hr>
# 

# <h2>Quiz on Functions</h2>
# 

# Come up with a function that divides the first input by the second input:
# 

# In[44]:


# Write your code below and press Shift+Enter to execute
def div(a, b):
    return(a/b)


# <hr>
# 

# Use the function <code>con</code> for the following question.
# 

# In[45]:


# Use the con function for the following question

def con(a, b):
    return(a + b)


# Can the <code>con</code> function we defined before be used to add two integers or strings?
# 

# In[46]:


# Write your code below and press Shift+Enter to execute
con(2, 2)


# <hr>
# 

# Can the <code>con</code> function we defined before be used to concatenate lists or tuples?
# 

# In[47]:


# Write your code below and press Shift+Enter to execute
con(['a', 1], ['b', 1])


# Write a function code to find total count of word `little` in the given string: 
# `"Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"**`
# 

# In[48]:


# Write your code below and press Shift+Enter to execute
def freq(string,passedkey):

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    #step5: Print the dictionary
    print("Total Count:",Dict)

#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")
    


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>
# 
