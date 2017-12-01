#Top 10 Medalists

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

frame = pd.read_csv('summer.csv')
df = frame.Athlete.value_counts(ascending = False)
print (df.head(10))
df1 = df.head(10)
df1.plot(kind = 'bar', color = 'grgggrgrr')
plt.xlabel('Athlete Name')
plt.ylabel('No of Medals Won')
plt.title('Top 10 medal winners:')
plt.show()
