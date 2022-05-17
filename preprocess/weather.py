import pandas

INPUT_FILE = 'data/72G600_weather_raw.csv'
OUTPUT_FILE = 'data/72G600_WEATHER.csv'

def getMonth(row):
    year, month, date = row.觀測時間.split('/')
    return f'{year}{month.zfill(2)}'

def getDate(row):
    year, month, date = row.觀測時間.split('/')
    return f'{date.zfill(2)}'

df = pandas.read_csv(INPUT_FILE, encoding='utf-8', keep_default_na=False)
df = df.rename({'平均氣溫(℃)': 'avg_temperature', '最高氣溫(℃)': 'max_temperature', '最低氣溫(℃)': 'min_temperature', '累計雨量(mm)': 'rainfall', '累積日照時數(hr)': 'sunshine'}, axis=1)
df['month'] = df.apply(lambda row: getMonth(row), axis=1)
df['date'] = df.apply(lambda row: getDate(row), axis=1)
df.drop(['測站代碼' ,'觀測時間'], axis=1, inplace=True)
df = df[['month', 'date', 'avg_temperature', 'max_temperature', 'min_temperature', 'rainfall', 'sunshine']]
df.to_csv(OUTPUT_FILE, index=False)