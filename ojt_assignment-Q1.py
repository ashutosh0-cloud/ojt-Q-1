#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. Data Visualization and Statistical Measures: For this question, you are required to analyse the iris dataset (iris.csv) using Python. Perform all possible data visualization techniques (histograms, scatter plots, box plots, etc.) on all numerical columns of the dataset. Additionally, calculate All possible statistical measures (mean, median, mode, standard deviation, etc.) For each numerical column. 


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_data = pd.read_csv('iris.csv')
print(iris)


# In[29]:


# Compute statistical measures
iris.describe()



# In[24]:


# Plot histograms
iris.hist()
plt.show()


# In[25]:


# Plot pairplots
sns.pairplot(iris, hue='species')
plt.show()


# In[26]:


# Plot boxplots
iris.boxplot(by='species', figsize=(12, 6))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




