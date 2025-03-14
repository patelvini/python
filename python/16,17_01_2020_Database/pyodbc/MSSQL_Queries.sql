CREATE DATABASE DEMO

USE DEMO
---------------------------------------------------------------------------------------------------------------------------------------

SELECT * FROM CUSTOMER;
SELECT * FROM PRODUCT;
SELECT * FROM ORDERS;

SELECT TOP(3) * FROM CUSTOMER;

SELECT FIRST_NAME,* FROM CUSTOMER;

---------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE CUSTOMER
(

ID INT PRIMARY KEY IDENTITY (1,1),
FIRST_NAME CHAR (100) NOT NULL,
LAST_NAME CHAR (100) NOT NULL,
CITY VARCHAR (50),
AGE INT ,

);

INSERT INTO CUSTOMER ([FIRST_NAME],[LAST_NAME],[CITY],[AGE])
VALUES ('VINI','PATEL','VALSAD',20);

INSERT INTO CUSTOMER ([FIRST_NAME],[LAST_NAME],[CITY],[AGE])
VALUES ('FORAM','PATEL','VALSAD',20);

INSERT INTO CUSTOMER ([FIRST_NAME],[LAST_NAME],[CITY],[AGE])
VALUES ('DEEPAK','BHAVSAR','SURAT',23);

INSERT INTO CUSTOMER ([FIRST_NAME],[LAST_NAME],[CITY],[AGE])
VALUES ('MILI','JAVIA','VALSAD',22);

INSERT INTO CUSTOMER ([FIRST_NAME],[LAST_NAME],[CITY],[AGE])
VALUES ('SAUMYA','BHATT','VALSAD',21);

---------------------------------------------------------------------------------------------------------------------------------------

UPDATE CUSTOMER SET CITY = 'VALSAD' WHERE FIRST_NAME = 'VINI';

----------------------------------------------------------------------------------------------------------------------------------------

DELETE CUSTOMER WHERE FIRST_NAME='VINI';

----------------------------------------------------------------------------------------------------------------------------------------

ALTER TABLE CUSTOMER ADD COUNTRY VARCHAR (50);

----------------------------------------------------------------------------------------------------------------------------------------

UPDATE CUSTOMER SET COUNTRY = 'INDIA';

------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE PRODUCT
(

ID INT PRIMARY KEY IDENTITY (1,1),
PRODUCT_NAME VARCHAR (100) ,
PRICE FLOAT ,

);

SELECT * FROM PRODUCT;

INSERT INTO PRODUCT ([PRODUCT_NAME],[PRICE] )
VALUES ('BALL',20.00);

INSERT INTO PRODUCT ([PRODUCT_NAME],[PRICE] )
VALUES ('BASEBALL',50.00);

INSERT INTO PRODUCT ([PRODUCT_NAME],[PRICE] )
VALUES ('BAT',200.00);

INSERT INTO PRODUCT ([PRODUCT_NAME],[PRICE] )
VALUES ('DOLL',100.00);

INSERT INTO PRODUCT ([PRODUCT_NAME],[PRICE] )
VALUES ('FOOTBALL',300.00);

------------------------------------------------------------------------------------------------------------------------------------------


CREATE TABLE ORDERS
(

ORDER_ID INT PRIMARY KEY IDENTITY (1,1),
ORDER_DATE DATE,
PRODUCT_ID INT FOREIGN KEY REFERENCES PRODUCT(ID) ,
CUSTOMER_ID INT FOREIGN KEY REFERENCES CUSTOMER(ID),

);


SELECT * FROM ORDERS;

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),1,1)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),1,2)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),1,4)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),1,3)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),2,4)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),4,4)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),3,4)

INSERT INTO ORDERS ([ORDER_DATE],[PRODUCT_ID],[CUSTOMER_ID])
VALUES (GETDATE(),5,5)

------------------------------------------------------------------------------------------------------------------------------------------------------


SELECT * FROM ORDERS AS O 
INNER JOIN PRODUCT P ON
O.PRODUCT_ID = P.ID
INNER JOIN CUSTOMER C ON
O.CUSTOMER_ID = C.ID;


SELECT C.ID,C.FIRST_NAME,P.PRODUCT_NAME,P.PRICE,O.ORDER_DATE,O.ORDER_ID FROM ORDERS AS O 
INNER JOIN PRODUCT P ON
O.PRODUCT_ID = P.ID
INNER JOIN CUSTOMER C ON
O.CUSTOMER_ID = C.ID;

SELECT C.LAST_NAME,SUM(P.PRICE) TOTAL, AVG(P.PRICE) AVERAGE FROM ORDERS O 
INNER JOIN PRODUCT P ON
O.PRODUCT_ID = P.ID
INNER JOIN CUSTOMER C ON
O.CUSTOMER_ID = C.ID GROUP BY C.LAST_NAME;

--------------------------------------------------------------------------------------------------------------------------------------------------------


SELECT 