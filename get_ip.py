import requests
import json
import re

headers = {
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.zhimahttp.com',
    'Referer': 'http://www.zhimahttp.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}


a=1
while True:

    response = requests.post('http://wapi.http.linkudp.com/index/index/get_free_ip', headers=headers, data={'page':'%s' % a}, verify = False)
    if response.status_code != 200:
        break
    response=json.loads(response.text)
    response=response.get('ret_data').get('html')
    com=re.compile('<td><span class="slogan".*?span>(.*?)</td>.*?d>(\d{4})</td>',re.S)
    res=re.findall(com,response)
    for i in res:
        i=":".join(i)
        with open("ip.text",'a+') as f:
            f.write(i+'\n')
    a+=1
    print(i,a)
