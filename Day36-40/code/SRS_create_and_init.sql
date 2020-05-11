-- 如果存在名爲school的數據庫就刪除它
drop database if exists school;

-- 創建名爲school的數據庫並設置默認的字符集和排序方式
create database school default charset utf8 collate utf8_bin;

-- 切換到school數據庫上下文環境
use school;

-- 創建學院表
create table tb_college
(
collid int not null auto_increment comment '編號',
collname varchar(50) not null comment '名稱',
collmaster varchar(20) not null comment '院長',
collweb varchar(511) default '' comment '網站',
primary key (collid)
);

-- 創建學生表
create table tb_student
(
stuid int not null comment '學號',
stuname varchar(20) not null comment '姓名',
stusex bit default 1 comment '性別',
stubirth date not null comment '出生日期',
stuaddr varchar(255) default '' comment '籍貫',
collid int not null comment '所屬學院',
primary key (stuid),
foreign key (collid) references tb_college (collid)
);

-- alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);

-- 創建教師表
create table tb_teacher
(
teaid int not null comment '工號',
teaname varchar(20) not null comment '姓名',
teatitle varchar(10) default '助教' comment '職稱',
collid int not null comment '所屬學院',
primary key (teaid),
foreign key (collid) references tb_college (collid)
);

-- 創建課程表
create table tb_course
(
couid int not null comment '編號',
couname varchar(50) not null comment '名稱',
coucredit int not null comment '學分',
teaid int not null comment '授課老師',
primary key (couid),
foreign key (teaid) references tb_teacher (teaid)
);

-- 創建選課記錄表
create table tb_score
(
scid int auto_increment comment '選課記錄編號',
stuid int not null comment '選課學生',
couid int not null comment '所選課程',
scdate datetime comment '選課時間日期',
scmark decimal(4,1) comment '考試成績',
primary key (scid),
foreign key (stuid) references tb_student (stuid),
foreign key (couid) references tb_course (couid)
);

-- 添加唯一性約束（一個學生選某個課程只能選一次）
alter table tb_score add constraint uni_score_stuid_couid unique (stuid, couid);

-- 插入學院數據
insert into tb_college (collname, collmaster, collweb) values 
('計算機學院', '左冷禪', 'http://www.abc.com'),
('外國語學院', '嶽不羣', 'http://www.xyz.com'),
('經濟管理學院', '風清揚', 'http://www.foo.com');

