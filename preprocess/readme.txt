- 先提取當時投影片有提到的欄位為主
- 還沒修正資料缺失的部分，目前還是空著或是(蛋價會寫休市)，但是確定日期沒有缺失
- 檔案名全大寫的代表處理過的
- 共同欄位:
    - month: xxxxxx ex.202103 (所以大家都會是這樣的六位數)
    - date: xx ex.03 (有些只有月資料的就沒有這個欄位)

EGG_PRICE:
    month | date | lunar_date | white_broiler_big | white_broiler_mid | white_broiler_retail | egg_price

    另外計算農曆日期(xxxx ex.1129)，原本的表示方法不好使用或有錯
    日期缺失: 20130401已補上
    資料刪除: 201010的資料只有10天左右且不連續，所以排除掉
    區間: 20101101-20220520

WEED_PRICE:
    month | corn_price | rice_price | bran_price | soy_price | fish_meal_price | chicken_feed_price

    重新下載一份比較完整好整理的檔案
    區間: 198101-202202
    新資料來源: http://price.naif.org.tw/

EGG_PRODUCTION:
    month | 入中雞雛數 | 產蛋隻數 | 均日產蛋箱數 | 年產蛋數 | 淘汰隻數 | 目前換羽隻數

    重新下載一份比較完整的檔案(到2022)
    區間: 201101-202203

WEATHER:
    month | date | avg_temperature | max_temperature | min_temperature | rainfall | sunshine

    區間: 20000101-20220520

AVIAN_INFLUENZA:
    month | amount

    區間: 201501-202204

COVID:
    month | date | total_cases | new_cases | total_deaths | new_deaths | positive_rate

    區間: 20200116-20220313
