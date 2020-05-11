drop database if exists hrs;
create database hrs default charset utf8;

use hrs;

drop table if exists tb_emp;
drop table if exists tb_dept;

create table tb_dept
(
dno int not null comment '編號',
dname varchar(10) not null comment '名稱',
dloc varchar(20) not null comment '所在地',
primary key (dno)
);

insert into tb_dept values 
	(10, '會計部', '北京'),
	(20, '研發部', '成都'),
	(30, '銷售部', '重慶'),
	(40, '運維部', '深圳');

create table tb_emp
(
eno int not null comment '員工編號',
ename varchar(20) not null comment '員工姓名',
job varchar(20) not null comment '員工職位',
mgr int comment '主管編號',
sal int not null comment '員工月薪',
comm int comment '每月補貼',
dno int comment '所在部門編號',
primary key (eno)
);

alter table tb_emp add constraint fk_emp_mgr foreign key (mgr) references tb_emp (eno);
alter table tb_emp add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);

insert into tb_emp values 
	(7800, '張三丰', '總裁', null, 9000, 1200, 20),
	(2056, '喬峯', '分析師', 7800, 5000, 1500, 20),
	(3088, '李莫愁', '設計師', 2056, 3500, 800, 20),
	(3211, '張無忌', '程序員', 2056, 3200, null, 20),
	(3233, '丘處機', '程序員', 2056, 3400, null, 20),
	(3251, '張翠山', '程序員', 2056, 4000, null, 20),
	(5566, '宋遠橋', '會計師', 7800, 4000, 1000, 10),
	(5234, '郭靖', '出納', 5566, 2000, null, 10),
	(3344, '黃蓉', '銷售主管', 7800, 3000, 800, 30),
	(1359, '胡一刀', '銷售員', 3344, 1800, 200, 30),
	(4466, '苗人鳳', '銷售員', 3344, 2500, null, 30),
	(3244, '歐陽鋒', '程序員', 3088, 3200, null, 20),
	(3577, '楊過', '會計', 5566, 2200, null, 10),
	(3588, '朱九真', '會計', 5566, 2500, null, 10);


-- 查詢月薪最高的員工姓名和月薪

-- 查詢員工的姓名和年薪((月薪+補貼)*13)

-- 查詢有員工的部門的編號和人數

-- 查詢所有部門的名稱和人數

-- 查詢月薪最高的員工(Boss除外)的姓名和月薪

-- 查詢薪水超過平均薪水的員工的姓名和月薪

-- 查詢薪水超過其所在部門平均薪水的員工的姓名、部門編號和月薪

-- 查詢部門中薪水最高的人姓名、月薪和所在部門名稱

-- 查詢主管的姓名和職位

-- 查詢月薪排名4~6名的員工姓名和月薪
