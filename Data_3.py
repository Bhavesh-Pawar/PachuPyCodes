import matplotlib.pyplot as plt 
x=[1400,250,450,890,1000]
y=["rent","personal","general","picnic","grocery"]
plt.pie(x,labels=y,autopct="%0.2f%%",startangle=75,explode=[0.2,0,0,0,0],
shadow=True,normalize=True)
plt.show()