#Number of Medals USA have won..


import pandas as pd
import matplotlib.pyplot as plt 

lis = []
gold = []
sliver = []
bronze = []
frame = pd.read_csv('summer.csv')
df = frame[frame.Country == 'USA']

year = frame.Year 
year = list(set(year))
year.sort()

for y in year:
	y_table = df[df.Year == y]
	gold_medals = y_table.Medal.str.contains('Gold').sum()
	sliver_medals = y_table.Medal.str.contains('Silver').sum()
	bronze_medals = y_table.Medal.str.contains('Bronze').sum()
	gold.append(gold_medals)
	sliver.append(sliver_medals)
	bronze.append(bronze_medals)

dic= { 'bronze':bronze,'silver':sliver,'gold': gold }
dataf = pd.DataFrame(dic,index= year,columns=['bronze','silver','gold'])
dataf.plot(kind = 'bar',stacked = 'True',color=['#a87900','lightgrey','gold'])

plt.xlabel('years')
plt.ylabel('medals')
plt.title('medal analysis of USA Country')
#plt.legend((a,b,c),('gold medals','sliver medals','bronze medals'))
plt.show()