import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import codecademylib3

#load data
forests = pd.read_csv('forests.csv')

#check multicollinearity with a heatmap

# Create correlation matrix
corr_grid = forests.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_grid, annot=True, cmap="coolwarm", xticklabels=corr_grid.columns, yticklabels=corr_grid.columns)
plt.title("Correlation Heatmap")
plt.show()
plt.clf()


# Scatter plot of humidity vs temperature colored by region
sns.scatterplot(data=forests, x="temp", y="humid", hue="region")
plt.title("Humidity vs Temperature by Region")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.show()
plt.clf()
