import pandas as pd
import matplotlib.pyplot as plt

file_path = 'API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_130173.csv'
df = pd.read_csv(file_path, skiprows=4)

indicator_name = 'Inflation, consumer prices (annual %)'
countries = ['Ukraine', 'United States']
years = list(map(str, range(2004, 2024)))
filtered_df = df[(df['Country Name'].isin(countries)) & (df['Indicator Name'] == indicator_name)][['Country Name'] + years]

ukraine_df = filtered_df[filtered_df['Country Name'] == 'Ukraine'][years].T # транспонування 
ukraine_df.columns = ['Ukraine']

usa_df = filtered_df[filtered_df['Country Name'] == 'United States'][years].T
usa_df.columns = ['USA']

data = pd.concat([ukraine_df, usa_df], axis=1)
data.index = data.index.astype(int)

def plot_line_chart(): # лінійний графік
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Ukraine'], label='Ukraine', color='blue')
    plt.plot(data.index, data['USA'], label='USA', color='red')
    plt.title('Inflation, consumer prices (annual %) in Ukraine and USA (2004-2023)')
    plt.xlabel('Year')
    plt.ylabel('Inflation, %')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_bar_chart(country_name): # стовпчик графік
    if country_name not in ['Ukraine', 'USA']:
        print('Country not supported.')
        return
    plt.figure(figsize=(12,6))
    plt.bar(data.index, data[country_name], color='green')
    plt.title(f'Inflation, consumer prices (annual %) in {country_name} (2004-2023)')
    plt.xlabel('Year')
    plt.ylabel('Inflation, %')
    plt.grid(True)
    plt.show()

plot_line_chart()
plot_bar_chart('Ukraine')



