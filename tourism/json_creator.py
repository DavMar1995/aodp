import pandas as pd
import json

data = pd.read_excel('excel/2003_2020-06.xlsx', index_col='Nationality')

data['Total'] = data['Total'].str.replace(',', '')

for i in data['Total']:
    i = i.replace(',', '')

print(data['Total'])

data.index = data.index.str.title()

data['Total'] = data['Total'].astype(float)
data['Total'] = pd.to_numeric(data['Total'])

data['Time'] = pd.to_datetime(data['Time'], format='%Y-%m')

cleaned_data = []
column = ['Nationality', 'Total', 'Time']


for y in range(2017, 2020):
    st = f'{y}-01'
    et = f'{y}-12'
    print(data[data['Time'].between(st, et)])

time = data.groupby('Time')

nation = data.groupby('Nationality')

# print(time.size())

# print(time.sum())

year_data = {}

for y in range(2017, 2020):
    st = f'{y}-01'
    et = f'{y}-12'
    mask = (data['Time'] >= st) & (data['Time'] <= et)
    # print(data.loc[mask, ['Total','Time']].sum())
    print(nation.filter(
        lambda x:
            x.index == 'Taiwan'
        # (x['Time'] >= st ) & (x['Time'] <= et)
    ))
    # year_data[y] = time.filter(lambda x: x['Time'].between(f"{y}-01", "{y}-12"))

print(data.dtypes)

# print(year_data)


for i in range(len(data.index)):
    tmp = data.iloc[i, [3, 7]]
    # tmp = data.iloc[[i]]
    dict = {}

    dict[column[0]] = data.index[i]
    dict[column[1]] = data.iat[i, 3]
    dict[column[2]] = data.iat[i, 7]

    cleaned_data.append(dict)

# print(cleaned_data)


# print(data)
