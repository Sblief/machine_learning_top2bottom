# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:59:54 2018

@author: Ashfak Md. Shibli
"""

# Regression Template

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values # Is a matrix
y = dataset.iloc[:,2].values  #is a vector

"""
#splitting dataset into training and test data set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train) """


# Fitting Regression Model to the dataset
# Create a regressor

# Predicting a new result with Regression
y_pred = regressor.predict((6.5))

# Visualizing the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff ( Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualizing the Regression results in higher resolution and smother curve
X_grid = np.arrange(min(X), max(X), 0.1 )
X_grid = X_grid.reshape((len(X_grid)), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff ( Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()




