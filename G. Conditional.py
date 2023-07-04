#!/usr/bin/env python
# coding: utf-8

# # Conditions in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * work with condition statements in Python, including operators, and branching.

# <h2 id="cond">Condition Statements</h2>

# <h3 id="comp">Comparison Operators</h3>
# 

# Comparison operations compare some value or operand and based on a condition, produce a Boolean. When comparing two values you can use these operators:
# 
# <ul>
#     <li>equal: <b>==</b></li>
#     <li>not equal: <b>!=</b></li>
#     <li>greater than: <b>></b></li>
#     <li>less than: <b>&lt;</b></li>
#     <li>greater than or equal to: <b>>=</b></li>
#     <li>less than or equal to: <b>&lt;=</b></li>
# </ul>
# 

# Let's assign <code>a</code> a value of 5. Use the equality operator denoted with two equal <b>==</b> signs to determine if two values are equal. The case below compares the variable <code>a</code> with 6.
# 

# In[3]:


# Condition Equal

a = 5
a == 6


# The result is <b>False</b>, as 5 does not equal to 6.

# Consider the following equality comparison operator: <code>i > 5</code>. If the value of the left operand, in this case the variable <b>i</b>, is greater than the value of the right operand, in this case 5, then the statement is <b>True</b>. Otherwise, the statement is <b>False</b>.  If <b>i</b> is equal to 6, because 6 is larger than 5, the output is <b>True</b>.
# 

# In[4]:


# Greater than Sign

i = 6
i > 5


# The inequality test uses an exclamation mark preceding the equal sign, if two operands are not equal then the condition becomes **True**.  For example, the following condition will produce **True** as long as the value of <code>i</code> is not equal to 6:

# In[5]:


# Inequality Sign

i = 2
i != 6


# When <code>i</code> equals 6 the inequality expression produces <b>False</b>. 

# In[6]:


# Inequality Sign

i = 6
i != 6


# In[7]:


# Use Equality sign to compare the strings

"ACDC" == "Michael Jackson"


# In[8]:


# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"


# In[9]:


# Compare characters

'B' > 'A'


# In[10]:


# Compare characters

'BA' > 'AB'


# <h3 id="branch">Branching</h3>

#  Branching allows us to run different statements for different inputs. It is helpful to think of an **if statement** as a locked room, if the statement is **True** we can enter the room and your program will run some predefined tasks, but if the statement is **False** the program will ignore the task.

# In[11]:


# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/CondsIf.gif" width="650">

# The <code>else</code> statement runs a block of code if none of the conditions are **True** before this <code>else</code> statement. Let's use the ACDC concert analogy again. If the user is 17 they cannot go to the ACDC concert,  but they can go to the Meatloaf concert.
# The syntax of the <code>else</code> statement is similar as the syntax of the <code>if</code> statement, as <code>else :</code>. Notice that, there is no condition statement for <code>else</code>.
# Try changing the values of <code>age</code> to see what happens:  

# In[12]:


# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/CondsElse.gif" width="650">

# The <code>elif</code> statement, short for else if, allows us to check additional conditions if the condition statements before it are <b>False</b>. If the condition for the <code>elif</code> statement is <b>True</b>, the alternate expressions will be run. Consider the concert example, where if the individual is 18 they will go to the Pink Floyd concert instead of attending the ACDC or Meat-loaf concert. A person that is 18 years of age enters the area, and as they are not older than 18 they can not see ACDC, but since they are 18 years of age, they attend  Pink Floyd. After seeing Pink Floyd, they move on. The syntax of the <code>elif</code> statement is similar in that we merely change the <code>if</code> in the <code>if</code> statement to <code>elif</code>.
# 

# In[13]:


# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/CondsElif.gif" width="650">

# In[14]:


# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/CondsLogicMap.png" width="650">

# In[15]:


# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')


# <h3 id="logic">Logical operators</h3>

# Sometimes you want to check more than one condition at once. For example, you might want to check if one condition and another condition are both **True**. Logical operators allow you to combine or modify conditions.
# <ul>
#     <li><code>and</code></li>
#     <li><code>or</code></li>
#     <li><code>not</code></li>
# </ul>
# 
# These operators are summarized for two variables using the following truth tables:  

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/CondsTable.png" width="650">
# 

# The <code>and</code> statement is only **True** when both conditions are true. The <code>or</code> statement is True if one condition, or both are **True**. The <code>not</code> statement outputs the opposite truth value.

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/CondsEgOne.png" width="650">

# In[16]:


# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


# In[17]:


# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# In[18]:


# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")


# <h2 id="quiz">Practise Exercises</h2>

# ##### 1. There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.

# In[19]:


Annie=1996
Jane=1999
if Annie%4==0:
    print("Annie was born in a leap year")
elif Jane%4==0:
    print("Jane was born in a leap year")
else:
    print("None of them were born in a leap year")


# ##### 2. In a school canteen, children under the age of 9 are only given milk porridge for breakfast. Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger. The canteen master asks the age of the student and gives them breakfast accordingly. Sam's age is 10. Use if-else statement to determine what the canteen master will offer to him.

# In[21]:


age = 15
if age <=9:
    print ("You will get a bowl of porridge!")
elif age>=10 and age<=14:
    print ("You will get a sandwich!")
elif age>=15 and age<=17:
    print("You will get a burger!")


# <hr>
# <h3>Congratulations, you have completed your lab on Conditions and Branching<h3>
# <hr>

# In[ ]:




