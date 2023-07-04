#!/usr/bin/env python
# coding: utf-8

# # **Web Scraping Lab**
# 

# ## Objectives
# 

# After completing this lab you will be able to:
# 

# For this lab, we are going to be using Python and several Python libraries. Some of these libraries might be installed in your lab environment or in SN Labs. Others may need to be installed by you. The cells below will install these libraries when executed.
# 

# In[7]:


get_ipython().system('pip install bs4==4.10.0')
get_ipython().system('pip install lxml==4.6.4')
get_ipython().system('pip install html5lib==1.1')


# Import the required modules and functions
# 

# In[11]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# <h2 id="BSO">Beautiful Soup Objects</h2>
# 

# Beautiful Soup is a Python library for pulling data out of HTML and XML files, we will focus on HTML files. This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML.  We can navigate the HTML as a tree and/or filter out what we are looking for.
# 
# Consider the following HTML:
# 

# In[12]:


get_ipython().run_cell_magic('html', '', "<!DOCTYPE html>\n<html>\n<head>\n<title>Page Title</title>\n</head>\n<body>\n<h3><b id='boldest'>Lebron James</b></h3>\n<p> Salary: $ 92,000,000 </p>\n<h3> Stephen Curry</h3>\n<p> Salary: $85,000, 000 </p>\n<h3> Kevin Durant </h3>\n<p> Salary: $73,200, 000</p>\n</body>\n</html>\n")


# We can store it as a string in the variable HTML:
# 

# In[13]:


html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"


# To parse a document, pass it into the <code>BeautifulSoup</code> constructor, the <code>BeautifulSoup</code> object, which represents the document as a nested data structure:
# 

# In[14]:


soup = BeautifulSoup(html, "html.parser")


# First, the document is converted to Unicode, (similar to ASCII),  and HTML entities are converted to Unicode characters. Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. The <code>BeautifulSoup</code> object can create other types of objects. In this lab, we will cover <code>BeautifulSoup</code> and <code>Tag</code> objects that for the purposes of this lab are identical, and <code>NavigableString</code> objects.
# 

# We can use the method <code>prettify()</code> to display the HTML in the nested structure:
# 

# In[15]:


print(soup.prettify())


# ## Tags
# 

# Let's say we want the  title of the page and the name of the top paid player we can use the <code>Tag</code>. The <code>Tag</code> object corresponds to an HTML tag in the original document, for example, the tag title.
# 

# In[16]:


tag_object=soup.title
print("tag object:",tag_object)


# we can see the tag type <code>bs4.element.Tag</code>
# 

# In[17]:


print("tag object type:",type(tag_object))


# If there is more than one <code>Tag</code>  with the same name, the first element with that <code>Tag</code> name is called, this corresponds to the most paid player:
# 

# In[18]:


tag_object=soup.h3
tag_object


# Enclosed in the bold attribute <code>b</code>, it helps to use the tree representation. We can navigate down the tree using the child attribute to get the name.
# 

# ### Children, Parents, and Siblings
# 

# As stated above the <code>Tag</code> object is a tree of objects we can access the child of the tag or navigate down the branch as follows:
# 

# In[19]:


tag_child =tag_object.b
tag_child


# You can access the parent with the <code> parent</code>
# 

# In[20]:


parent_tag=tag_child.parent
parent_tag


# this is identical to
# 

# In[21]:


tag_object


# <code>tag_object</code> parent is the <code>body</code> element.
# 

# In[22]:


tag_object.parent


# <code>tag_object</code> sibling is the <code>paragraph</code> element
# 

# In[23]:


sibling_1=tag_object.next_sibling
sibling_1


# `sibling_2` is the `header` element which is also a sibling of both `sibling_1` and `tag_object`
# 

# In[24]:


sibling_2=sibling_1.next_sibling
sibling_2


# <h3 id="first_question">Exercise: <code>next_sibling</code></h3>
# 

# Using the object <code>sibling\_2</code> and the property <code>next_sibling</code> to find the salary of Stephen Curry:
# 

# In[25]:


sibling_2.next_sibling


# ### HTML Attributes
# 

# If the tag has attributes, the tag <code>id="boldest"</code> has an attribute <code>id</code> whose value is <code>boldest</code>. You can access a tag’s attributes by treating the tag like a dictionary:
# 

# In[26]:


tag_child['id']


# You can access that dictionary directly as <code>attrs</code>:
# 

# In[27]:


tag_child.attrs


# You can also work with Multi-valued attribute check out <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01">\[1]</a> for more.
# 

# We can also obtain the content if the attribute of the <code>tag</code> using the Python <code>get()</code> method.
# 

