import matplotlib.pyplot as plt
import numpy as np

"""
xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()
"""
"""
xpoints = np.array([7,2,5,2,7])

apoints = np.array([0,2,4])
bpoints = np.array([2,6,2])

plt.plot(xpoints,c = 'black')
plt.plot(apoints,bpoints,c = 'black')

# plt.xlabel("")
# plt.ylabel("")
# plt.title("")

# plt.grid()

# plt.scatter(apoints,bpoints)
"""
x = ['CR','LM','NM']
y = np.array([5,3,1])

# plt.bar(x,y,color = "black")
plt.pie(y ,labels = x,startangle=90)
plt.title("Champions League")
plt.show()