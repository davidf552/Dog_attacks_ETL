import pandas as pd 


#Extract 
df = pd.read_csv("dog_attacks.csv")

#Transform
df = df.drop(columns =['desc'])

#The character ' of some names will cause problems at the moment of inserting them into the table. 
#It must be replaced with something else
df = df.replace(to_replace = "'", value = "_", regex = True)
df = df.replace(to_replace = ",", value = " ", regex = True)
df = df.replace(to_replace = "Illlinois", value = "Illinois", regex = True)

df = df.replace(to_replace = "Brooklyn", value = "New York", regex = True)
df = df.replace(to_replace = "Flatbush", value = "New York City", regex = True)
df = df.replace(to_replace = "Perry County", value = "Pennsylvania", regex = True)

#groupby uses the index id to group the data
df['dog_number'] = df['dog_type'].str.extractall(pat = '(\d+)').astype(int).groupby(level=0).sum()

#In the event where no number of dogs is recorded, it will be assumed it is one.
df = df.fillna(value = 1)
df['dog_number'] = df['dog_number'].astype(int)
df[['month', 'day']] = df['date'].str.split(" ", expand = True)

df.index+=1

#Load
names = ['month','day','year','city','state','vic_name','vic_age','dog_type','dog_number']

df.to_csv("dog_analysis.csv",columns = names, index = True, header = False)
df.to_csv("dog_analysisv2.csv",columns = names, index = True, header = True, index_label = 'id')

#A client is needed to upload the csv files to de database. It can be either by using Python, PgAdmin 4 or others.