drop database if exists shop;
create database shop default charset utf8;
	
use shop;

drop table if exists tb_goods;
create table tb_goods
(
gid int not null auto_increment,
gname varchar(50) not null,
gprice decimal(10,2) not null,
gimage varchar(255),
primary key (gid)
);

insert into tb_goods values 
(default, '樂事（Lay’s）無限薯片', 8.2, 'images/lay.jpg'),
(default, '旺旺 仙貝 加量裝 540g', 18.5, 'images/wang.jpg'),
(default, '多兒比（Dolbee）黃桃水果罐頭', 6.8, 'images/dolbee.jpg'),
(default, '王致和 精製料酒 500ml', 7.9, 'images/wine.jpg'),
(default, '陳克明 麪條 雞蛋龍鬚掛麪', 1.0, 'images/noodle.jpg'),
(default, '魯花 菜籽油 4L', 69.9, 'images/oil.jpg');