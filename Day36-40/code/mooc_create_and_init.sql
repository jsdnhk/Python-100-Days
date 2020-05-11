drop database if exists mooc1706;
create database mooc1706 default charset utf8;

use mooc1706;

create table tb_course_catalog
(
catid integer not null auto_increment,
catname varchar(20) not null,
catparent integer,
primary key (catid)
);

alter table tb_course_catalog add constraint fk_catalog_parent 
foreign key (catparent) references tb_course_catalog(catid) 
on delete cascade 
on update cascade;

insert into tb_course_catalog values (default, '前端開發', null);
insert into tb_course_catalog values (default, '後端開發', null);
insert into tb_course_catalog values (default, '移動開發', null);
insert into tb_course_catalog values (default, '數據庫', null);
insert into tb_course_catalog values (default, '雲計算&大數據', null);
insert into tb_course_catalog values (default, '運維&測試', null);
insert into tb_course_catalog values (default, 'UI設計', null);


insert into tb_course_catalog values (default, 'HTML/CSS', 1);
insert into tb_course_catalog values (default, 'JavaScript', 1);
insert into tb_course_catalog values (default, 'jQuery', 1);
insert into tb_course_catalog values (default, 'HTML5', 1);
insert into tb_course_catalog values (default, 'CSS3', 1);
insert into tb_course_catalog values (default, 'Node.js', 1);
insert into tb_course_catalog values (default, 'AngularJS', 1);
insert into tb_course_catalog values (default, 'Bootstrap', 1);
insert into tb_course_catalog values (default, 'React', 1);
insert into tb_course_catalog values (default, 'Sass/Less', 1);
insert into tb_course_catalog values (default, 'Vue.js', 1);
insert into tb_course_catalog values (default, 'WebApp', 1);