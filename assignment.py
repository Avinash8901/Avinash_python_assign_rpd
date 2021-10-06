#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# In[2]:


#reading a csv document and converting to data frame we use read_csv function
df=pd.read_csv("https://github.com/Avinash8901/Avinash_python_assign_rpd/blob/b2003c7b80c0e233f1da5f7ffd3fd7d012429cee/HDFCBANK_01-01-2021_27-09-2021.csv")
df.head()


# In[3]:


#storing the old names and new names of columns in a dictionary for renaming them in a simple manner
dic={'Date':'date',"High Price":"high","Low Price":"low","Turnover (in lacs)":"turnover_in_lakhs","No. of Contracts":"contracts"}
df.rename(columns=dic,inplace=True)
df.head()


# In[4]:

#creating difference column 
df['difference']=df['high']-df['low']
df.head()


# In[5]:

#converting dataframe to csv
df.to_csv('processed_data.csv')


# In[6]:

#csv to dataframe
co=pd.read_csv('processed_data.csv')
plt.figure(figsize=(15,15))
corr=co.corr()
sns.heatmap(corr,cmap='Greens',annot=True)
plt.show()


# In[7]:

#connecting to dbms
import mysql.connector as dbms


# In[8]:

#creating a connection object
db=dbms.connect(host="localhost",user='root',passwd="111PythonFinTest###",database='python_fin_test')


# In[9]:
#creating a cursor
cursor=db.cursor()


# In[10]:


col=co.columns
col


# In[ ]:

#create statement
cr="create table processed_data(Ind INT(4),date1 varchar2(20),high FLOAT(10,7),low FLOAT(10,7),ClosePrice FLOAT(10,7),Total_traded_quantity INT(11),turnover_in_lakhs FLOAT(10,7),contracts INT(3),Unnamed FLOAT(10,7),difference FLOAT(10,7));"


# In[11]:


#replacing missing values
co.fillna(-1.0,inplace=True)
co.isnull().sum()


# In[ ]:

#creating table
cursor.execute(cr)


# In[ ]:
#inserting values from csv to table
#%s indicates string values
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




