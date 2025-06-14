# Problem 2 : The Number of Rich Customers ( https://leetcode.com/problems/the-number-of-rich-customers/ )

import pandas as pd

# using set
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount']>500]
    richCount = len(set(df['customer_id']))
    return pd.DataFrame([richCount], columns=['rich_count'])

# using nunique
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    richCount = store[store['amount']>500]['customer_id'].nunique()
    return pd.DataFrame([richCount], columns=['rich_count'])