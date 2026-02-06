import pandas as pd
df=pd.read_csv('sales.csv')
df['total_sales']=df['Price']*df['Quantity']

print(df)
best_prod=df.loc[df['total_sales'].idxmax()]
print(best_prod)

df['price_with_tax']=df['Price']*1.10
print("final data :",df)