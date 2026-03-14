# Source Data Model

The POS system produces transaction-level data representing sales at retail stores.

## Source Entities

Stores
Products
Calendar
Sales Transactions

## Relationship

Store (1) ---- (many) Sales Transactions

Product (1) ---- (many) Sales Transactions

Calendar (1) ---- (many) Sales Transactions

## Grain

Sales Transactions table grain:

One row per:

store_id
product_id
transaction_date
transaction_id
