import pandas as pd

df = pd.read_csv("amazon.csv", sep=";")
print(df["status"].value_counts())

cancelled = len(df[df["status"] == "Cancelled"])
total = len(df)
percent = cancelled / total * 100
print("Процент отмен:", round((percent), 2))

cancel_by_category = df[df["status"] == "Cancelled"]["category"].value_counts()
print(cancel_by_category)

cancelled = df[df["status"] == "Cancelled"]
total_by_category = df["category"].value_counts()
cancel_by_category = cancelled["category"].value_counts()
cancel_percent = round(((cancel_by_category / total_by_category) * 100), 2)
print("Процент отмен по категориям:")
print(cancel_percent.sort_values(ascending=False))
avg_cancel_amount = cancelled["amount"].astype(float).mean()

print("Средняя сумма отменённого заказа:", round(avg_cancel_amount))
print("Всего заказов:", round(len(df)))
print("Всего отмен:", round(len(cancelled)))
print("Категория с самым высоким процентом отмен:")
print(cancel_percent.idxmax())
