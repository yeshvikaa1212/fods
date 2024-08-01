import pandas as pd

# Sample employee dataset (replace this with your actual dataset)
data = {
    'Employee ID': [1, 2, 3, 4, 5, 6],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 70000, 55000, 65000, 75000],
    'Joining Date': ['2010-01-15', '2012-05-23', '2013-11-10', '2011-03-29', '2014-07-19', '2015-09-01']
}

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Convert the 'Joining Date' column to datetime
df['Joining Date'] = pd.to_datetime(df['Joining Date'])

# Determine the highest and lowest salaries in each department
salary_stats = df.groupby('Department')['Salary'].agg(['max', 'min']).reset_index()
print("Highest and lowest salaries in each department:")
print(salary_stats)

# Calculate the average tenure of employees in the company
# Assuming today's date for tenure calculation
today = pd.Timestamp('2024-07-22')
df['Tenure'] = (today - df['Joining Date']).dt.days / 365.25  # Convert days to years
average_tenure = df['Tenure'].mean()
print(f"\nAverage tenure of employees in the company: {average_tenure:.2f} years")

# Identify employees who joined before a specific date
specific_date = pd.Timestamp('2013-01-01')
employees_before_date = df[df['Joining Date'] < specific_date]
print("\nEmployees who joined before 2013-01-01:")
print(employees_before_date)
