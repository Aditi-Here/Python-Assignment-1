import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# Problem 1
"""
1. Some values in the the FlightNumber column are missing. These numbers are
meant to increase by 10 with each row so 10055 and 10075 need to be put in
place. Fill in these missing numbers and make the column an integer column
(instead of a float column).
"""
# df_1=df
# df_1['FlightNumber']=df_1['FlightNumber']+10
# df_1['FlightNumber'].fillna(10,inplace=True)
# df_1['FlightNumber']=df_1['FlightNumber'].astype(int)
# print(df_1)

# Problem 2
"""
2. The From_To column would be better as two separate columns! Split each
string on the underscore delimiter _ to give a new temporary DataFrame with
the correct values. Assign the correct column names to this temporary
DataFrame.
"""
df_2=pd.DataFrame()
df_2[['From','To']]=df['From_To'].str.split("_",1,expand=True)
# print(df_2)

# Problem 3
"""
3. Notice how the capitalisation of the city names is all mixed up in this
temporary DataFrame. Standardise the strings so that only the first letter is
uppercase (e.g. "londON" should become "London".)
"""
df_3=pd.DataFrame()
df_3['From']=df_2['From'].str.capitalize()
df_3['To']=df_2['To'].str.capitalize()
# print(df_3)

# Problem 4
"""
4. Delete the From_To column from df and attach the temporary DataFrame
from the previous questions.
"""
df_4=df
del df_4['From_To']
df_4=df_3.join(df_4)
print(df_4)

# Problem 5
"""
5. In the RecentDelays column, the values have been entered into the
DataFrame as a list. We would like each first value in its own column, each
second value in its own column, and so on. If there isn't an Nth value, the value
should be NaN.
Expand the Series of lists into a DataFrame named delays, rename the columns
delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
with delays.
"""
df_5=pd.DataFrame()

for i in range(len(df['RecentDelays'])):
    for j in range(len(df['RecentDelays'][i])):
        print(df['RecentDelays'][i][j])
