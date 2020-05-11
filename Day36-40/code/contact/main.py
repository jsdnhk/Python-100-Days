"""
-- 創建名爲address的數據庫
create database address default charset utf8;

-- 切換到address數據庫
use address;

-- 創建聯繫人表tb_contacter
create table tb_contacter
(
conid int auto_increment comment '編號',
conname varchar(31) not null comment '姓名',
contel varchar(15) default '' comment '電話',
conemail varchar(255) default'' comment '郵箱',
primary key (conid)
);
"""
import pymysql

INSERT_CONTACTER = """
insert into tb_contacter (conname, contel, conemail) 
values (%s, %s, %s)
"""
DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""
UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s 
where conid=%s
"""
SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter limit %s offset %s
"""
SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter where conname like %s
"""
COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""


class Contacter(object):

    def __init__(self, id, name, tel, email):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email


def input_contacter_info():
    name = input('姓名: ')
    tel = input('手機: ')
    email = input('郵箱: ')
    return name, tel, email


def add_new_contacter(con):
    name, tel, email = input_contacter_info()
    try:
        with con.cursor() as cursor:
            if cursor.execute(INSERT_CONTACTER,
                              (name, tel, email)) == 1:
                print('添加聯繫人成功!')
    except pymysql.MySQLError as err:
        print(err)
        print('添加聯繫人失敗!')


def delete_contacter(con, contacter):
    try:
        with con.cursor() as cursor:
            if cursor.execute(DELETE_CONTACTER, (contacter.id, )) == 1:
                print('聯繫人已經刪除!')
    except pymysql.MySQLError as err:
        print(err)
        print('刪除聯繫人失敗!')


def edit_contacter_info(con, contacter):
    name, tel, email = input_contacter_info()
    contacter.name = name or contacter.name
    contacter.tel = tel or contacter.tel
    contacter.email = email or contacter.email
    try:
        with con.cursor() as cursor:
            if cursor.execute(UPDATE_CONTACTER,
                              (contacter.name, contacter.tel,
                               contacter.email, contacter.id)) == 1:
                print('聯繫人信息已經更新!')
    except pymysql.MySQLError as err:
        print(err)
        print('更新聯繫人信息失敗!')


def show_contacter_detail(con, contacter):
    print('姓名:', contacter.name)
    print('手機號:', contacter.tel)
    print('郵箱:', contacter.email)
    choice = input('是否編輯聯繫人信息?(yes|no)')
    if choice == 'yes':
        edit_contacter_info(con, contacter)
    else:
        choice = input('是否刪除聯繫人信息?(yes|no)')
        if choice == 'yes':
            delete_contacter(con, contacter)


def show_search_result(con, cursor):
    contacters_list = []
    for index, row in enumerate(cursor.fetchall()):
        contacter = Contacter(**row)
        contacters_list.append(contacter)
        print('[%d]: %s' % (index, contacter.name))
    if len(contacters_list) > 0:
        choice = input('是否查看聯繫人詳情?(yes|no)')
        if choice.lower() == 'yes':
            index = int(input('請輸入編號: '))
            if 0 <= index < cursor.rowcount:
                show_contacter_detail(con, contacters_list[index])


def find_all_contacters(con):
    page, size = 1, 5
    try:
        with con.cursor() as cursor:
            cursor.execute(COUNT_CONTACTERS)
            total = cursor.fetchone()['total']
            while True:
                cursor.execute(SELECT_CONTACTERS,
                               (size, (page - 1) * size))
                show_search_result(con, cursor)
                if page * size < total:
                    choice = input('繼續查看下一頁?(yes|no)')
                    if choice.lower() == 'yes':
                        page += 1
                    else:
                        break
                else:
                    print('沒有下一頁記錄!')
                    break
    except pymysql.MySQLError as err:
        print(err)


def find_contacters_by_name(con):
    name = input('聯繫人姓名: ')
    try:
        with con.cursor() as cursor:
            cursor.execute(SELECT_CONTACTERS_BY_NAME,
                           ('%' + name + '%', ))
            show_search_result(con, cursor)
    except pymysql.MySQLError as err:
        print(err)


def find_contacters(con):
    while True:
        print('1. 查看所有聯繫人')
        print('2. 搜索聯繫人')
        print('3. 退出查找')
        choice = int(input('請輸入: '))
        if choice == 1:
            find_all_contacters(con)
        elif choice == 2:
            find_contacters_by_name(con)
        elif choice == 3:
            break


def main():
    con = pymysql.connect(host='1.2.3.4', port=3306,
                          user='yourname', passwd='yourpass',
                          db='address', charset='utf8',
                          autocommit=True,
                          cursorclass=pymysql.cursors.DictCursor)
    while True:
        print('=====通訊錄=====')
        print('1. 新建聯繫人')
        print('2. 查找聯繫人')
        print('3. 退出系統')
        print('===============')
        choice = int(input('請選擇: '))
        if choice == 1:
            add_new_contacter(con)
        elif choice == 2:
            find_contacters(con)
        elif choice == 3:
            con.close()
            print('謝謝使用, 再見！')
            break


if __name__ == '__main__':
    main()
