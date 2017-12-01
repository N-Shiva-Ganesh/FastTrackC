#Pie chart (supportive) for medals by countries. Place it inside bar graph.


import pandas as pd 
import matplotlib.pyplot as plt

frame = pd.read_csv('summer.csv')
df = frame.Country.value_counts(ascending = False)
#print (df.head(50))
df1 = df.head(13) #Consider top 13 countries out of which top 1 country is exploded
plt.title("Medals won in olympics - By countries")
df1.plot(kind = 'pie', autopct='%1.1f%%',explode = (0.1,0,0,0,0,0,0,0,0,0,0,0,0),shadow='True',startangle = 90)
plt.show()
