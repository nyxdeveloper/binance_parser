import requests
import gspread

import datetime

gc = gspread.service_account(filename='binancecourse-2a726ff4c777.json')
sh = gc.open("Курс BTC")
worksheet = sh.sheet1

license = datetime.date(2022, 6, 1)


def main():
    while not datetime.datetime.now().date() > license:
        try:
            course_btc_usd = requests.get(url='https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()[
                'price']
            course_usd_rub = requests.get(url='https://www.binance.com/api/v3/ticker/price?symbol=USDTRUB').json()[
                'price']
            course_btc_rub = requests.get(url='https://www.binance.com/api/v3/ticker/price?symbol=BTCRUB').json()[
                'price']

            usd_rub = round(float(course_usd_rub), 2)
            btc_rub = round(float(course_btc_rub), 2)
            btc_usd = round(float(course_btc_usd), 2)

            cell_list = worksheet.range('A28:C28')
            cell_values = [btc_usd, btc_rub, usd_rub]

            for i, val in enumerate(cell_values):
                cell_list[i].value = val

            worksheet.update_cells(cell_list)

            print('usd_rub: ', usd_rub, '\t', 'btc_rub: ', btc_rub, '\t', 'btc_usd: ', btc_usd, '\n')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
