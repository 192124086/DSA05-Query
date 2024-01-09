import pandas as pd
file_path = 'EMPLOYEES.csv'
employees = pd.read_csv(file_path)
distinct_department_ids = employees['DEPARTMENT_ID'].unique()
print("Distinct Department IDs:")
print(distinct_department_ids)
