#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Work with classes and objects
# *   Identify and define attributes and methods

# <h2 id="intro">Introduction to Classes and Objects</h2>

# <h3>Creating a Class</h3>

# The first step in creating a class is giving it a name. In this notebook, we will create two classes: Circle and Rectangle. We need to determine all the data that make up that class, which we call <em>attributes</em>. Think about this step as creating a blue print that we will use to create objects. In figure 1 we see two classes, Circle and Rectangle. Each has their attributes, which are variables. The class Circle has the attribute radius and color, while the Rectangle class has the attribute height and width. Let’s use the visual examples of these shapes before we get to the code, as this will help you get accustomed to the vocabulary.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/ClassesClass.png" width="500">

# <h3 id="instance">Instances of a Class: Objects and Attributes</h3>

# An instance of an object is the realisation of a class, and in Figure 2 we see three instances of the class circle. We give each object a name: red circle, yellow circle, and green circle. Each object has different attributes, so let's focus on the color attribute for each object.

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/ClassesObj.png" width="500">

# The colour attribute for the red Circle is the colour red, for the green Circle object the colour attribute is green, and for the yellow Circle the colour attribute is yellow.

# <h3 id="method">Methods</h3>

# Methods give you a way to change or interact with the object; they are functions that interact with objects. For example, let’s say we would like to increase the radius of a circle by a specified amount. We can create a method called **add_radius(r)** that increases the radius by **r**. This is shown in figure 3, where after applying the method to the "orange circle object", the radius of the object increases accordingly. The “dot” notation means to apply the method to the object, which is essentially applying a function to the information in the object.

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/ClassesMethod.png" width="500"> 

# <i>Figure 3: Applying the method “add_radius” to the object orange circle object.</i>

# <hr>

# <h2 id="creating">Creating a Class</h2>

# In[1]:


# Import the library

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# The first step in creating your own class is to use the <code>class</code> keyword, then the name of the class as shown in Figure 4. In this course the class parent will always be object:

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/ClassesDefine.png" width="400">

# The next step is a special method called a constructor <code>\__init\_\_</code>, which is used to initialize the object. The inputs are data attributes. The term <code>self</code> contains all the attributes in the set. For example the <code>self.color</code> gives the value of the attribute color and <code>self.radius</code> will give you the radius of the object. We also have the method <code>add_radius()</code> with the parameter <code>r</code>, the method adds the value of <code>r</code> to the attribute radius. To access the radius we use the syntax <code>self.radius</code>. The labeled syntax is summarized in Figure 5:

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/ClassesCircle.png" width="600">

# In[2]:


# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


# <h2 id="circle">Creating an instance of a class Circle</h2>

# In[3]:


# Create an object RedCircle

RedCircle = Circle(10, 'red')


# We can use the <code>dir</code> command to get a list of the object's methods. Many of them are default Python methods.

# In[4]:


# Find out the methods can be used on the object RedCircle

dir(RedCircle)


# We can look at the data attributes of the object:

# In[5]:


# Print the object attribute radius

RedCircle.radius


# In[6]:


# Print the object attribute color

RedCircle.color


# In[7]:


# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius


# In[8]:


# Call the method drawCircle

RedCircle.drawCircle()


# We can increase the radius of the circle by applying the method <code>add_radius()</code>. Let's increases the radius by 2 and then by 5:

# In[9]:


# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)


# In[10]:


# Create a blue circle with a given radius

BlueCircle = Circle(radius=100)


# In[11]:


# Print the object attribute radius

BlueCircle.radius


# In[12]:


# Print the object attribute color

BlueCircle.color


# In[13]:


# Call the method drawCircle

BlueCircle.drawCircle()


# <hr>

# <h2 id="rect">The Rectangle Class</h2>

# Let's create a class rectangle with the attributes of height, width, and color. We will only add the method to draw the rectangle object:

# In[15]:


# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


# In[16]:


# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 3, 'blue')


# In[17]:


# Print the object attribute height

SkinnyBlueRectangle.height


# In[18]:


# Print the object attribute width

SkinnyBlueRectangle.width


# In[19]:


# Print the object attribute color

SkinnyBlueRectangle.color


# In[20]:


# Use the drawRectangle method to draw the shape

SkinnyBlueRectangle.drawRectangle()


# In[21]:


# Create a new object rectangle

FatYellowRectangle = Rectangle(20, 5, 'yellow')


# In[22]:


# Print the object attribute height

FatYellowRectangle.height 


# In[23]:


# Print the object attribute width

FatYellowRectangle.width


# In[24]:


# Print the object attribute color

FatYellowRectangle.color


# In[25]:


# Use the drawRectangle method to draw the shape

FatYellowRectangle.drawRectangle()


# <center>
#     
# # Scenario: Car dealership's inventory management system
# 
# </center>

# ### Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage. 

# In[27]:


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# ### Task-2. Update the class with the default color for all vehicles," white".

# In[28]:


class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# ### Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle. 

# In[29]:


class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity


# ### Task-4. Create a method to display all the properties of an object of the class. 

# In[30]:


class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)


# ### Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kph and mileage of 50000kmpl with five seating capacities, and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.

# In[31]:


# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 50000)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 75000)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. 
# <hr>

# In[ ]:




