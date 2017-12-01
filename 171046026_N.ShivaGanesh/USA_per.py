import pandas as pd
import matplotlib.pyplot as plt

lis = []
gold = []
sliver = []
bronze = []
frame = pd.read_csv('summer.csv')
df = frame[frame.Country == 'USA']
# print df
year = frame.Year
year = list(set(year))
year.sort()
# print (year)
for y in year:
    y_table = df[df.Year == y]
    gold_medals = y_table.Medal.str.contains('Gold').sum()
    sliver_medals = y_table.Medal.str.contains('Silver').sum()
    bronze_medals = y_table.Medal.str.contains('Bronze').sum()
    gold.append(gold_medals)
    sliver.append(sliver_medals)
    bronze.append(bronze_medals)

a = [sum(gold), sum(sliver), sum(bronze)]


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


l = ['Gold', 'Silver', 'Bronze']
clr = ['gold', 'lightgrey', '#a87900']
expld = (0.01, 0.01, 0.01)
plt.pie(a, labels=l, colors=clr, explode=expld, autopct=make_autopct(a), shadow=False)
plt.show()
