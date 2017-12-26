#number of medals won by USA and URS during the period of coldwar(1952-1988)
#RESULT : URS has won more number of times medals during coldwar.
import pandas as pd 

olympics = pd.read_csv('summer.csv')

olympics_usa_urs = olympics.pivot_table(index = 'Year',columns = 'Country',values = 'Athlete',aggfunc = 'count')
medals_of_usa_urs = olympics_usa_urs.loc[1952:1988,['USA','URS']]
max_medals = medals_of_usa_urs.idxmax(axis = 'columns')
maximum = max_medals.value_counts()
print(maximum) 
