import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/palaa/OneDrive/Desktop/whitehat/python/c132/pro/stars.csv")
mass = df["Mass"].tolist()
gravity = df["Gravity"].tolist()

X = np.reshape(mass, (len(mass), 1))
Y = np.reshape(gravity, (len(gravity), 1))

sizes = np.random.uniform(15, 80, len(X))
colors = np.random.uniform(15, 80, len(X))

fig, ax = plt.subplots()
ax.scatter(X, Y, s=sizes, c=colors, vmin=0, vmax=100)

plt.ylabel('Y')
plt.xlabel('X')
plt.show()
