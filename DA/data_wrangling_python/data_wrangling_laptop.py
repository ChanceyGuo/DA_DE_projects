import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
df = pd.read_csv(file_path, header=0)

# Quick check
print(df.info())
print(df.head())

# Missing data
missing_data = df.isnull()
for column in missing_data.columns.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print()

# Fill missing values
df["Weight_kg"] = pd.to_numeric(df["Weight_kg"], errors="coerce")
df["Screen_Size_cm"] = pd.to_numeric(df["Screen_Size_cm"], errors="coerce")

df["Weight_kg"] = df["Weight_kg"].fillna(df["Weight_kg"].mean())
df["Screen_Size_cm"] = df["Screen_Size_cm"].fillna(df["Screen_Size_cm"].mode()[0])

# Fix data types
df[["Weight_kg", "Screen_Size_cm"]] = df[["Weight_kg", "Screen_Size_cm"]].astype(float)

# Standardization and normalization
df["Weight_pounds"] = df["Weight_kg"] * 2.205
df["Screen_Size_inch"] = df["Screen_Size_cm"] / 2.54
df["CPU_frequency"] = df["CPU_frequency"] / df["CPU_frequency"].max()

df.drop(columns=["Weight_kg", "Screen_Size_cm"], inplace=True)

# Binning
bins = np.linspace(df["Price"].min(), df["Price"].max(), 4)
group_names = ["Low", "Medium", "High"]

df["Price-binned"] = pd.cut(
    df["Price"],
    bins=bins,
    labels=group_names,
    include_lowest=True
)

price_counts = df["Price-binned"].value_counts().reindex(group_names)
plt.bar(group_names, price_counts)
plt.xlabel("Price Group")
plt.ylabel("Count")
plt.title("Price Bins")
plt.show()

# Dummy variables
screen_dummies = pd.get_dummies(df["Screen"])
screen_dummies = screen_dummies.rename(
    columns={
        "IPS Panel": "Screen-IPS_panel",
        "Full HD": "Screen-Full_HD"
    }
)

df = pd.concat([df, screen_dummies], axis=1)
df.drop(columns=["Screen"], inplace=True)

print(df.head())
