# IMPORTANT : pip install pandas numpy
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# output path
OUTPUT_PATH = "../sample/"

# -------------------------
# STORES
# -------------------------

cities = ["New York", "Chicago", "Dallas", "Seattle", "Boston"]
states = ["NY", "IL", "TX", "WA", "MA"]
regions = ["East", "Midwest", "South", "West"]

stores = []

for i in range(1, 21):

    store = {
        "store_id": i,
        "store_name": f"Store_{i}",
        "city": random.choice(cities),
        "state": random.choice(states),
        "region": random.choice(regions),
        "store_type": random.choice(["Urban","Suburban","Mall"]),
        "open_date": datetime(2015,1,1) + timedelta(days=random.randint(0,2000))
    }

    stores.append(store)

stores_df = pd.DataFrame(stores)

# -------------------------
# PRODUCTS
# -------------------------

categories = ["Healthcare","Personal Care","Vitamins","Pain Relief"]

products = []

for i in range(1,101):

    price = round(random.uniform(5,50),2)

    product = {
        "product_id": i,
        "product_name": f"Product_{i}",
        "brand": random.choice(["BrandA","BrandB","BrandC"]),
        "category": random.choice(categories),
        "sub_category": random.choice(["Tablet","Liquid","Capsule"]),
        "unit_cost": round(price * 0.6,2),
        "unit_price": price
    }

    products.append(product)

products_df = pd.DataFrame(products)

# -------------------------
# CALENDAR
# -------------------------

start = datetime(2022,1,1)
end = datetime(2024,12,31)

dates = []

d = start

while d <= end:

    dates.append({
        "date": d,
        "year": d.year,
        "month": d.month,
        "day": d.day,
        "week_of_year": d.isocalendar()[1],
        "day_name": d.strftime("%A"),
        "is_weekend": d.weekday() >= 5
    })

    d += timedelta(days=1)

calendar_df = pd.DataFrame(dates)

# -------------------------
# SALES
# -------------------------

transactions = []

transaction_id = 1

for i in range(50000):

    store = random.randint(1,20)
    product = random.randint(1,100)
    date = random.choice(calendar_df["date"])

    qty = random.randint(1,5)

    price = products_df.loc[
        products_df.product_id == product,"unit_price"
    ].values[0]

    discount = round(random.uniform(0,price*0.2),2)

    total = round((price * qty) - discount,2)

    transactions.append({
        "transaction_id": transaction_id,
        "transaction_date": date,
        "store_id": store,
        "product_id": product,
        "quantity": qty,
        "unit_price": price,
        "discount_amount": discount,
        "total_amount": total
    })

    transaction_id += 1

sales_df = pd.DataFrame(transactions)

# -------------------------
# WRITE FILES
# -------------------------

stores_df.to_csv(f"{OUTPUT_PATH}/stores.csv",index=False)
products_df.to_csv(f"{OUTPUT_PATH}/products.csv",index=False)
calendar_df.to_csv(f"{OUTPUT_PATH}/calendar.csv",index=False)
sales_df.to_csv(f"{OUTPUT_PATH}/sales_transactions.csv",index=False)

print("Data generated successfully")
