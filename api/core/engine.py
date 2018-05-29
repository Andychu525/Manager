import requests
import json


def run(method, url, headers=None, bodyParams=None, urlParams=None):
    ret = requests.request(method, url, headers=headers, params=urlParams, data=bodyParams)
    # http://xiaorui.cc/2016/01/25/分析requests源码解决headers无法json问题/
    return {
        'headers': eval(str(ret.headers)),
        'cookies': ret.cookies.get_dict(),
        'code': ret.status_code,
        'reason': ret.reason,
        'content': ret.text,
        'time': ret.elapsed.total_seconds()
    }


def main():
    url = "http://www.baidu.com"
    params = {'cityId': 52,
              'page': 1,
              'size': 0,
              'dk': 'N%2Bay43M7HJ8%3D',
              'gk': 'mfeFAFmM%2F%2BI%3D'}

    headers = {"uthority": "map.365daoyou.cn",
               "method": "GET",
               "path": "/web/scenicGrouploadChildData?gk=whdwMjHgDns%253D&dk=p4DuCWqEqU0%253D&gId=105",
               "scheme": "https",
               "accept": "application/json, text/javascript, */*; q=0.01",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
               "cache-control": "no-cache",
               "cookie": "UM_distinctid=16358ecd1e15cb-0f818889a18a8c-6373563-1fa400-16358ecd1e2fb9; acw_tc=AQAAADeHHgGqvwcA8U1VeIDOFvSMpujz",
               "pragma": "no-cache",
               "x-requested-with": "XMLHttpRequest"
               }
    run("POST", url, headers=headers, urlParams=params)


if __name__ == "__main__":
    main()
