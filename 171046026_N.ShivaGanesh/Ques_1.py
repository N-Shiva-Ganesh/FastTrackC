#Which olympics had the most medals won?

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('summer.csv')
counts =  df.Year.value_counts(ascending=True)
y = sorted(set(df.Year))
df1 = pd.DataFrame(counts,y)
#print(df1.head()) #Test GIT
df1.plot(kind = 'bar')
plt.xlabel("Year")
plt.ylabel("No. of Medals")
plt.title("Number of Medals won each time")
plt.show()

