
# coding: utf-8

# In[16]:


import pandas as pd 
import numpy as np
import sys

sys.stdout = open("Results.txt", "w")



file1_df = pd.read_csv('budget_data_1.csv')
file1_df.head()


# In[8]:


total_month = file1_df['Date'].count()
total_month


# In[53]:


total_rev_num = file1_df['Revenue'].sum()
total_rev='${:,.2f}'.format(total_rev_num)
total_rev


# In[54]:


avg_change = total_rev_num/total_month
avg_change_num = '${:,.2f}'.format(avg_change)
avg_change_num


# In[57]:


max_val = file1_df['Revenue'].max()
max_index = file1_df[file1_df['Revenue'] == max_val].index[0]
max_date = file1_df['Date'].loc[max_index]
max_val_num = '${:,.2f}'.format(max_val)
max_date


# In[59]:


min_val = file1_df['Revenue'].min()
min_index = file1_df[file1_df['Revenue'] == min_val].index[0]
min_date = file1_df['Date'].loc[min_index]
min_val_num = '${:,.2f}'.format(min_val)
min_date


# In[61]:


print('Financial Analysis')
print('----------------------------')
print('Total Months: '+str(total_month))
print('Total Revenue: '+(total_rev))
print('Average Revenue Change: '+ avg_change_num)
print('Greatest Increase in Revenue: '+ max_date+' ('+max_val_num+')')
print('Greatest Decrease in Revenue: '+ min_date+' ('+min_val_num+')')

