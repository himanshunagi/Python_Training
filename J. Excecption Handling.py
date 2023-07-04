#!/usr/bin/env python
# coding: utf-8

# # **Exception Handling**
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * Understand exceptions    
# * Handle the exceptions
# 

# ----
# 

# ## What is an Exception?
# 

# ### Definition
# 

# An exception is an error that occurs during the execution of code. This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code.
# 

# ### Examples
# 

# Run each piece of code and observe the exception raised
# 

# In[1]:


1/0


# <code>ZeroDivisionError</code> occurs when you try to divide by zero.
# 

# In[2]:


y = a + 5


# <code>NameError</code> -- in this case, it means that you tried to use the variable a when it was not defined.
# 

# In[3]:


a = [1, 2, 3]
a[10]


# <code>IndexError</code> -- in this case, it occured because you tried to access data from a list using an index that does not exist for this list.
# 

# There are many more exceptions that are built into Python, here is a list of them https://docs.python.org/3/library/exceptions.html
# 

# ## Exception Handling
# 

# ### Try Except
# 

# A <code>try except</code> will allow you to execute code that might raise an exception and in the case of any exception or a specific one we can handle or catch the exception and execute specific code. This will allow us to continue the execution of our program even if there is an exception.
# 
# Python tries to execute the code in the <code>try</code> block. In this case if there is any exception raised by the code in the <code>try</code> block, it will be caught and the code block in the <code>except</code> block will be executed. After that, the code that comes <em>after</em> the try except will be executed.
# 

# In[4]:


# potential code before try catch

try:
    # code to try to execute
except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception


# ### Try Except Example
# 

# In this example we are trying to divide a number given by the user, save the outcome in the variable <code>a</code>, and then we would like to print the result of the operation. When taking user input and dividing a number by it there are a couple of exceptions that can be raised. For example if we divide by zero. Try running the following block of code with <code>b</code> as a number. An exception will only be raised if <code>b</code> is zero.
# 

# In[6]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        


# ### Try Except Specific
# 

# A specific <code>try except</code> allows you to catch certain exceptions and also execute certain code depending on the exception. This is useful if you do not want to deal with some exceptions and the execution should halt. It can also help you find errors in your code that you might not be aware of. Furthermore, it can help you differentiate responses to different exceptions. In this case, the code after the try except might not run depending on the error.
# 

# <b>Do not run, just to illustrate:</b>
# 

# In[7]:


# potential code before try catch

try:
    # code to try to execute
except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types
    
# code that will execute if there is no exception or a one that we are handling


# In[8]:


# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
    
# code that will execute if there is no exception or a one that we are handling


# You can also have an empty <code>except</code> at the end to catch an unexpected exception:
# 

# <b>Do not run, just to illustrate:</b>
# 

# In[9]:


# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
    
# code that will execute if there is no exception or a one that we are handling


# ### Try Except Specific Example
# 

# This is the same example as above, but now we will add differentiated messages depending on the exception, letting the user know what is wrong with the input.
# 

# In[ ]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
        


# ### Try Except Else and Finally
# 

# <code>else</code> allows one to check if there was no exception when executing the try block. This is useful when we want to execute something only if there were no errors.
# 

# <b>do not run, just to illustrate</b>
# 

# In[ ]:


# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
    
# code that will execute if there is no exception or a one that we are handling


# <code>finally</code> allows us to always execute something even if there is an exception or not. This is usually used to signify the end of the try except.
# 

# In[ ]:


# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling


# ### Try Except Else and Finally Example
# 

# You might have noticed that even if there is an error the value of <code>a</code> is always printed. Let's use the <code>else</code> and print the value of <code>a</code> only if there is no error.
# 

# In[ ]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)


# Now lets let the user know that we are done processing their answer. Using the <code>finally</code>, let's add a print.
# 

# In[ ]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

