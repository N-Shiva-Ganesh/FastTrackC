#For supporting Future-Host effect, Australia and United Kingdom's Medals count as been compared.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


count1 = []
count2 = []
df = pd.read_csv('summer.csv')
lis = df.Year
year = list(set(lis))
year.sort()
for i in year:
	frame = df[(df.Year == i) & (df.Country == 'AUS')]
	count1.append(frame.Medal.count())

for i in year:
	frame = df[(df.Year == i) & (df.Country == 'GBR')]
	count2.append(frame.Medal.count())
df2 = pd.DataFrame(count1,year)
df3 = pd.DataFrame(count2,year)

plt.subplot(2,1,1)
plt.plot(df2,'ro',df2,'k')
plt.title('AUSTRALIA')

plt.ylabel('Medals')
plt.subplot(2,1,2)
plt.plot(df3,'bo',df3,'k')
plt.xlabel('YEARS')
plt.ylabel('Medals')
plt.title('UK')
plt.tight_layout()
plt.show()