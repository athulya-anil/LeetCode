# Last updated: 13/07/2026, 17:23:08
df = employees.groupby(['event_day','emp_id']).apply(

    lambda x: sum(x['out_time'] - x['in_time'])


).reset_index()

df.columns = ['day','emp_id', 'total_time']

return df