# In[28]:


tag_child.get('id')


# ### Navigable String
# 

# A string corresponds to a bit of text or content within a tag. Beautiful Soup uses the <code>NavigableString</code> class to contain this text. In our HTML we can obtain the name of the first player by extracting the sting of the <code>Tag</code> object <code>tag_child</code> as follows:
# 

# In[29]:


tag_string=tag_child.string
tag_string


# we can verify the type is Navigable String
# 

# In[30]:


type(tag_string)


# A NavigableString is just like a Python string or Unicode string, to be more precise. The main difference is that it also supports some  <code>BeautifulSoup</code> features. We can covert it to sting object in Python:
# 

# In[31]:


unicode_string = str(tag_string)
unicode_string


# <h2 id="filter">Filter</h2>
# 

# Filters allow you to find complex patterns, the simplest filter is a string. In this section we will pass a string to a different filter method and Beautiful Soup will perform a match against that exact string.  Consider the following HTML of rocket launchs:
# 

# In[32]:


get_ipython().run_cell_magic('html', '', "<table>\n  <tr>\n    <td id='flight' >Flight No</td>\n    <td>Launch site</td> \n    <td>Payload mass</td>\n   </tr>\n  <tr> \n    <td>1</td>\n    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>\n    <td>300 kg</td>\n  </tr>\n  <tr>\n    <td>2</td>\n    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>\n    <td>94 kg</td>\n  </tr>\n  <tr>\n    <td>3</td>\n    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>\n    <td>80 kg</td>\n  </tr>\n</table>\n")


# We can store it as a string in the variable <code>table</code>:
# 

# In[33]:


table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"


# In[34]:


table_bs = BeautifulSoup(table, "html.parser")


# ## find All
# 

# The <code>find_all()</code> method looks through a tag’s descendants and retrieves all descendants that match your filters.
# 
# <p>
# The Method signature for <code>find_all(name, attrs, recursive, string, limit, **kwargs)<c/ode>
# </p>
# 

# ### Name
# 

# When we set the <code>name</code> parameter to a tag name, the method will extract all the tags with that name and its children.
# 

# In[35]:


table_rows=table_bs.find_all('tr')
table_rows


# The result is a Python Iterable just like a list, each element is a <code>tag</code> object:
# 

# In[36]:


first_row =table_rows[0]
first_row


# The type is <code>tag</code>
# 

# In[37]:


print(type(first_row))


# we can obtain the child
# 

# In[38]:


first_row.td


# If we iterate through the list, each element corresponds to a row in the table:
# 

# In[39]:


for i,row in enumerate(table_rows):
    print("row",i,"is",row)
    


# As <code>row</code> is a <code>cell</code> object, we can apply the method <code>find_all</code> to it and extract table cells in the object <code>cells</code> using the tag <code>td</code>, this is all the children with the name <code>td</code>. The result is a list, each element corresponds to a cell and is a <code>Tag</code> object, we can iterate through this list as well. We can extract the content using the <code>string</code>  attribute.
# 

# In[40]:


for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)


# If we use a list we can match against any item in that list.
# 

# In[41]:


list_input=table_bs .find_all(name=["tr", "td"])
list_input


# ## Attributes
# 

# If the argument is not recognized it will be turned into a filter on the tag’s attributes. For example the <code>id</code>  argument, Beautiful Soup will filter against each tag’s <code>id</code> attribute. For example, the first <code>td</code> elements have a value of <code>id</code> of <code>flight</code>, therefore we can filter based on that <code>id</code> value.
# 

# In[42]:


table_bs.find_all(id="flight")


# We can find all the elements that have links to the Florida Wikipedia page:
# 

# In[43]:


list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input


# If we set the  <code>href</code> attribute to True, regardless of what the value is, the code finds all tags with <code>href</code> value:
# 

# In[44]:


table_bs.find_all(href=True)


# There are other methods for dealing with attributes and other related methods; Check out the following <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01#css-selectors'>link</a>
# 

# <h3 id="exer_type">Exercise: <code>find_all</code></h3>
# 

# Using the logic above, find all the elements without <code>href</code> value
# 

# In[45]:


table_bs.find_all(href=False)


# Using the soup object <code>soup</code>, find the element with the <code>id</code> attribute content set to <code>"boldest"</code>.
# 

# In[46]:


soup.find_all(id="boldest")


# ### string
# 

# With string you can search for strings instead of tags, where we find all the elments with Florida:
# 

# In[47]:


table_bs.find_all(string="Florida")


# ## find
# 

# The <code>find_all()</code> method scans the entire document looking for results, it’s if you are looking for one element you can use the <code>find()</code> method to find the first element in the document. Consider the following two table:
# 

