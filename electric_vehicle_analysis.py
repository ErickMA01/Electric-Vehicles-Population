# data processing
import pandas as pd
import numpy as np
# visualization
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
print(df.shape)

# print(df.head(2))

# print(df.head(2).T)

# print(df.tail(2))

print(df.dtypes)

# print(df.Make.unique())

# print(df.Make.nunique())

# print(df.describe())

# df = df.drop(columns=["Clean Alternative Fuel Vehicle (CAFV) Eligibility", "Legislative District",
# "DOL Vehicle ID", "Vehicle Location", "Electric Utility", "2020 Census Tract", "Electric Vehicle Type"])
# print(df.head(4).T)

# print(df.shape)

df = df.rename(columns={"2020 Census Tract": "Census", "Vehicle Location": "Location", "Electric Utility": "Utility", "DOL Vehicle ID": "DVID", "Legislative District": "District", "VIN (1-10)": "VIN", "Model Year": "Year", "Postal Code": "Zip", "Base MSRP": "MRSP", "Electric Range": "Range"})
# print(df.head(2).T)

# print(df[df.duplicated()].shape)

# duplicate_rows_df = df[df.duplicated()]

# df_no_duplicates = df.drop_duplicates()

# print(df.shape, df_no_duplicates.shape)


print(df[df.isna().any(axis=1)].shape)

print(df[~df.isna().any(axis=1)].shape)


print(df.Year.mode())

print(df.Year.mean())

df.fillna({"County": "N/A"}, inplace=True)
print(df[df.isna().any(axis=1)].head(2).T)

df.fillna({"City": "Missing"}, inplace=True)

df.fillna({"Zip": 0}, inplace=True)

df.fillna({"District": "Missing"}, inplace=True)

df.fillna({"Location": "Missing"}, inplace=True)

df.fillna({"Utility": "Missing"}, inplace=True)

df.fillna({"Census": "Missing"}, inplace=True)

print(df.isnull().sum())

print(df.shape)

# Boxplot
sns.boxplot(x=df["Range"])
plt.xlabel("Range")
plt.show()

sns.boxplot(x=df["Year"])
plt.xlabel("Year")
plt.show()

sns.boxplot(x=df["MRSP"])
plt.xlabel("MRSP")
plt.show()

df.Make.value_counts().nlargest(20).plot(kind="bar", figsize=(10, 6))
plt.title("Count of EV Cars by Make")
plt.xlabel("Car Makes")
plt.ylabel("Counts")
plt.show()

# Heatmap
plt.figure(figsize=(6, 6))
c = df[["Zip", "Year", "Range", "MRSP"]].corr()
sns.heatmap(c, cmap="BrBG", annot=True)
plt.show()

# Scatterplot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['Year'], df["Range"])
ax.set_xlabel('Year')
ax.set_ylabel('Range')
plt.show()






