#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# In[2]:


#reading a csv document and converting to data frame we use read_csv function
df=pd.read_csv("C:/Users/Avinash/Downloads/HDFCBANK_01-01-2021_27-09-2021.csv")
df.head()


# In[3]:


#storing the old names and new names of columns in a dictionary for renaming them in a simple manner
dic={'Date':'date',"High Price":"high","Low Price":"low","Turnover (in lacs)":"turnover_in_lakhs","No. of Contracts":"contracts"}
df.rename(columns=dic,inplace=True)
df.head()


# In[4]:


df['difference']=df['high']-df['low']
df.head()


# In[5]:


df.to_csv('C:/assignment/processed_data.csv')


# In[6]:


co=pd.read_csv('C:/assignment/processed_data.csv')
plt.figure(figsize=(15,15))
corr=co.corr()
sns.heatmap(corr,cmap='Greens',annot=True)
plt.show()


# In[7]:


import mysql.connector as dbms


# In[8]:


db=dbms.connect(host="localhost",user='root',passwd="111PythonFinTest###",database='python_fin_test')


# In[9]:


cursor=db.cursor()


# In[10]:


col=co.columns
col


# In[ ]:


cr="create table processed_data(Ind INT(4),date1 varchar2(20),high FLOAT(10,7),low FLOAT(10,7),ClosePrice FLOAT(10,7),Total_traded_quantity INT(11),turnover_in_lakhs FLOAT(10,7),contracts INT(3),Unnamed FLOAT(10,7),difference FLOAT(10,7));"


# In[11]:



co.fillna(-1.0,inplace=True)
co.isnull().sum()


# In[ ]:


s="DROP TABLE processed_data"
cursor.execute(s)


# In[ ]:


cursor.execute(cr)


# In[ ]:


for i,row in co.iterrows():
            #here %S means string values 
            sql = "INSERT INTO processed_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
cursor.commit()


# In[ ]:


s="select * from processed_data;"


# In[ ]:


print(s)


# In[ ]:



