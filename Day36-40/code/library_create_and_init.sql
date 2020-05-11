drop database if exists library;

create database library default charset utf8;

use library;

create table tb_book
(
bookid integer primary key auto_increment,
title varchar(100) not null,
author varchar(50) not null,
publisher varchar(50) not null,
price float not null,
lendout bit default 0,
lenddate datetime,
lendcount integer default 0
);

insert into tb_book (title, author, publisher, price, lendcount) values ('Java核心技術(卷1)', '凱 S.霍斯特曼', '機械工業出版社', 98.2, 102);
insert into tb_book (title, author, publisher, price, lendcount) values ('Java編程思想', '埃史爾', '機械工業出版社', 86.4, 87);
insert into tb_book (title, author, publisher, price, lendcount) values ('深入理解Java虛擬機', '周志明', '機械工業出版社', 64.4, 32);
insert into tb_book (title, author, publisher, price, lendcount) values ('Effective Java中文版(第2版) ', '埃史爾', '機械工業出版社', 36.8, 200);
insert into tb_book (title, author, publisher, price, lendcount) values ('數據結構與算法分析:Java語言描述(原書第3版)', '馬克·艾倫·維斯', '機械工業出版社', 51.0, 15);
insert into tb_book (title, author, publisher, price, lendcount) values ('Java 8實戰', '厄馬', '人民郵電出版社', 56.8, 25);
insert into tb_book (title, author, publisher, price, lendcount) values ('重構:改善既有代碼的設計', '馬丁·福勒', '人民郵電出版社', 53.1, 99);
insert into tb_book (title, author, publisher, price, lendcount) values ('代碼大全(第2版)', '史蒂夫•邁克康奈爾', '電子工業出版社', 53.1, 99);
insert into tb_book (title, author, publisher, price, lendcount) values ('程序員修煉之道:從小工到專家', '亨特, 托馬斯', '電子工業出版社', 45.4, 50);
insert into tb_book (title, author, publisher, price, lendcount) values ('代碼整潔之道', '馬丁', '人民郵電出版社', 45.4, 30);
insert into tb_book (title, author, publisher, price, lendcount) values ('設計模式 可複用面向對象軟件的基礎', 'Erich Gamma, Richard Helm', '機械工業出版社', 30.2, 77);
insert into tb_book (title, author, publisher, price, lendcount) values ('設計模式之禪(第2版)', '秦小波', '機械工業出版社', 70.4, 100);

