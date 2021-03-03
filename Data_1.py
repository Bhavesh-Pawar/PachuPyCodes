import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[4,8,6,6,7,5,9]
plt.xlabel("Day")
plt.ylabel("Scores")
plt.title("Performance")
# key-value pair
# plt.plot(x,y,"r*",linestyle="dotted",fontsize=15)

# format string :- order does not matter 
plt.plot(x,y,"b<--",markersize=15,alpha=0.36)

# alpha property is used for tranparency
plt.show()