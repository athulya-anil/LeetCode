# Last updated: 12/07/2026, 14:34:10
employees['bonus'] = ((employees['employee_id'] % 2) & (employees['name'].str[0] != 'M')) * employees['salary']
return employees[['employee_id', 'bonus']].sort_values('employee_id')