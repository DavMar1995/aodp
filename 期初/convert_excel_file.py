from os import name
import pandas as pd
def xlsx_to_csv_pd(fileName):
    data_xls = pd.read_excel(f'{fileName}.xlsx', index_col=0)
    data_xls.to_csv(f'{fileName}.csv', encoding='utf-8')
    print(f'convert {fileName}.xlsx to {fileName}.csv')


# fileName =ministryet'
xlsx_to_csv_pd(fileName)