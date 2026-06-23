import pandas as pd
import statsmodels.api as sm
df = pd.read_csv("PhysicalActivity_BMI_Cleaned.csv")
X = df["ExerciseDays"]
Y = df["BMIPercentile"]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())