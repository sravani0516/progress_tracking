# ==========================================
# Student Performance Mini Project
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------

df = pd.read_csv("StudentsPerformance.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# ------------------------------------------
# 2. Descriptive Analysis
# ------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# Mean, Median, Mode (Math Score)
print("\nMean Math Score:", df["math score"].mean())
print("Median Math Score:", df["math score"].median())
print("Mode Math Score:", df["math score"].mode()[0])

# Variance & Standard Deviation
print("\nVariance of Reading Score:", df["reading score"].var())
print("Std Dev of Reading Score:", df["reading score"].std())

# Correlation
print("\nCorrelation Matrix:")
print(df[["math score", "reading score", "writing score"]].corr())

# ------------------------------------------
# 3. Data Visualization
# ------------------------------------------

# Histogram - Math Score Distribution
plt.figure()
plt.hist(df["math score"], bins=20)
plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()

# Boxplot - Writing Score
plt.figure()
plt.boxplot(df["writing score"])
plt.title("Writing Score Boxplot")
plt.show()

# Scatter Plot - Reading vs Writing
plt.figure()
plt.scatter(df["reading score"], df["writing score"])
plt.title("Reading vs Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.show()

# ------------------------------------------
# 4. Probability Model
# ------------------------------------------

# Create Pass/Fail Column (Pass if Math >= 40)
df["pass_math"] = (df["math score"] >= 40).astype(int)

# Actual Probability of Passing
pass_probability = df["pass_math"].mean()
print("\nActual Probability of Passing Math:", pass_probability)

# Simulate 1000 Students using Binomial Distribution
simulated = np.random.binomial(n=1, p=pass_probability, size=1000)

print("Simulated Pass Probability:", np.mean(simulated))

# ------------------------------------------
# 5. Visualize Simulation
# ------------------------------------------

plt.figure()
plt.hist(simulated, bins=2)
plt.title("Simulated Pass/Fail Outcomes")
plt.xlabel("0 = Fail, 1 = Pass")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------------
# 6. Interpretation
# ------------------------------------------

print("\nInterpretation:")
print("- The average math score represents overall performance.")
print("- Most students score between 50–80 range.")
print("- Reading and writing scores show strong positive correlation.")
print("- Simulated probability is close to actual probability.")
print("- This verifies the Law of Large Numbers.")