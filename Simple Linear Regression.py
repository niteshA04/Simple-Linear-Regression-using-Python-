#!/usr/bin/env python
# coding: utf-8

# # 1. Import Libraries

# In[1]:


#First Import the necessary Librarys

#1
import numpy as np 
#used to work with multidimensional array 
#(p.s: numpy is not required for now, but it is good practice to write it)


#2
import pandas as pd
#used to organize data in tabular form


#3
import matplotlib.pyplot as plt
#it is a 2D visualization tool for plotting

#4
import statsmodels.api as sm
#it is used to get table summeries

#Optional Step
import seaborn as sb
sb.set()
#it beautifies the graphs
#difference is shown at the end of the notebook


# # 2. Now Import Data

# In[2]:


data = pd.read_csv('real_estate_price_size.csv')
#our excel sheet has extension .csv and all of our data is stored in data variable


# # 3. Describe the Data

# In[3]:


data.describe()
#it gives necessary calculations automatically


# # 4. Create Variables

# In[4]:


y = data['price'] 
#(on Y-axis) it is a dependent variable, also one of the columns in our data set.
#data which is dependent variables is displayed on Y-axis

x1 = data['size']
#(on X-axis) it is a independent variable, also one of the columns in our data set.
#data which is independent variables is displayed on X-axis


# # 5. Create scatter graph

# In[5]:


plt.scatter(x1, y)
#creats scatter graph

plt.xlabel('SIZE', fontsize=20)
plt.ylabel('PRICE', fontsize=20)
#giving label to X, Y axis and its size to 20


# In[6]:


x = sm.add_constant(x1)
result = sm.OLS(y,x).fit()
result.summary()
#OLS is a method in statsmodels used for estimating linear regression
#it creates a table with necessary calculations


# # Create Linear Regression

# In[7]:


plt.scatter(x1,y)

yhat = 223.1787*x1 + 1.09
# formula y = mx + c

fig = plt.plot(x1, yhat, lw=4, c='orange', label='regression line')
#Creates the line graph

plt.xlabel('Size', fontsize=20)
plt.ylabel('Price', fontsize=20)
#Labelling Axis

plt.show()
#Displays the Graph


# # Before Using Seaborn

# ![beforeSeaborn.png](attachment:beforeSeaborn.png)

# # After Using Seaborn

# ![afterSeaborn.png](attachment:afterSeaborn.png)

# In[ ]:




