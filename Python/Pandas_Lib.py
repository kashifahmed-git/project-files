import pandas as pd
import matplotlib.pyplot as plt

# mydata={'cars': ['BMW','Rolls Royce','Mercedes Benz'],'Price': ['50L','5Cr','50L'] }

# mydata2={"Ronaldo": 7 ,"Messi" : 10 }

View = pd.read_csv('data.csv')

# print(View.loc[1:])

View.plot(kind = 'scatter',x='Duration',y='Pulse')
plt.show()



"""
m = View['Calories'].mean()
print(m)

View['Calories'].fillna(m,inplace=True)
print(View['Calories'].loc[15:30])


# print(View['Calories'])

"""
