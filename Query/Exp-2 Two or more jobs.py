import pandas as pd
file_path = 'employee.csv'
employees_jobs = pd.read_csv(file_path)
employees_with_multiple_jobs = employees_jobs.groupby('EMPLOYEE_ID').filter(lambda x: len(x) >= 2)
print("Employees with Two or More Jobs:")
print(employees_with_multiple_jobs)
