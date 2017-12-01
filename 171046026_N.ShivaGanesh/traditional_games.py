#In this plot we know which countries is leading in
# Traditional Games like Aquatics, Athletics and Gymnastic

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('summer.csv')
plt.subplot(3,1,1)
frame1 = df[(df.Sport == 'Aquatics')]
a = frame1.Country.value_counts()
a1 = a.head(10)
plt.title('Aquatics')
a1.plot()
a1.plot(style = "o")
plt.subplot(3,1,2)
frame2 = df[df.Sport == 'Athletics']
b = frame2.Country.value_counts()
b1 = b.head(10)
plt.title('Athletics')
b1.plot()
b1.plot(style = "o")
plt.subplot(3,1,3)
frame3 = df[df.Sport == 'Gymnastics']
c = frame3.Country.value_counts()
c1 = c.head(10)
plt.title('Gymnastics')
c1.plot()
c1.plot(style = "o")
plt.show()