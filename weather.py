import requests
from bs4 import BeautifulSoup

#网页的解析函数
def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')#由于html5lib容错性较好因此用它不用lxml
    conMidtab = soup.find('div',class_ = 'conMidtab')
    tables = conMidtab.find_all('table')
    #查看是否拿到了每个城市的天气
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]#获取标签里面的字符串属性返回一个生成器,因此要转化为一个列表
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            print({'城市':city,'最低气温':min_temp})

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml'
    ]
    for url in urls:
        parse_page(url)
if __name__ == '__main__':
    main()



