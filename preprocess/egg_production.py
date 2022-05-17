import pandas

INPUT_FILE = 'data/egg_production_raw.csv'
OUTPUT_FILE = 'data/EGG_PRODUCTION.csv'

columns = ['年','月','入中雞雛數','產蛋隻數','均日產蛋箱數','年產蛋數','淘汰隻數','目前換羽隻數']
df = pandas.read_csv(INPUT_FILE, encoding='utf-8', keep_default_na=False, usecols=columns)
df['month'] = df.apply(lambda row: f'{row.年}{str(row.月).zfill(2)}', axis=1)
df.drop(['年' ,'月'], axis=1, inplace=True)
df = df[['month', '入中雞雛數', '產蛋隻數', '均日產蛋箱數', '年產蛋數', '淘汰隻數', '目前換羽隻數']]
df.to_csv(OUTPUT_FILE, index=False)