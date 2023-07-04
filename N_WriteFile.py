#!/usr/bin/env python
# coding: utf-8

# # Write and Save Files in Python
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * Write to files using Python libraries
# 

# <h2 id="write">Writing Files</h2>
# 

#  We can open a file object using the method <code>write()</code> to save the text file to a list. To write to a file, the mode argument must be set to **w**. Let’s write a file **Example2.txt** with the line: **“This is line A”**
# 

# In[1]:


# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")


#  We can read the file to see if it worked:
# 

# In[2]:


# Read file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


# We can write multiple lines:
# 

# In[3]:


# Write lines to file

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")


# The method <code>.write()</code> works similar to the method <code>.readline()</code>, except instead of reading a new line it writes a new line. The process is illustrated in the figure. The different colour coding of the grid represents a new line added to the file after each method call.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/WriteLine.png" width="500">
# 

# You can check the file to see if your results are correct 
# 

# In[4]:


# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


#  We write a list to a **.txt** file  as follows:
# 

# In[5]:


# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines


# In[6]:


# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)


#  We can verify the file is written by reading it and printing out the values:  
# 

# In[7]:


# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# However, note that setting the mode to __w__ overwrites all the existing data in the file.
# 

# In[8]:


with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# <hr>
# <h2 id="Append">Appending Files</h2>
# 

#  We can write to files without losing any of the existing data as follows by setting the mode argument to append: **a**.  you can append a new line as follows:
# 

# In[10]:


# Write a new line to text file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")


#  You can verify the file has changed by running the following cell:
# 

# In[11]:


# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# <hr>
# <h2 id="add">Additional modes</h2> 
# 

# It's fairly ineffecient to open the file in **a** or **w** and then reopening it in **r** to read any lines. Luckily we can access the file in the following modes:
# - **r+** : Reading and writing. Cannot truncate the file.
# - **w+** : Writing and reading. Truncates the file.
# - **a+** : Appending and Reading. Creates a new file, if none exists.
# You dont have to dwell on the specifics of each mode for this lab. 
# 

# Let's try out the __a+__ mode:
# 

# In[12]:


with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())


# There were no errors but <code>read()</code> also did not output anything. This is because of our location in the file.
# 

# Most of the file methods we've looked at work in a certain location in the file. <code>.write() </code> writes at a certain location in the file. <code>.read()</code> reads at a certain location in the file and so on. You can think of this as moving your pointer around in the notepad to make changes at specific location.
# 

# Opening the file in **w** is akin to opening the .txt file, moving your cursor to the beginning of the text file, writing new text and deleting everything that follows.
# Whereas opening the file in **a** is similiar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text. <br>
# It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -
# - <code>.tell()</code> - returns the current position in bytes
# - <code>.seek(offset,from)</code> - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end
# 

# Now lets revisit **a+**
# 

# In[13]:


with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )


# Finally, a note on the difference between **w+** and **r+**. Both of these modes allow access to read and write methods, however, opening a file in **w+** overwrites it and deletes all pre-existing data. <br>
# To work with a file on existing data, use **r+** and **a+**. While using **r+**, it can be useful to add a <code>.truncate()</code> method at the end of your data. This will reduce the file to your data and delete everything that follows. <br>
# In the following code block, Run the code as it is first and then run it with the <code>.truncate()</code>.
# 

# In[14]:


with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    


# <hr>
# 

# <h2 id="copy">Copy a File</h2> 
# 

# Let's copy the file **Example2.txt** to the file **Example3.txt**:
# 

# In[15]:


# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


# We can read the file to see if everything works:
# 

# In[16]:


# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())


#  After reading files, we can also write data into files and save them in different file formats like **.txt, .csv, .xls (for excel files) etc**. You will come across these in further examples
# 

# **NOTE:** If you wish to open and view the `example3.txt` file, download this lab [here](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/PY0101EN-4-2-WriteFile.ipynb) and run it locally on your machine. Then go to the working directory to ensure the `example3.txt` file exists and contains the summary data that we wrote.
# 

# <hr>
# 

# <h2> Exercise </h2>
# 

# Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills. <br>
# Given the file `currentMem`, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the `exMem` file. Make sure that the format of the original files in preserved.   (*Hint: Do this by reading/writing whole lines and ensuring the header remains* )
# <br>
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the `cleanFiles` function.
# 

# In[17]:


#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


# Now that you've run the prerequisite code cell above, which prepared the files for this exercise, you are ready to move on to the implementation.
# 
# #### **Exercise:** Implement the cleanFiles function in the code cell below.
# 

# In[18]:


'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
        #TODO: Open the exMem file in a+ mode

        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Hint: Recall that the first line in the file is the header.

        #TODO: iterate through the members and create a new list of the innactive members

        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem

        
    
    pass # Remove this line when done implementation


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
    


# The code cell below is to verify your solution. Please do not modify the code and run it to test your implementation of `cleanFiles`.
# 

# In[20]:


def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    
def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            #go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()
                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed this lesson and hands-on lab in Python. 
# <hr>
# 
