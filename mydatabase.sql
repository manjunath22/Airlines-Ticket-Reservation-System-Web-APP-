PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE flight(
f_code varchar primary key,
f_name varchar,
src varchar,
dst varchar);
INSERT INTO "flight" VALUES('AI266','AIR INDIA-9','PATNA','DELHI');
INSERT INTO "flight" VALUES('AI274','AIR INDIA-3','HYDERABAD','CHENNAI');
INSERT INTO "flight" VALUES('AI358','AIR INDIA-7','DELHI','PATNA');
INSERT INTO "flight" VALUES('AI359','AIR INDIA-6','CHENNAI','PATNA');
INSERT INTO "flight" VALUES('AI913','AIR INDIA-10','MUMBAI','HYDERABAD');
INSERT INTO "flight" VALUES('AI933','AIR INDIA-8','HYDERABAD','BANGALORE');
INSERT INTO "flight" VALUES('AI951','AIR INDIA-4','BANGALORE','PATNA');
INSERT INTO "flight" VALUES('AI970','AIR INDIA-5','MUMBAI','CHENNAI');
INSERT INTO "flight" VALUES('AI9730','AIR INDIA-1','BANGALORE','MUMBAI');
INSERT INTO "flight" VALUES('AI9731','AIR INDIA-2','DELHI','CHENNAI');
CREATE TABLE passenger(
pnr_id varchar primary key,
   address varchar,
   nationality varchar,
   name varchar,
   gender varchar,
   ph_no varchar,
   passport varchar,
   f_code varchar,
    foreign key(f_code) references flight(f_code) on delete cascade);
INSERT INTO "passenger" VALUES('','','','','','','',NULL);
INSERT INTO "passenger" VALUES('91','JP NAGAR','INDIA','AJAY','MALE','9945266352','J836982','AI358');
INSERT INTO "passenger" VALUES('120','BSK','INDIA','PRIYA','FEMALE','9945266353','J836983','AI359');
INSERT INTO "passenger" VALUES('200','KORAMANGALA','INDIA','UDAY','MALE','9945266354','J836984','AI266');
INSERT INTO "passenger" VALUES('400','KS LAYOUT','IRAN','SALEEM','MALE','9945266355','J836985','AI913');
INSERT INTO "passenger" VALUES('331','JAYANAGAR','INDIA','SATHISH','MALE','9945266356','J836986','AI933');
INSERT INTO "passenger" VALUES('81','KENGERI','AFGHANISTAN','IRFAN','MALE','9945266357','J836987','AI951');
INSERT INTO "passenger" VALUES('49','BTM LAYOUT','CANADA','RICHA','FEMALE','9945266357','J836988','AI970');
CREATE TABLE sector(
f_code varchar,
capacity number,
class_code varchar,
class_name varchar,
foreign key(f_code) references flight(f_code) on delete cascade);
INSERT INTO "sector" VALUES('AI9730',550,'A','FIRSTCLASSDISCOUNT');
INSERT INTO "sector" VALUES('AI9731',800,'C','BUSINESSCLASSDISCOUNT');
INSERT INTO "sector" VALUES('AI274',600,'F','FIRSTCLASS');
INSERT INTO "sector" VALUES('AI951',500,'D','BUSINESSCLASSDISCOUNT');
INSERT INTO "sector" VALUES('AI970',550,'B','ECONOMY/COACH');
CREATE TABLE cancellation(
pnr_id varchar,
cancellation_no number,
cancellation_date date,
f_code varchar,
foreign key(f_code) references flight(f_code) on delete cascade,
foreign key(pnr_id) references passenger(pnr_id) on delete cascade);
INSERT INTO "cancellation" VALUES('200',201,'2017-03-15','AI266');
INSERT INTO "cancellation" VALUES('300',261,'2017-03-02','AI274');
INSERT INTO "cancellation" VALUES('81',300,'2017-06-10','AI358');
INSERT INTO "cancellation" VALUES('401',378,'2017-03-08','AI359');
INSERT INTO "cancellation" VALUES('49',401,'2017-03-07','AI274');
INSERT INTO "cancellation" VALUES('151',503,'2017-06-07','AI913');
INSERT INTO "cancellation" VALUES('80',58,'2017-06-01','AI933');
CREATE TABLE payment(
pnr_id varchar,
ph_no varchar,
cheque_no varchar,
card_no varchar,
paid_amt varchar,
pay_date date,
foreign key(pnr_id) references passenger(pnr_id) on delete cascade);
INSERT INTO "payment" VALUES('56','9945266350','0046234','-','15000','2017-01-01');
INSERT INTO "payment" VALUES('80','9945266351','0086001','-','20000','2017-01-03');
INSERT INTO "payment" VALUES('91','9945266352','0096021','-','15000','2017-02-05');
INSERT INTO "payment" VALUES('120','9945266353','0015020','-','20000','2017-02-07');
INSERT INTO "payment" VALUES('200','9945266354','-','5195501955019','25000','2017-01-09');
INSERT INTO "payment" VALUES('400','9945266355','0805010','-','25000','2017-02-11');
CREATE TABLE reservation(
pnr_id varchar,
ticket_id varchar,
f_code varchar,
jny_date date,
jny_time varchar,
src varchar,
dst varchar,
foreign key(pnr_id) references passenger(pnr_id) on delete cascade,
foreign key(f_code) references flight(f_code) on delete cascade);
INSERT INTO "reservation" VALUES('331','AB650','AI9730','2017-06-02','5.30PM','BANGALORE','MUMBAI');
INSERT INTO "reservation" VALUES('81','AB651','AI951','2017-06-03','6.00PM','BANGALORE','PATNA');
INSERT INTO "reservation" VALUES('49','AB652','AI9731','2017-03-10','7.00PM','DELHI','CHENNAI');
INSERT INTO "reservation" VALUES('82','AB653','AI970','2017-04-20','4.00PM','MUMBAI','CHENNAI');
INSERT INTO "reservation" VALUES('401','AB654','AI9730','2017-03-11','4.00PM','BANGALORE','MUMBAI');
COMMIT;
