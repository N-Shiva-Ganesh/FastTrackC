#Male and Female Equality in medal winning

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

frame = pd.read_csv('summer.csv')
d_male = frame[frame.Gender == 'Men']
d_female = frame[frame.Gender == 'Women']
count1 = []
count2 = []
year = frame.Year
year = set(year)
year = list(year)
year.sort()
print (year)
for i in year:
	df1 = d_male[(d_male.Year == i)]
	count = df1.Gender.count()
	count1.append(count)


for i in year:
	df2 = d_female[(d_female.Year == i)]
	count = df2.Gender.count()
	count2.append(count)


p = plt.bar(year,count1,align = 'center',width = 2,color = 'black')
q = plt.bar(year,count2,align = 'edge',width = 2,color = 'red')
plt.title('male and female participants in every olympics ')
plt.legend((p,q),('male','female'))
plt.xlabel('Year')
plt.ylabel("Medals")
plt.show()

