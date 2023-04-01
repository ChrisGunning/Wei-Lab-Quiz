import matplotlib.pyplot as plt
  
# dum1 values
x = [1,2,1]
y = [2,-2,1]

# dim2 values
x1 = [1,2,-2,1]
y1 = [-2.5,2,1,1]
  
# plotting dim1
plt.scatter(x, y, color= "red", marker= ".", s=20,alpha=0.1)
plt.scatter(x, y, color= "red", marker= ".", s=20,alpha=0.1)

# plotting dim2
plt.scatter(y1, x1, color= "red", marker= ".", s=20, alpha=0.1)
plt.scatter(y1, x1, color= "red", marker= ".", s=20, alpha=0.1)
  
# naming axis
plt.xlabel('dim1')
plt.ylabel('dim2')

# setting x and y axis range
plt.ylim(-3,3)
plt.xlim(-3,3)
  
# function to show the plot
plt.show()