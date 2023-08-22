import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('/workspaces/flask_SBP/blood_pressure_age.csv')


data = data.drop('Id',axis=1)
# print(data.head())

X = data['Age']
y = data['SBP']
# print(X)
model = LinearRegression()
model.fit(X.values.reshape(-1, 1),y)

print(model.predict([[60]]))

pickle.dump(model, open('model.pkl', 'wb'))