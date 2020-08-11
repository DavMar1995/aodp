import pandas as pd
import numpy as np
from tqdm import tqdm
import re

# print(pd.__version__ )


def getSheet(sheetName, nameList=False):
    io = r'C:\Users\yjwil\OneDrive\Desktop\aodp\all_cancer\column_info.xls'
    if nameList is False:
        info = pd.read_excel(io, sheet_name=sheetName)
    else:
        info = pd.read_excel(io, sheet_name=sheetName, names=nameList)
    # print(info.head())
    # print(info)
    return info


def getRefData(df, rowNum, idx, info):
    list = []

    for i in range(rowNum):
        # print(df.iat[i, 0])
        dict = {'id': df.iat[i, idx], 'info': df.iat[i, info]}
        # print(i, dict)
        list.append(dict)

    return list


def getCauseSheet(df):
    list = []


def getData(start, end):
    count = 0
    data = {}
    columns = []

    for year in range(start, end+1):
        print(f'This is {year}({year+1911})')
        f = open(f'cancer{year}.txt', 'r')
        for i, element in enumerate(f):
            if i == 0:
                tmp = element.replace('\n', '').split(',')
                for j in tmp:
                    columns.append(j)
                continue
            data[count+i] = element.replace('\n', '').split(',')
            max = count + i
        count = max

    df = pd.DataFrame(
        data, index=['year', 'county', 'cause', 'sex', 'age_code', 'N'])

    # print(columns)

    # print(df.T)
    df = df.T
    print(df)
    return df


def compareData(df, ageData, causeData):
    global AGE, SEX, CAUSE, COUNTY, REGIONS
    rowNum, colNum = df.shape

    for i in range(rowNum):
        # * age_code
        # * Changing the "age_code"...
        for age in ageData:
            # print(df.iat[i, AGE], age['id'])
            if re.sub('^0', '', df.iat[i, AGE]) == age['id'].astype(str):
                df.iat[i, AGE] = age['info']
                # print('---------------------------------------------------------------------------------------')

        # * sex
        # * Changing the "sex"...
        if df.iat[i, SEX] == '1':
            df.iat[i, SEX] = '男'
        else:
            df.iat[i, SEX] = '女'

        # * cause
        # * Changing the "cause"...
        for cause in causeData:
            # print(type(re.sub('^0', '',df.iat[i, CAUSE])), type(y))
            if re.sub('^0', '', df.iat[i, CAUSE]) == cause['id'].astype(int).astype(str):
                df.iat[i, CAUSE] = cause['info']
                # print('---------------------------------------------------------------------------------------')

        # * country
        # for j in range(REGIONS):
        # print(df.iat[i, COUNTY][:2] ==
        # print(df.iat[i, COUNTY][:2], REGIONS.__contains__(df.iat[i, COUNTY][:2]))
        if REGIONS.__contains__(df.iat[i, COUNTY][:2]):
            df.iat[i, COUNTY] = REGIONS.get(df.iat[i, COUNTY][:2])
            # print(df.iat[i, COUNTY])


if __name__ == '__main__':
    YEAR = 0
    COUNTY = 1
    CAUSE = 2
    SEX = 3
    AGE = 4
    NUM = 5

    start = 108
    end = start
    # end = 108

    REGIONS = {
        '01': 'Taipei City', '03': 'Taichung City',
        '05': 'Tainan City', '07': 'Kaohsiung City',
        '11': 'Keelung City', '12': 'Hsinchu City',
        '22': 'Chiayi City', '31': 'New Taipei City',
        '32': 'Taoyuan County', '33': 'Hsinchu County',
        '34': 'Yilan County', '35': 'Miaoli County',
        '37': 'Changhua County', '38': 'Nantou County',
        '39': 'Yunlin County', '40': 'Chiayi County',
        '43': 'Pingtung County', '44': 'Penghu County',
        '45': 'Hualien County', '46': 'Taitung County',
        '90': 'Kinmen County', '91': 'Lienchiang County',
    }

    cancerData = getData(start, end)

    ageData = getRefData(getSheet(1), 27, 0, 1)
    # print(ageData)
    causeData = getRefData(getSheet(2), 33, 4, 5)
    # print(causeData)

    compareData(cancerData, ageData, causeData)
    print(cancerData)

    # cancerData.progress_apply(lambda x: x, axis=1)

    cancerData.to_excel(f'cancer_{start}-{end}.xlsx')
    cancerData.to_csv(f'cancer_{start}-{end}.csv')