# In[48]:


get_ipython().run_cell_magic('html', '', "<h3>Rocket Launch </h3>\n\n<p>\n<table class='rocket'>\n  <tr>\n    <td>Flight No</td>\n    <td>Launch site</td> \n    <td>Payload mass</td>\n  </tr>\n  <tr>\n    <td>1</td>\n    <td>Florida</td>\n    <td>300 kg</td>\n  </tr>\n  <tr>\n    <td>2</td>\n    <td>Texas</td>\n    <td>94 kg</td>\n  </tr>\n  <tr>\n    <td>3</td>\n    <td>Florida </td>\n    <td>80 kg</td>\n  </tr>\n</table>\n</p>\n<p>\n\n<h3>Pizza Party  </h3>\n  \n    \n<table class='pizza'>\n  <tr>\n    <td>Pizza Place</td>\n    <td>Orders</td> \n    <td>Slices </td>\n   </tr>\n  <tr>\n    <td>Domino's Pizza</td>\n    <td>10</td>\n    <td>100</td>\n  </tr>\n  <tr>\n    <td>Little Caesars</td>\n    <td>12</td>\n    <td >144 </td>\n  </tr>\n  <tr>\n    <td>Papa John's </td>\n    <td>15 </td>\n    <td>165</td>\n  </tr>\n")


# We store the HTML as a Python string and assign <code>two_tables</code>:
# 

# In[49]:


two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"


# We create a <code>BeautifulSoup</code> object  <code>two_tables_bs</code>
# 

# In[50]:


two_tables_bs= BeautifulSoup(two_tables, 'html.parser')


# We can find the first table using the tag name table
# 

# In[51]:


two_tables_bs.find("table")


# We can filter on the class attribute to find the second table, but because class is a keyword in Python, we add an underscore.
# 

# In[52]:


two_tables_bs.find("table",class_='pizza')


# <h2 id="DSCW">Downloading And Scraping The Contents Of A Web Page</h2> 
# 

# We Download the contents of the web page:
# 

# In[53]:


url = "http://www.ibm.com"


# We use <code>get</code> to download the contents of the webpage in text format and store in a variable called <code>data</code>:
# 

# In[54]:


data  = requests.get(url).text 


# We create a <code>BeautifulSoup</code> object using the <code>BeautifulSoup</code> constructor
# 

# In[55]:


soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'


# Scrape all links
# 

# In[56]:


for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# ## Scrape  all images  Tags
# 

# In[57]:


for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# ## Scrape data from HTML tables
# 

# In[58]:


#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check how many rows and columns are there in the color table.
# 

# In[59]:


# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text


# In[60]:


soup = BeautifulSoup(data,"html.parser")


# In[61]:


#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>


# In[62]:


#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


# ## Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
# 

# In[63]:


import pandas as pd


# In[64]:


#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"


# Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check the tables on the webpage.
# 

# In[65]:


# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text


# In[66]:


soup = BeautifulSoup(data,"html.parser")


# In[67]:


#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>


# In[68]:


# we can see how many tables were found by checking the length of the tables list
len(tables)


# Assume that we are looking for the `10 most densly populated countries` table, we can look through the tables list and find the right one we are look for based on the data in each table or we can search for the table name if it is in the table but this option might not always work.
# 

# In[69]:


for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)


# See if you can locate the table name of the table, `10 most densly populated countries`, below.
# 

# In[70]:


print(tables[table_index].prettify())


# In[71]:


population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data


# ## Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html
# 

# Using the same `url`, `data`, `soup`, and `tables` object as in the last section we can use the `read_html` function to create a DataFrame.
# 
# Remember the table we need is located in `tables[table_index]`
# 
# We can now use the `pandas` function `read_html` and give it the string version of the table as well as the `flavor` which is the parsing engine `bs4`.
# 

# In[72]:


pd.read_html(str(tables[5]), flavor='bs4')


# The function `read_html` always returns a list of DataFrames so we must pick the one we want out of the list.
# 

# In[73]:


population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html


# ## Scrape data from HTML tables into a DataFrame using read_html
# 

# We can also use the `read_html` function to directly get DataFrames from a `url`.
# 

# In[74]:


dataframe_list = pd.read_html(url, flavor='bs4')


# We can see there are 25 DataFrames just like when we used `find_all` on the `soup` object.
# 

# In[75]:


len(dataframe_list)


# Finally we can pick the DataFrame we need out of the list.
# 

# In[76]:


dataframe_list[5]


# We can also use the `match` parameter to select the specific table we want. If the table contains a string matching the text it will be read.
# 

# In[77]:


pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]

