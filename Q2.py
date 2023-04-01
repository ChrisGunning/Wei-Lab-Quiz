import numpy as np
from sklearn.linear_model import LinearRegression

# independent features
x = []
# dependent features
y = []
# creating a txt file object
with open('dataset1.txt') as txtFile:
    for line in txtFile:
        f = line.split()
        x.append(f[1:])
        y.append(f[0])

x, y = np.array(x), np.array(y)

# create linear regression model and predict dependent variables
model = LinearRegression().fit(x, y)
y_pred = model.predict(x)

# Output
print('The predicted first columns of the sequence is as follows: ')
print(y_pred)
