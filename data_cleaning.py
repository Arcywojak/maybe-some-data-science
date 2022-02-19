import pandas as pd
from data_cleaning_helpers import (getMinSalary, getMaxSalary, 
DoesContractTypeExists, isTechnologyRequired,sumLevelsOfSkills)

df = pd.read_csv('frontend_raw_data.csv')
df.drop('Unnamed: 0', axis=1, inplace = True)

#Columns:
"""
'title', 'street', 'city', 'country_code', 'address_text',
'marker_icon', 'workplace_type', 'company_name', 'company_url',
'company_size', 'experience_level', 'latitude', 'longitude',
'published_at', 'remote_interview', 'id', 'employment_types',
'company_logo_url', 'skills', 'remote'
```
"""

# replace single quote with double to allow to convert to json format

df['employment_types'] = df['employment_types'].apply(lambda x: x.replace("'", '"'))
df['skills'] = df['skills'].apply(lambda x: x.replace("'", '"'))

#add, maybe useful, columns into df

df['min_salary'] = df['employment_types'].apply(getMinSalary)
df['max_salary'] = df['employment_types'].apply(getMaxSalary)
df['b2b'] = df['employment_types'].apply(lambda x: DoesContractTypeExists(x, 'b2b'))
df['permament'] = df['employment_types'].apply(lambda x: DoesContractTypeExists(x, 'permanent'))
df['mandate_contract'] = df['employment_types'].apply(lambda x: DoesContractTypeExists(x, 'mandate_contract'))
df['react'] = df.apply(lambda x: isTechnologyRequired(x['title'], x['skills'], 'react'), axis=1)
df['angular'] = df.apply(lambda x: isTechnologyRequired(x['title'], x['skills'], 'angular'), axis=1)
df['vue'] = df.apply(lambda x: isTechnologyRequired(x['title'], x['skills'], 'vue'), axis=1)
df['sum_of_skill_levels'] = df['skills'].apply(sumLevelsOfSkills)

df.to_csv('cleaned_frontend_data.csv')

