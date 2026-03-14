# Warehouse Schema

## DimDate

date_key
date
year
month
day
week_of_year
day_name
is_weekend

## DimStore

store_key
store_id
store_name
city
state
region
store_type
open_date

## DimProduct

product_key
product_id
product_name
brand
category
sub_category
unit_cost
unit_price

## FactSales

sales_key
date_key
store_key
product_key
transaction_id
quantity
unit_price
discount_amount
total_amount
