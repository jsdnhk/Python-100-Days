
from hashlib import sha1
from urllib.parse import urljoin

import pickle
import re
import requests
import zlib

from bs4 import BeautifulSoup
from redis import Redis


def main():
    # 指定種子頁面
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    # 創建Redis客戶端
    client = Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
    # 設置用戶代理(否則訪問會被拒絕)
    headers = {'user-agent': 'Baiduspider'}
    # 通過requests模塊發送GET請求並指定用戶代理
    resp = requests.get(seed_url, headers=headers)
    # 創建BeautifulSoup對象並指定使用lxml作爲解析器
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    # 將URL處理成SHA1摘要(長度固定更簡短)
    hasher_proto = sha1()
    # 查找所有href屬性以/question打頭的a標籤
    for a_tag in soup.find_all('a', {'href': href_regex}):
        # 獲取a標籤的href屬性值並組裝完整的URL
        href = a_tag.attrs['href']
        full_url = urljoin(base_url, href)
        # 傳入URL生成SHA1摘要
        hasher = hasher_proto.copy()
        hasher.update(full_url.encode('utf-8'))
        field_key = hasher.hexdigest()
        # 如果Redis的鍵'zhihu'對應的hash數據類型中沒有URL的摘要就訪問頁面並緩存
        if not client.hexists('zhihu', field_key):
            html_page = requests.get(full_url, headers=headers).text
            # 對頁面進行序列化和壓縮操作
            zipped_page = zlib.compress(pickle.dumps(html_page))
            # 使用hash數據類型保存URL摘要及其對應的頁面代碼
            client.hset('zhihu', field_key, zipped_page)
    # 顯示總共緩存了多少個頁面
    print('Total %d question pages found.' % client.hlen('zhihu'))


if __name__ == '__main__':
    main()

