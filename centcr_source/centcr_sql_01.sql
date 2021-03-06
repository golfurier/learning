

create table projects(id serial primary key not null, proj_name varchar not null);
create table departments(id serial primary key not null, dep_name varchar not null);
create table testers(id serial primary key not null, t_name varchar not null, t_lastname varchar not null, dep_id integer not null references departments);
create table accepters(id serial primary key not null, a_name varchar not null, a_lastname varchar not null, dep_id integer not null references departments);
create table transactions(id serial primary key not null, trans_type varchar not null);
create table switchings(id serial primary key not null, sw_name varchar not null);
create table actas(id serial primary key not null, act_as varchar not null);
create table status(id serial primary key not null, status varchar not null);
create table lgnt(id serial primary key not null, lgnt varchar not null);

create table tcrs(id serial primary key not null,
case_no varchar not null,
mti varchar,
case_name varchar,
purpose varchar,
card_no varchar,
f4 varchar,
f39_exp varchar,
f39_visa varchar,
f39_mastercard varchar,
f39_itmx varchar,
f39_pcc varchar,
f39_eps varchar,
f39_clsp varchar,
f39_clst varchar,
f39_cardm varchar,
f39_cbs varchar,
seq_no varchar,
tdate varchar,
lgnt varchar,
status_id integer not null references status,
progress_comment varchar,
project_id integer not null references projects,
switching_id integer not null references switchings,
transaction_id integer not null references transactions,
actas_id integer not null references actas,
tester_id integer not null references testers,
accepter_id integer not null references accepters
);



insert into departments(dep_name) VALUES ('ฝพรบ');
insert into departments(dep_name) VALUES ('ฝปอ');
insert into departments(dep_name) VALUES ('ฝผบ');
insert into testers(t_name, t_lastname, dep_id) VALUES ('Ukrit', 'Koolvitit', '1');
insert into testers(t_name, t_lastname, dep_id) VALUES ('Nopsara', 'Sumneanglum', '1');
insert into accepters(a_name, a_lastname, dep_id) VALUES ('XXX', 'XXX', '2');
insert into accepters(a_name, a_lastname, dep_id) VALUES ('YYY', 'YYY', '3');
insert into transactions(trans_type) VALUES ('ATM');
insert into transactions(trans_type) VALUES ('POS');
insert into transactions(trans_type) VALUES ('OCT');
insert into transactions(trans_type) VALUES ('ORFT');
insert into transactions(trans_type) VALUES ('PAYMENT');
insert into transactions(trans_type) VALUES ('PP');
insert into switchings(sw_name) VALUES ('VISA');
insert into switchings(sw_name) VALUES ('MASTERCARD');
insert into switchings(sw_name) VALUES ('ITMX');
insert into switchings(sw_name) VALUES ('PCC');
insert into switchings(sw_name) VALUES ('OnUs');
insert into actas(act_as) VALUES ('ACQ');
insert into actas(act_as) VALUES ('ISS');
insert into status(status) VALUES ('Passed');
insert into status(status) VALUES ('Failed');
insert into status(status) VALUES ('Pending');
insert into projects (proj_name) VALUES ('VISA2018001');
insert into lgnt(lgnt) VALUES ('SIT');
insert into lgnt(lgnt) VALUES ('UAT');

insert into tcrs(case_no,mti,case_name,purpose,card_no,f4,f39_exp,f39_visa,f39_mastercard,f39_itmx,f39_pcc,f39_eps,f39_clsp,f39_clst,f39_cardm,f39_cbs,seq_no,tdate,lgnt,status_id,progress_comment,project_id,switching_id,transaction_id,actas_id,tester_id,accepter_id)
VALUES ('3.2','0200/0210','Balance Inquiry – Savings Account','','4834460100000082','','00','00','','','','000','','5000','00','','1234','2018/05/05','SIT','1','ACQ CRNCY CDE=764','1','1','1','2','1','1');
insert into tcrs (case_no,mti,case_name,purpose,card_no,f4,f39_exp,f39_visa,f39_mastercard,f39_itmx,f39_pcc,f39_eps,f39_clsp,f39_clst,f39_cardm,f39_cbs,seq_no,tdate,lgnt,status_id,progress_comment,project_id,switching_id,transaction_id,actas_id,tester_id,accepter_id)
VALUES ('2.4','0200/0210','Authorization - Unspecified Account - with MVV','','4834460100000082','400.00','00','00','','','','000','','5000','00','','1235','2018/05/06','SIT','1','ACQ CRNCY CDE=764','1','1','2','2','1','1');

select * from testers join departments on testers.dep_id = departments.id;
select * from accepters join departments on accepters.dep_id = departments.id;
select t_name , t_lastname, dep_name from testers join departments on testers.dep_id = departments.id;
select a_name , a_lastname, dep_name from accepters join departments on accepters.dep_id = departments.id;

SELECT 
	tcr.case_num,
	tcr.mti,
	tcr.description,
	tcr.purpose,
	tcr.card,
	tcr.expected_values,
	tcr.actual_values,
	status.status,
	tcr.progress_comment,
	projects.proj_name,
	switchings.sw_name,
	transactions.trans_type,
	actas.act_as,
	testers.t_name,
	accepters.a_name
FROM tcr
INNER 
	JOIN status
	ON tcr.status_id = status.id
INNER
	JOIN projects
	ON tcr.project_id = projects.id
INNER
	JOIN switchings
	ON tcr.switching_id = switchings.id
INNER
	JOIN transactions
	ON tcr.transaction_id = transactions.id
INNER
	JOIN actas
	ON tcr.actas_Id = actas.id
INNER 
	JOIN testers
	ON tcr.tester_id = testers.id
INNER 
	JOIN accepters
	ON tcr.accepter_id = accepters.id

drop table projects, departments, testers, accepters;

alter table testers add foreign key (department_id) references departments;
alter table accepters add foreign key (department_id) references departments;

update tcrs set case_name = 'Balance Inquiry – Savings Account' where case_no = '3.2';
delete from tcrs where id = 2