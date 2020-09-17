import pandas as pd
import json

# * init


def getDataFrame():
    data = pd.read_excel('excel/2003_2020-06.xlsx')
    data.set_index(keys=['Year', 'Nationality'], inplace=True)

    # * clean data
    # data.index = data.index.str.title()

    for i in data.index.get_level_values('Nationality'):
        i = i.title()

    for i in data.index.get_level_values('Year'):
        i = pd.to_datetime(i, format='%Y')

    # for i in data.index.get_level_values('Time'):
    #     i = pd.to_datetime(i, format='%Y-%m')

    data['Total'] = data['Total'].str.replace(',', '')
    data['Total'] = data['Total'].astype(float)
    data['Total'] = pd.to_numeric(data['Total'])

    return data


def getKoreaData(data, start, end):
    global nation

    # * Group by year
    time = data.groupby(level=['Year', 'Nationality'])

    korea_data = {}

    for i in range(start, end+1):
        tmp = []
        for country, geo in nation.items():
            if country == 'South Korea':
                continue
            tmp.append({
                # 'year': i,
                'total': int(time.get_group((i, country.upper()))
                             ['Total'].sum()),
                'source': country,
                'target': 'South Korea',
                's_lat': geo[0],
                's_lng': geo[1],
                't_lat': nation.get('South Korea')[0],
                't_lng': nation.get('South Korea')[1],
            })
        korea_data[i] = tmp

    return korea_data


if __name__ == '__main__':
    start = 2019
    end = 2020
    nation = {
        'China': [39.905278, 116.398113],
        'Japan': [35.710073, 139.810702],
        'Taiwan': [25.033493, 121.564101],
        'Thailand': [13.744333, 100.540395],
        'South Korea': [37.540701, 126.992391],
    }

    df = getDataFrame()
    kData = getKoreaData(df, start, end)

    # print(kData)

    for year, data in kData.items():
        print(year)
        # print(json.dumps(data))
        with open(f'json/Korea_tourist_{year}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
