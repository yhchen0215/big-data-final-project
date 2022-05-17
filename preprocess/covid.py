import pandas

INPUT_FILE = 'data/covid_raw.csv'
OUTPUT_FILE = 'data/COVID.csv'

def getMonth(row):
    year, month, date = row.date.split('-')
    return f'{year}{month.zfill(2)}'

def getDate(row):
    year, month, date = row.date.split('-')
    return f'{date.zfill(2)}'

columns = ['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'positive_rate']
df = pandas.read_csv(INPUT_FILE, encoding='utf-8', keep_default_na=False, usecols=columns)
df = df.loc[df['location'] == 'Taiwan']
df['month'] = df.apply(lambda row: getMonth(row), axis=1)
df['date'] = df.apply(lambda row: getDate(row), axis=1)
df.drop(['location'], axis=1, inplace=True)
df = df[['month', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'positive_rate']]
df.to_csv(OUTPUT_FILE, index=False)