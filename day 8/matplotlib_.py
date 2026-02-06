import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.figure()
plt.barh(df["Product"], df["Price"])
plt.xlabel("Price")
plt.ylabel("Product")
plt.title("Product Price Comparison")

plt.show()
