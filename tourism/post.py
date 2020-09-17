import requests
from typing import Optional
from requests.exceptions import HTTPError


def sendHttpPost(pageUrl, param=None, headers=None,
                 timeout=50) -> Optional[str]:
    try:
        resp = requests.post(pageUrl, data=param, headers=headers,
                             timeout=timeout)
        resp.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP post error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other post error occured: {err}')
        return None
    else:
        return resp


def getHtml(code='21', func='1', yyyy='2020', mm='06', month=''):
    url = 'https://kto.visitkorea.or.kr/eng/tourismStatics/keyFacts/KoreaMonthlyStatistics/eng/inout/inout.kto'
    param = {'code': code, 'func_name': func,
             'yyyy': yyyy, 'mm': mm, 'month': month}
    return sendHttpPost(url, param)
