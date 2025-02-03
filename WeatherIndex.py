# Fit polynomial regression model
resultsP = sm.OLS.from_formula("FFMC ~ humid + humid_squared", data=forests).fit()
print(resultsP.summary())

#plot regression lines

humid_values = np.array([25, 35, 60, 70])
predicted_FFMC = resultsP.predict(pd.DataFrame({"humid": humid_values, "humid_squared": humid_values ** 2}))
print(predicted_FFMC)

#plot FFMC vs temperature
results_multi_FFMC = sm.OLS.from_formula("FFMC ~ temp + humid + wind + rain", data=forests).fit()
print(results_multi_FFMC.summary())


#model predicting FFMC with interaction
results_FWI = sm.OLS.from_formula("FWI ~ ISI + BUI", data=forests).fit()
print(results_FWI.summary())
