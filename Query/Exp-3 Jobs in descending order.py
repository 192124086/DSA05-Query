import pandas as pd
file_path = 'job.csv'
jobs = pd.read_csv(file_path)
sorted_jobs=jobs.sort_values(by='JOB_TITLE',ascending=False)
print("Details of Jobs in descending sequence on job title")
print(sorted_jobs)
