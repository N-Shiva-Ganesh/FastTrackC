import pandas as pd

frame = pd.read_csv('summer.csv')

arr = []
while True:
    a = eval(input('Enter the Year and enter 000 to proceed:\n'))
    if (a == 0):
        break
    if (a % 4 == 0) and (a in range(1896, 2016)):
        arr.append(a)
        continue
    else:
        print('Enter years only between 1896 to 2012 and with year gap of 4')
        quit()


print(arr)
country = eval(input('Enter the country'))

for x in arr:
    df = frame[(frame.Year == x) & (frame.Country == country)]
    sports = list(set(df.Sport))
    sports.sort()
    gold = []
    silver = []
    bronze = []
    for y in sports:
        y_table = df[df.Sport == y]

        gold_medals = y_table.Medal.str.contains('Gold').sum()
        gold.append(gold_medals)
        silver_medals = y_table.Medal.str.contains('Silver').sum()
        silver.append(silver_medals)
        bronze_medals = y_table.Medal.str.contains('Bronze').sum()
        bronze.append(bronze_medals)

    dic = {'bronze': bronze, 'silver': silver, 'gold': gold}
    dataf = pd.DataFrame(dic, index=sports, columns=['bronze', 'silver', 'gold'])
    print(str(x) + 'th Year')
    print(dataf)
    print('Total Medal=')
    a = sum(gold)
    b = sum(silver)
    c = sum(bronze)
    s = (a + b + c)
    print(s)
    print('\n')

	
