# ====================================
# Final Project
# Data Cleaning
# Physical Activity vs BMI Percentile
# ====================================

import pandas as pd

# 1. Read dataset
df = pd.read_csv("cleaned_YRBS_2007.csv")

# 2. Check columns
print(df.columns)

# ------------------------------------
# 3. Keep variables
# ------------------------------------

df_clean = df[['PhysicalActivity5OrMoreDays', 'BMIPCT']]

# ------------------------------------
# 4. Remove missing values
# ------------------------------------

df_clean = df_clean.dropna()

print("After removing missing values:")
print(df_clean.shape)

# ------------------------------------
# 5. Recode physical activity
# ------------------------------------

activity_map = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7
}

df_clean['ExerciseDays'] = (
    df_clean['PhysicalActivity5OrMoreDays']
    .map(activity_map)
)

# ------------------------------------
# 6. Remove invalid values
# ------------------------------------

df_clean = df_clean.dropna(subset=['ExerciseDays'])

# ------------------------------------
# 7. Keep final variables
# ------------------------------------

df_clean = df_clean[['ExerciseDays', 'BMIPCT']]

# Rename variable

df_clean.columns = [
    'ExerciseDays',
    'BMIPercentile'
]

# ------------------------------------
# 8. Check cleaned data
# ------------------------------------

print("\nData Information")
print(df_clean.info())

print("\nSummary Statistics")
print(df_clean.describe())

print("\nFirst 5 Rows")
print(df_clean.head())

# ------------------------------------
# 9. Save cleaned data
# ------------------------------------

df_clean.to_csv(
    "PhysicalActivity_BMI_Cleaned.csv",
    index=False
)

print("\nCleaning completed successfully.")
print("File saved as:")
print("PhysicalActivity_BMI_Cleaned.csv")