#Medals won by each countries

import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv('summer.csv')
df = frame.Country.value_counts(ascending = False) #sorting it in descending order
#print (df.head(5))
df1 = df.head(13) #Considering only top 13 countries for plotting(based on medal count)
plt.title("Medals won in olympics - By countries")
plt.xlabel("Countries")
plt.ylabel("No of Medals")
df1.plot(kind = 'bar')
plt.show()
