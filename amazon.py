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
print("Сумма денег, потерянных на отменах:", (round(avg_cancel_amount))*(round(len(cancelled))))

lost_revenue = cancelled.groupby("category")["amount"].sum()
total_revenue = df.groupby("category")["amount"].sum()
lost_revenue_percent = (lost_revenue / total_revenue) * 100

print("\nПотерянная выручка по категориям (%):")
print(round(lost_revenue_percent).sort_values(ascending=False))

avg_cancel_by_category = cancelled.groupby("category")["amount"].mean()
print("\nСредний чек отменённых заказов:")
print(round(avg_cancel_by_category).sort_values(ascending=False))

analysis = pd.DataFrame({
    "total_orders": total_by_category,
    "cancelled_orders": cancel_by_category,
    "cancel_rate_percent": cancel_percent,
    "lost_revenue": lost_revenue
}).fillna(0)
print("\nПолная таблица анализа:")
print(analysis.sort_values("cancel_rate_percent", ascending=False))

analysis.to_excel("analysis.xlsx")

