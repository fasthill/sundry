import pandas as pd
import numpy as np


df_public = pd.read_csv('survey_results_public.csv')
df_schema = pd.read_csv('survey_results_schema.csv')

country_grp = df_public.groupby(by='Country')

filt = df_public['Country'] == 'South Korea'
df_public[filt]['SocialMedia'].value_counts()
print(df_public[filt])
