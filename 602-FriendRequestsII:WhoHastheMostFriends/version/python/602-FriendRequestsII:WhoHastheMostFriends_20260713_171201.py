# Last updated: 13/07/2026, 17:12:01
df = values.groupby('id', as_index=False).agg(num=('id', 'count')).sort_values('num', ascending=False).head(1)