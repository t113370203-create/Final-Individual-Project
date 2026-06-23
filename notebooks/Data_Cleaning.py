# ====================================
# Final Project
# Data Cleaning
# Physical Activity vs BMI Percentile
# ====================================

import pandas as pd

# 讀取原始資料
df = pd.read_csv("YRBS_2007.csv")

# -------------------------------
# 保留需要的欄位
# -------------------------------
df = df[["PhysicalActivity5OrMoreDays", "BMIPCT"]]

# -------------------------------
# 移除缺失值
# -------------------------------
df = df.dropna()

# -------------------------------
# BMI Percentile 篩選
# 保留 1~99
# -------------------------------
df = df[(df["BMIPCT"] >= 1) & (df["BMIPCT"] <= 99)]

# -------------------------------
# 將運動天數重新編碼
# 原始資料:
# 1=0天
# 2=1天
# ...
# 8=7天
# -------------------------------
df["ExerciseDays"] = df["PhysicalActivity5OrMoreDays"] - 1

# -------------------------------
# 只保留 0~7 天
# -------------------------------
df = df[(df["ExerciseDays"] >= 0) & (df["ExerciseDays"] <= 7)]

# -------------------------------
# 刪除原始欄位
# -------------------------------
df = df.drop(columns=["PhysicalActivity5OrMoreDays"])

# -------------------------------
# 顯示資料資訊
# -------------------------------
print("Number of observations:", len(df))
print(df.head())

# -------------------------------
# 儲存清理後資料
# -------------------------------
df.to_csv("cleaned_YRBS_2007.csv", index=False)

print("Data cleaning completed!")