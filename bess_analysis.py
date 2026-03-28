import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv("bess_dataset.csv")

print(df.columns)
print(df.head())

# calculate RTE
df["RTE"] = (df["Energy_Out_kWh"] / df["Energy_In_kWh"]) * 100

# RTE graph
plt.figure()
plt.plot(df["Day"], df["RTE"])
plt.title("Round Trip Efficiency")
plt.xlabel("Day")
plt.ylabel("Efficiency %")
plt.show()

# temperature graph
plt.figure(figsize=(8,5))
sns.lineplot(x="Day", y="Temperature_C", data=df)

plt.title("Battery Temperature Over Time")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.show()
#Peak Shaving and Cost Savings
price_per_kwh = 8  # ₹8 per kWh
# Cost savings
df["Cost_Savings"] = df["Peak_Shaved_kW"] * price_per_kwh
print("\nPeak Shaving & Cost Savings (first 5 days):")
print(df[["Day","Peak_Shaved_kW","Cost_Savings"]])
# Peak Shaving Graph
plt.figure(figsize=(10,5))
sns.barplot(x="Day", y="Peak_Shaved_kW", data=df, color='green')
plt.title("Peak Shaving Impact Over Days")
plt.xlabel("Day")
plt.ylabel("Power Reduced (kW)")
plt.grid(True)
plt.show()

# Cost Savings Graph
plt.figure(figsize=(10,5))
sns.lineplot(x="Day", y="Cost_Savings", data=df, marker='o', color='purple')
plt.title("Daily Cost Savings Due to Peak Shaving")
plt.xlabel("Day")
plt.ylabel("Savings ₹")
plt.grid(True)
plt.show()

print("\n BESS Project Analysis Complete!")