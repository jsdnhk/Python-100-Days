from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl

from pymysql import Error


# 通過指定的字符集對頁面進行解碼(不是每個網站都將字符集設置爲utf-8)
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


# 獲取頁面的HTML代碼(通過遞歸實現指定次數的重試操作)
def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


# 從頁面中提取需要的部分(通常是鏈接也可以通過正則表達式進行指定)
def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


# 開始執行爬蟲程序並對指定的數據進行持久化操作
def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    conn = pymysql.connect(host='localhost', port=3306,
                           database='crawler', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            visited_url_list = {seed_url: 0}
            while url_list:
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                            if headings:
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)',
                                       param_list)
                    conn.commit()
    except Error:
        pass
        # logging.error('SQL:', error)
    finally:
        conn.close()


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)


if __name__ == '__main__':
    main()
