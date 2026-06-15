import pandas as pd

# 讀取清理好的資料
df = pd.read_csv("PhysicalActivity_BMI_Cleaned.csv")

# 建立 Summary Table
summary = pd.DataFrame({
    "Measure": [
        "Sample Size",
        "Mean Exercise Days",
        "Mean BMI Percentile",
        "SD BMI Percentile",
        "Min BMI Percentile",
        "Max BMI Percentile"
    ],
    "Value": [
        len(df),
        round(df["ExerciseDays"].mean(), 2),
        round(df["BMIPercentile"].mean(), 2),
        round(df["BMIPercentile"].std(), 2),
        df["BMIPercentile"].min(),
        df["BMIPercentile"].max()
    ]
})

# 存成 CSV
summary.to_csv("summary_table.csv", index=False)

print(summary)