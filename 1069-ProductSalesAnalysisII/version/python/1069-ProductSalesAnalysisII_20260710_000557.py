# Last updated: 10/07/2026, 00:05:57
pd = sales.groupby(['product_id'], as_index = False)['quantity'].sum().rename(columns = {'quantity': 'total_quantity'})