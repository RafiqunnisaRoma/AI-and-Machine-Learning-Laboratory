#8.3 Linear Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

#Data
X=np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(-1,1)
y=np.array([35,40,45,50,55,60,65,70,75,80,85,90])
#Split train test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
#model Selection
model = LinearRegression()
model.fit(X_train,y_train)
#display slope ,c, r2
train_pred= model.predict (X_train)
test_pred= model.predict(X_test)

print('Slope: ',model.coef_[0])
print('Intercept: ',model.intercept_)
print('Train R2 : ',r2_score(y_train,train_pred))
print('Test R2 : ',r2_score(y_test,test_pred))
#Predit 2 unseen
new_X= np.array([13,14]).reshape(-1,1)
print('Predictions: ', model.predict(new_X))
#Plot
plt.scatter(X_train,y_train,label= "Trainning Data")
plt.scatter(X_test,y_test,label= "Testing Data",marker='x')
plt.plot(X,model.predict(X),label= "Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.show()
