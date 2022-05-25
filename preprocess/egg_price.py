import sxtwl, pandas, json

INPUT_FILE = 'data/egg_price_raw.json'
OUTPUT_FILE = 'data/EGG_PRICE.csv'

def getLunarDate(row):
    year, month, date = row.日期[0:4], row.日期[5:7], row.日期[8:10]
    day = sxtwl.fromSolar(int(year), int(month), int(date))
    return f'{str(day.getLunarMonth()).zfill(2)}{str(day.getLunarDay()).zfill(2)}'

f = open(INPUT_FILE, encoding="utf-8")
dataFromJson = json.load(f)
df = pandas.json_normalize(dataFromJson)

df = df.rename({'白肉雞(2.0Kg以上)': 'white_broiler_big', '白肉雞(1.75-1.95Kg)': 'white_broiler_mid', '白肉雞(門市價高屏)': 'white_broiler_retail', '雞蛋(產地)': 'egg_price'}, axis=1)
df['month'] = df.apply(lambda row: f'{row.日期[0:4]}{row.日期[5:7]}', axis=1)
df['date'] = df.apply(lambda row: f'{row.日期[8:10]}', axis=1)
df['lunar_date'] = df.apply(lambda row: getLunarDate(row), axis=1)
df.drop(['日期' ,'農曆'], axis=1, inplace=True)
df = df[['month', 'date', 'lunar_date', 'white_broiler_big', 'white_broiler_mid', 'white_broiler_retail', 'egg_price']]
df.to_csv(OUTPUT_FILE, index=False)