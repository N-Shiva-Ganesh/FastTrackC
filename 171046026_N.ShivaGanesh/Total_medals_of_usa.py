#analysis of no of medals won by USA.

import pandas as pd 
import matplotlib.pyplot as plt 

olympics = pd.read_csv('summer.csv')
USA = olympics[olympics.Country == 'USA']
USA_medals = USA.groupby(['Year','Medal'])['Athlete'].count()
USA_medals = USA_medals.unstack(level = 'Medal')

USA_medals.plot.area()
plt.show()
