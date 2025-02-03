#model predicting humidity
sns.lmplot(data=forests, x="temp", y="humid", hue="region")
plt.title("Regression Lines for Humidity vs Temperature by Region")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.show()
plt.clf()


#equations

resultsF = sm.OLS.from_formula("FFMC ~ temp * fire", data=forests).fit()
print(resultsF.summary())

#interpretations
## Coefficient on temp:
sns.lmplot(data=forests, x="temp", y="FFMC", hue="fire", ci=None)
plt.title("FFMC vs Temperature with Regression Lines")
plt.xlabel("Temperature (°C)")
plt.ylabel("FFMC")
plt.show()
plt.clf()

## For Bejaia equation:
sns.scatterplot(data=forests, x="humid", y="FFMC")
plt.title("FFMC vs Humidity")
plt.xlabel("Humidity (%)")
plt.ylabel("FFMC")
plt.show()
plt.clf()
