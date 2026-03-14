# Data Dictionary

## Stores

| Column | Description |
|------|-------------|
store_id | unique store identifier
store_name | name of store
city | store city
state | state
region | sales region
store_type | urban / suburban / mall
open_date | store opening date

## Products

| Column | Description |
|------|-------------|
product_id | product identifier
product_name | product name
brand | product brand
category | category
sub_category | sub category
unit_cost | cost price
unit_price | retail price

## Calendar

| Column | Description |
|------|-------------|
date | calendar date
year | year
month | month number
day | day of month
week_of_year | ISO week number
day_name | weekday
is_weekend | boolean

## Sales Transactions

| Column | Description |
|------|-------------|
transaction_id | unique transaction id
transaction_date | date of transaction
store_id | store where sale happened
product_id | sold product
quantity | quantity sold
unit_price | price per unit
discount_amount | applied discount
total_amount | final sales amount
