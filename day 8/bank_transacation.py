# task:

# bank tarnsaction analysis 

# track diposit and with drawals
# calculate final balance
# detect high value transactions


import pandas as pd

data = {
    "Transaction_ID": [101, 102, 103, 104],
    "Type": ["Deposit", "Withdrawal", "Deposit", "Withdrawal"],
    "Amount": [5000, 2000, 12000, 3000]
}

df = pd.DataFrame(data)

print("Transaction Dataset:")
print(df)

total_deposit = df[df["Type"] == "Deposit"]["Amount"].sum()
total_withdrawal = df[df["Type"] == "Withdrawal"]["Amount"].sum()

print("\nTotal Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)

final_balance = total_deposit - total_withdrawal
print("\nFinal Balance:", final_balance)

high_value_txns = df[df["Amount"] > 10000]

print("\nHigh Value Transactions:")
print(high_value_txns)
