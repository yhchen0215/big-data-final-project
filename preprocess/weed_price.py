import pandas

INPUT_FILE = 'data/weed_price_raw.csv'
OUTPUT_FILE = 'data/WEED_PRICE.csv'

def getMonth(row):
    year, month = str(int(row.年[:-1])+1911), str(row.月[:-1])
    return f'{year}{month.zfill(2)}'

df = pandas.read_csv(INPUT_FILE, encoding='utf-8', keep_default_na=False)
df = df.rename({'玉米粒(進口-產業協會)': 'corn_price', '米糠(國產-產業協會)': 'rice_price', '麩皮(白-產業協會)': 'bran_price', '黃豆粉(進口-產業協會)': 'soy_price', '魚粉(進口貨)': 'fish_meal_price', '蛋雞飼料': 'chicken_feed_price'}, axis=1)
df['month'] = df.apply(lambda row: getMonth(row), axis=1)
df.drop(['年' ,'月'], axis=1, inplace=True)
df = df[['month', 'corn_price', 'rice_price', 'bran_price', 'soy_price', 'fish_meal_price', 'chicken_feed_price']]
df.to_csv(OUTPUT_FILE, index=False)