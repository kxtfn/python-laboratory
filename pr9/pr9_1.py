import pandas as pd # библиотека для работы с данными

try:
    df = pd.read_csv(r'C:\Users\evil\Desktop\sumdu\python-laboratory\pr9\API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_130173.csv', skiprows=4)
except Exception as e:
    print(f"Помилка відкриття файлу: {e}")
    exit()

countries = ['USA', 'UKR']
years = [str(year) for year in range(2010, 2020)]

filtered_df = df[df['Country Code'].isin(countries)][['Country Name', 'Country Code'] + years]

print(filtered_df)

filtered_df_pivot = filtered_df.set_index('Country Code')
comparison = filtered_df_pivot.loc['USA', years] - filtered_df_pivot.loc['UKR', years]
comparison = comparison.reset_index()
comparison.columns = ['Year', 'Inflation difference USA - UKR']

filtered_df.to_csv('inflation_USA_UKR_2010_2019.csv', index=False)
comparison.to_csv('inflation_comparison_USA_UKR_2010_2019.csv', index=False)
