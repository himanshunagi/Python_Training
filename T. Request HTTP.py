#!/usr/bin/env python
# coding: utf-8

# <h1> HTTP and Requests</h1>
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Understand HTTP
# *   Handle HTTP Requests

# <h2 id="">Overview of HTTP </h2>
# 

# When you, the **client**, use a web page your browser sends an **HTTP** request to the **server** where the page is hosted. The server tries to find the desired **resource** by default "<code>index.html</code>". If your request is successful, the server will send the object to the client in an **HTTP response**. This includes information like the type of the **resource**, the length of the **resource**, and other information.
# 
# <p>
# The figure below represents the process. The circle on the left represents the client, the circle on the right represents the Web server. The table under the Web server represents a list of resources stored in the web server. In  this case an <code>HTML</code> file, <code>png</code> image, and <code>txt</code> file .
# </p>
# <p>
# The <b>HTTP</b> protocol allows you to send and receive information through the web including webpages, images, and other web resources. In this lab, we will provide an overview of the Requests library for interacting with the <code>HTTP</code> protocol. 
# </p
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/reqest_basics.png" width="750" align="center">
# 
# </div>

# <h2 id="URL">Uniform Resource Locator: URL</h2>
# 

# Uniform resource locator (URL) is the most popular way to find resources on the web.  We can break the URL into three parts.
# 
# <ul>
#     <li><b>Scheme</b>:- This is this protocol, for this lab it will always be <code>http://</code>  </li>
#     <li><b> Internet address or  Base URL </b>:- This will be used to find the location here are some examples: <code>www.ibm.com</code> and  <code> www.gitlab.com </code> </li>
#     <li><b>Route</b>:- Location on the web server for example: <code>/images/IDSNlogo.png</code> </li>
# </ul>
# 

# <h2 id="RE">Request </h2>
# 

# The process can be broken into the <b>Request</b> and <b>Response </b> process.  The request using the get method is partially illustrated below. In the start line we have the <code>GET</code> method, this is an <code>HTTP</code> method. Also the location of the resource  <code>/index.html</code> and the <code>HTTP</code> version. The Request header passes additional information with an <code>HTTP</code> request:
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/reqest_messege.png" width="400" align="center">
# </div>
# 

# When an <code>HTTP</code> request is made, an <code>HTTP</code> method is sent, this tells the server what action to perform.  A list of several <code>HTTP</code> methods is shown below. We will go over more examples later.
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/http_methods.png" width="400" align="center">
# </div>

# <h2 id="RES">Response</h2>

# The figure below represents the response; the response start line contains the version number <code>HTTP/1.0</code>, a status code (200) meaning success, followed by a descriptive phrase (OK). The response header contains useful information. Finally, we have the response body containing the requested file, an <code> HTML </code> document.  It should be noted that some requests have headers.

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/response_message.png" width="400" align="center">
# </div>

# Some status code examples are shown in the table below, the prefix indicates the class. These are shown in yellow, with actual status codes shown in  white. Check out the following <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">link </a> for more descriptions.
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/status_code.png" width="300" align="center">
# </div>
# 

# <h2 id="RP">Requests in Python</h2>

# In[2]:


import requests


# In[3]:


import os 
from PIL import Image
from IPython.display import IFrame


# In[4]:


url='https://www.ibm.com/'
r=requests.get(url)


# We have the response object <code>r</code>, this has information about the request, like the status of the request. We can view the status code using the attribute <code>status_code</code>.

# In[5]:


r.status_code


# In[6]:


print(r.request.headers)


# In[7]:


print("request body:", r.request.body)


# In[8]:


header=r.headers
print(r.headers)


# In[9]:


header['date']


# In[10]:


header['Content-Type']


# In[11]:


r.encoding


# As the <code>Content-Type</code> is <code>text/html</code> we can use the attribute <code>text</code> to display the <code>HTML</code> in the body. We can review the first 100 characters:

# In[13]:


r.text[0:100]


# In[14]:


# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'


# In[15]:


r=requests.get(url)


# In[16]:


print(r.headers)


# In[17]:


r.headers['Content-Type']


# In[18]:


path=os.path.join(os.getcwd(),'image.png')
path


# In[19]:


with open(path,'wb') as f:
    f.write(r.content)


# In[20]:


Image.open(path)  


# <h3>Question 1: write <a href="https://www.gnu.org/software/wget/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01"><code> wget </code></a></h3>

# <code>!wget -O /resources/data/Example1.txt <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt></code>
# 

# In[21]:


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)


# <h2 id="URL_P">Get Request with URL Parameters </h2>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/base_URL_Route.png" width="400" align="center">
# </div>

# In[23]:


url_get='http://httpbin.org/get'


# In[24]:


payload={"name":"Joseph","ID":"123"}


# In[25]:


r=requests.get(url_get,params=payload)


# In[26]:


r.url


# In[27]:


print("request body:", r.request.body)


# In[28]:


print(r.status_code)


# In[29]:


print(r.text)


# In[30]:


r.headers['Content-Type']


# In[31]:


r.json()


# In[32]:


r.json()['args']


# <h2 id="POST">Post Requests  </h2>

# In[33]:


url_post='http://httpbin.org/post'


# In[34]:


r_post=requests.post(url_post,data=payload)


# In[35]:


print("POST request URL:",r_post.url )
print("GET request URL:",r.url)


# In[36]:


print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)


# In[37]:


r_post.json()['form']


# There is a lot more you can do. Check out <a href="https://requests.readthedocs.io/en/master/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Requests </a> for more.

# In[ ]:




