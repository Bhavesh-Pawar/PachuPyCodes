import matplotlib.pyplot as plt  
import numpy as np 
X=np.arange(0,4)
c=["ggl","amz","msft","fb"]
profit=[30,7,45,23]
rev=[120,94,185,145]
plt.xlabel("Company")
plt.ylabel("revenue(in bln)")
plt.xticks(X,c)
plt.bar(X+0.00,rev,width=0.35,color="r")
plt.bar(X+0.35,profit,width=0.35,color="b")
plt.title("US Stocks")
plt.legend(["Revenue","Profit"])
plt.show()