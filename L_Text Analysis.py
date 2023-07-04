#!/usr/bin/env python
# coding: utf-8

# <center>
#     
# # **Scenario: Text Analysis**
# 
# </center>

# # What is Text analysis?
# Text analysis, also known as text mining or text analytics, refers to the process of extracting meaningful information and insights from textual data.

# # Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large dataset of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:
# 
# **1. String in lower case:**
# You want to Pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.
# 
# **2. Frequency of all words in a given string:**
# After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.
# 
# **3. Frequency of a specific word:**
# In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in the customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.
# 
# By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment

# In[2]:


givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."


# # Task-1 Define the class and its attributes:

# In[4]:


class TextAnalyzer(object):
    def __init__(self, text):
        self.text = text


# # Task-2 Formatting the text:

# 1. Inside the constructor, convert the text argument to lowercase using the `lower()` method.
# 2. Remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the `replace()` method.
# 3. Assign the formatted text to a new attribute called fmtText.
# 
# **Update the above `TextAnalyzer` class with points mentioned above.**

# In[5]:


class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText


# # Task-3 Frequency of all unique words:

# * Implement the `freqAll()` method:
#      1. Split the fmtText attribute into individual words using the `split()` method.
#      2. Create an empty dictionary to store the word frequency.
#      3. Iterate over the list of words and update the frequency dictionary accordingly.
#      4. use `count` method for counting the occurence
#      5. Return the frequency dictionary.
#      
# **Update the above `TextAnalyzer` class with points mentioned above.**

# In[6]:


class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    


# # Task-4 Frequency of a specific word:

# * Implement the `freqOf(word)` method that takes a word argument:
#    1. create method and pass the word that need to be found
#    2. get the `freqAll` method for look for count and check if that word is in the list.
#    3. Return the count.
#    
# **Update the above `TextAnalyzer` class with points mentioned above.**

# In[16]:


class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0


# ## Task-5 Create an instance of analysedText

# In[23]:


class TextAnalyzer(object):
    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
    
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in the list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

# Create an instance of TextAnalyzer
givenstr = "Sample text"
analyzed = TextAnalyzer(givenstr)


# ## Task-6 Print the formatted text(lower case string)

# In[24]:


print("Formatted Text:", analyzed.fmtText)


# ## Task-7 Test freqAll() method

# In[25]:


freqMap = analyzed.freqAll()
print(freqMap)


# ## Task-8 Test freqOf() method
# you have to find the frequency of the following words:-
# 1. "lorem"    
# 2. "diam"   
# 3. "et"    
# <br>
# 
# print the output using **formatting**

# In[26]:


word = "lorem"
frequency = analyzed.freqOf(word)
print(f"The word '{word}' appears {frequency} times.")


# In[27]:


word = "diam"
frequency = analyzed.freqOf(word)
print(f"The word '{word}' appears {frequency} times.")


# In[28]:


word = "et"
frequency = analyzed.freqOf(word)
print(f"The word '{word}' appears {frequency} times.")


# In[ ]:




