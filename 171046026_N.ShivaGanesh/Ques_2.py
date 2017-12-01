#Which cities have hosted the games more than once?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('summer.csv')
year = df.Year
city = df.City
data = { 'year' : year,
		 'city' : city}
df = pd.DataFrame(data,columns = ['year','city'])
frame1 = df.drop_duplicates(subset=None, keep='first', inplace=False)
count = frame1.city.value_counts()
print(count)

l = count.head(4)
print(l)
m = ['London','Athens','Los Angeles','Paris']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '({v:d})'.format(p=pct,v=val)
    return my_autopct
expld = (0.01,0.01,0.01,0.01)
plt.pie(l,labels=m,explode=expld, autopct =make_autopct(l), shadow = False)
plt.title('number of times each city hosted:')
plt.show()