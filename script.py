import numpy as np
from matplotlib import pyplot as plt
import random
import pandas as py 
import io
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

ds = py.read_csv('kag_risk_factors_cervical_cancer.csv')


print(ds.iloc[:])

r = np.random.random(32)
# print(r)

x_sample = np.random.randint(0,2,(1,32))
print(x_sample)

df = np.zeros((10, 5))
print(df)