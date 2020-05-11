from bs4 import BeautifulSoup

import requests

import re


def main():
    # 通過requests第三方庫的get方法獲取頁面
    resp = requests.get('http://sports.sohu.com/nba_a.shtml')
    # 對響應的字節串(bytes)進行解碼操作(搜狐的部分頁面使用了GBK編碼)
    html = resp.content.decode('gbk')
    # 創建BeautifulSoup對象來解析頁面(相當於JavaScript的DOM)
    bs = BeautifulSoup(html, 'lxml')
    # 通過CSS選擇器語法查找元素並通過循環進行處理
    # for elem in bs.find_all(lambda x: 'test' in x.attrs):
    for elem in bs.select('a[test]'):
        # 通過attrs屬性(字典)獲取元素的屬性值
        link_url = elem.attrs['href']
        resp = requests.get(link_url)
        bs_sub = BeautifulSoup(resp.text, 'lxml')
        # 使用正則表達式對獲取的數據做進一步的處理
        print(re.sub(r'[\r\n]', '', bs_sub.find('h1').text))


if __name__ == '__main__':
    main()
