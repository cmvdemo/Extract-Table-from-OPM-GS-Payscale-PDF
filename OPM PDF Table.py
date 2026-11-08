"""
@author: corina mccullough
"""

# Import packages
import pdfplumber
import pandas as pd

# Upload data
with pdfplumber.open('file path.pdf') as pdf:
    for p in pdf.pages:
        for dc_table in p.extract_tables():
            for r in dc_table:
                print(r)


# Convert to dataframe
pay_scale = pd.DataFrame(dc_table, 
                         columns=['Grade', 'Step 1', 'Step 2', 'Step 3',
                                  'Step 4', 'Step 5', 'Step 6', 'Step 7',
                                  'Step 8', 'Step 9', 'Step 10'])
print(pay_scale)

# Drop index
pay_scale = pay_scale.drop(index=0)

# Pivot table 
df_ps = pd.melt(pay_scale, 
                id_vars = 'Grade', 
                value_vars = ['Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5', 
                              'Step 6','Step 7', 'Step 8', 'Step 9', 'Step 10'])

# Rename columns
df_ps.rename(columns={'variable': 'Step', 'value': 'Salary'}, inplace=True)

# Remove extra characters, symbols, and spaces
df_ps['Salary'] = df_ps['Salary'].str.replace(('\$ |\|'), '',regex=True)
df_ps['Salary'] = df_ps['Salary'].str.replace(('\*|\|'), '',regex=True)
df_ps['Salary'] = df_ps['Salary'].str.replace(('\,|\|'), '',regex=True)
df_ps['Step'] = df_ps['Step'].str.replace(('\Step |\|'), '',regex=True)

# Convert data 
df_ps = df_ps.convert_dtypes()

df_ps['Grade'] = df_ps['Grade'].astype(int)
df_ps['Step'] = df_ps['Step'].astype(int)
df_ps['Salary'] = df_ps['Salary'].astype(int)

# Check data type
print(df_ps['Grade'].dtype)
print(df_ps['Step'].dtype)
print(df_ps['Salary'].dtype)

# Average salary by Grade
avg_salary = df_ps.groupby('Grade')['Salary'].mean()