-- 插入學生數據
insert into tb_student (stuid, stuname, stusex, stubirth, stuaddr, collid) values
(1001, '楊逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南長沙', 1),
(1033, '王語嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '嶽不羣', 1, '1993-7-19', '陝西咸陽', 1),
(1378, '紀嫣然', 0, '1995-8-12', '四川綿陽', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '東方不敗', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '項少龍', 1, '1993-1-25', null, 3),
(3923, '楊不悔', 0, '1985-4-17', '四川成都', 3);

-- 插入老師數據
insert into tb_teacher (teaid, teaname, teatitle, collid) values 
(1122, '張三丰', '教授', 1),
(1133, '宋遠橋', '副教授', 1),
(1144, '楊逍', '副教授', 1),
(2255, '範遙', '副教授', 2),
(3366, '韋一笑', '講師', 3);

-- 插入課程數據
insert into tb_course (couid, couname, coucredit, teaid) values 
(1111, 'Python程序設計', 3, 1122),
(2222, 'Web前端開發', 2, 1122),
(3333, '操作系統', 4, 1122),
(4444, '計算機網絡', 2, 1133),
(5555, '編譯原理', 4, 1144),
(6666, '算法和數據結構', 3, 1144),
(7777, '經貿法語', 3, 2255),
(8888, '成本會計', 2, 3366),
(9999, '審計學', 3, 3366);

-- 插入選課數據
insert into tb_score (stuid, couid, scdate, scmark) values 
(1001, 1111, '2017-09-01', 95),
(1001, 2222, '2017-09-01', 87.5),
(1001, 3333, '2017-09-01', 100),
(1001, 4444, '2018-09-03', null),
(1001, 6666, '2017-09-02', 100),
(1002, 1111, '2017-09-03', 65),
(1002, 5555, '2017-09-01', 42),
(1033, 1111, '2017-09-03', 92.5),
(1033, 4444, '2017-09-01', 78),
(1033, 5555, '2017-09-01', 82.5),
(1572, 1111, '2017-09-02', 78),
(1378, 1111, '2017-09-05', 82),
(1378, 7777, '2017-09-02', 65.5),
(2035, 7777, '2018-09-03', 88),
(2035, 9999, curdate(), null),
(3755, 1111, date(now()), null),
(3755, 8888, date(now()), null),
(3755, 9999, '2017-09-01', 92);

-- 查詢所有學生信息
select * from tb_student;

-- 查詢所有課程名稱及學分(投影和別名)
select couname, coucredit from tb_course;
select couname as 課程名稱, coucredit as 學分 from tb_course;

select stuname as 姓名, case stusex when 1 then '男' else '女' end as 性別 from tb_student;
select stuname as 姓名, if(stusex, '男', '女') as 性別 from tb_student;

-- 查詢所有女學生的姓名和出生日期(篩選)
select stuname, stubirth from tb_student where stusex=0;

-- 查詢所有80後學生的姓名、性別和出生日期(篩選)
select stuname, stusex, stubirth from tb_student where stubirth>='1980-1-1' and stubirth<='1989-12-31';
select stuname, stusex, stubirth from tb_student where stubirth between '1980-1-1' and '1989-12-31';

-- 查詢姓"楊"的學生姓名和性別(模糊)
select stuname, stusex from tb_student where stuname like '楊%';

-- 查詢姓"楊"名字兩個字的學生姓名和性別(模糊)
select stuname, stusex from tb_student where stuname like '楊_';

-- 查詢姓"楊"名字三個字的學生姓名和性別(模糊)
select stuname, stusex from tb_student where stuname like '楊__';

-- 查詢名字中有"不"字或"嫣"字的學生的姓名(模糊)
select stuname, stusex from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查詢沒有錄入家庭住址的學生姓名(空值)
select stuname from tb_student where stuaddr is null;

-- 查詢錄入了家庭住址的學生姓名(空值)
select stuname from tb_student where stuaddr is not null;

-- 查詢學生選課的所有日期(去重)
select distinct scdate from tb_score;

-- 查詢學生的家庭住址(去重)
select distinct stuaddr from tb_student where stuaddr is not null;

-- 查詢男學生的姓名和生日按年齡從大到小排列(排序)
-- asc - ascending - 升序（從小到大）
-- desc - descending - 降序（從大到小）
select stuname as 姓名, year(now())-year(stubirth) as 年齡 from tb_student where stusex=1 order by 年齡 desc;

-- 聚合函數：max / min / count / sum / avg
-- 查詢年齡最大的學生的出生日期(聚合函數)
select min(stubirth) from tb_student;

-- 查詢年齡最小的學生的出生日期(聚合函數)
select max(stubirth) from tb_student;

-- 查詢男女學生的人數(分組和聚合函數)
select count(stuid) from tb_student;
select stusex, count(*) from tb_student group by stusex;
select stusex, min(stubirth) from tb_student group by stusex;

-- 查詢課程編號爲1111的課程的平均成績(篩選和聚合函數)
select avg(scmark) from tb_score where couid=1111;
select min(scmark) from tb_score where couid=1111;
select count(scid) from tb_score where couid=1111;
select count(scmark) from tb_score where couid=1111;

-- 查詢學號爲1001的學生所有課程的平均分(篩選和聚合函數)
select avg(scmark) from tb_score where stuid=1001;

-- 查詢每個學生的學號和平均成績(分組和聚合函數)
select stuid as 學號, avg(scmark) as 平均分 from tb_score group by stuid;

-- 查詢平均成績大於等於90分的學生的學號和平均成績
-- 分組以前的篩選使用where子句
-- 分組以後的篩選使用having子句
select stuid as 學號, avg(scmark) as 平均分 from tb_score group by stuid having 平均分>=90;

-- 查詢年齡最大的學生的姓名(子查詢/嵌套的查詢)
select stuname from tb_student where stubirth=(
	select min(stubirth) from tb_student
);

-- 查詢年齡最大的學生姓名和年齡(子查詢+運算)
select stuname as 姓名, year(now())-year(stubirth) as 年齡 from tb_student where stubirth=(
	select min(stubirth) from tb_student
);

-- 查詢選了兩門以上的課程的學生姓名(子查詢/分組條件/集合運算)
select stuname from tb_student where stuid in (
	select stuid from tb_score group by stuid having count(stuid)>2
)

-- 查詢學生姓名、課程名稱以及成績(連接查詢)
select stuname, couname, scmark from tb_student t1, tb_course t2, tb_score t3 where t1.stuid=t3.stuid and t2.couid=t3.couid and scmark is not null;

select stuname, couname, scmark from tb_student t1 inner join tb_score t3 on t1.stuid=t3.stuid inner join tb_course t2 on t2.couid=t3.couid where scmark is not null order by scmark desc limit 5 offset 10;

select stuname, couname, scmark from tb_student t1 inner join tb_score t3 on t1.stuid=t3.stuid inner join tb_course t2 on t2.couid=t3.couid where scmark is not null order by scmark desc limit 10, 5;

-- 單表：65535TB
-- 單列：4G - LONGBLOB (Binary Large OBject) / LONGTEXT
-- 查詢選課學生的姓名和平均成績(子查詢和連接查詢)
select stuname, avgmark from tb_student t1, (select stuid, avg(scmark) as avgmark from tb_score group by stuid) t2 where t1.stuid=t2.stuid;

select stuname, avgmark from tb_student t1 inner join 
(select stuid, avg(scmark) as avgmark from tb_score group by stuid) t2 on t1.stuid=t2.stuid;

-- 內連接（inner join）：只有滿足連接條件的記錄纔會被查出來
-- 外連接（outer join）：左外連接 / 右外連接 / 全外連接
-- left outer join / right outer join / full outer join
-- 查詢每個學生的姓名和選課數量(左外連接和子查詢)
select stuname, ifnull(total, 0) from tb_student t1 left outer join (select stuid, count(stuid) as total from tb_score group by stuid) t2 on t1.stuid=t2.stuid;
