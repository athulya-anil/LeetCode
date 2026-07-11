# Last updated: 10/07/2026, 22:13:38
merged.rename(
    columns={
        'employee_id_y': 'employee_id',  # This is the actual manager's ID
    }, 
    inplace=True
)
final_output = merged[['employee_id', 'name', 'reports_count', 'average_age']]