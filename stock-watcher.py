import requests
import pandas as pd
import os
import csv
from dotenv import load_dotenv

load_dotenv()

VANTAGE_API_KEY = os.getenv("VANTAGE_API_KEY")

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey={VANTAGE_API_KEY}'
r = requests.get(url)
data = r.json()

def get_valid_year():
    while True:
        user_input = input("Enter a year (e.g., 2011): ")
        if user_input.isdigit() and len(user_input) == 4:
            year = int(user_input)
            if 2000 <= year <= 2024:
                return year
            else:
                print("Year out of range. Please enter a year between 2000 and 2024.")
        else:
            print("Invalid input. Please enter a valid year.")

year = get_valid_year()

def get_year_and_week(year):
    weekly_data = data['Weekly Time Series']
    df = pd.DataFrame.from_dict(weekly_data, orient='index')
    df.index = pd.to_datetime(df.index)
    only_year = df[df.index.year == year]
    return only_year

file_name = f'TSLA-weekly-{year}.csv'
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date', '1. open', '2. high', '3. low', '4. close', '5. volume'])
    year_data = get_year_and_week(year)
    for index, row in year_data.iterrows():
        writer.writerow([index.strftime('%Y-%m-%d'), row['1. open'], row['2. high'], row['3. low'], row['4. close'], row['5. volume']])

def print_stats(year_data):
    highest_open = year_data['1. open'].astype(float).max()
    lowest_open = year_data['1. open'].astype(float).min()
    print(f'Highest open in {year_data.index.year[0]}: {highest_open}')
    print(f'Lowest open in {year_data.index.year[0]}: {lowest_open}')
    print('------------------------------')
    highest_close = year_data['4. close'].astype(float).max()
    lowest_close = year_data['4. close'].astype(float).min()
    print(f'Highest close in {year_data.index.year[0]}: {highest_close}')
    print(f'Lowest close in {year_data.index.year[0]}: {lowest_close}')
    print('------------------------------')
    highest_volume = year_data['5. volume'].astype(float).max()
    lowest_volume = year_data['5. volume'].astype(float).min()
    print(f'Highest volume in {year_data.index.year[0]}: {highest_volume}')
    print(f'Lowest volume in {year_data.index.year[0]}: {lowest_volume}')
    print('------------------------------')
    average_open = year_data['1. open'].astype(float).mean()
    average_close = year_data['4. close'].astype(float).mean()
    average_volume = year_data['5. volume'].astype(float).mean()
    print(f'Average open in {year_data.index.year[0]}: {average_open}')
    print(f'Average close in {year_data.index.year[0]}: {average_close}')
    print(f'Average volume in {year_data.index.year[0]}: {average_volume}')

print_stats(year_data)
