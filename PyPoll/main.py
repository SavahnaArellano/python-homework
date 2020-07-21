
# coding: utf-8

# In[64]:


import pandas as pd
import numpy
import sys

sys.stdout = open("Results.txt", "w")


# In[22]:


file1_df = pd.read_csv('election_data_1.csv')


# In[31]:


total = file1_df['Voter ID'].count()
total


# In[23]:


file1_df['Candidate'].unique()


# In[24]:


file1_votes = file1_df['Candidate'].value_counts()
file1_votes


# In[25]:


print('Election Results')


# In[34]:


print('-------------------------')
print('Total Votes: '+ str(total))
print('-------------------------')


# In[75]:


candidates = file1_df['Candidate'].unique()
candidates = candidates.tolist()
type(candidates)


# In[76]:


votes = file1_votes.tolist()
type(votes)


# In[81]:


pair = dict(zip(candidates,votes))
#print(pair)


# In[85]:


for (c,v) in pair.items():
    percent = (v/total)*100
    print (c +": "+str(percent)+'% ('+str(v)+')')


# In[90]:


print('-------------------------')
print('Winner: '+next(iter(pair)))
print('-------------------------')

