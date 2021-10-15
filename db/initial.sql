CREATE DATABASE aarons_kit_backend;
use aarons_kit_backend;

-- table creation

CREATE TABLE Category(
CategoryID int not null,
CategoryName varchar(20),
primary key(CategoryID)
);

CREATE TABLE Journals(
JournalID int not null,
JournalName varchar(45),
primary key(JournalID)
);

CREATE TABLE Authors(
AuthorID int not null,
AuthorInitial varchar(1),
AuthorSurname varchar(45),
primary key(AuthorID)
);

CREATE TABLE Articles(
ArticleID int not null,
URL varchar(150),
Title varchar(150),
YearPublished int,
CategoryID int not null,
DOI varchar(80),
JournalID int not null,
primary key(ArticleID),
foreign key(CategoryID) references Category(CategoryID),
foreign key(JournalID) references Journals(JournalID)
);

CREATE TABLE Writes(
ArticleID int not null, 
AuthorID int not null, 
CONSTRAINT PK_Writes primary key(ArticleID, AuthorID),
foreign key(ArticleID) references Articles(ArticleID),
foreign key(AuthorID) references Authors(AuthorID)
);

-- inserting dummy data into tables

INSERT INTO Journals VALUES (1, 'American Economic Journal: Macroeconomics');
INSERT INTO Journals VALUES (2, 'African Review of Money Finance and Banking');
INSERT INTO Journals VALUES (3, 'Economic Theory');
INSERT INTO Journals VALUES (4, 'Business Economics');

INSERT INTO Authors VALUES (1,'S','Wiliamson');
INSERT INTO Authors VALUES (2,'D','Chen');
INSERT INTO Authors VALUES (3,'T','Abdelkhalek');
INSERT INTO Authors VALUES (4,'J','Alonso-Ortiz');
INSERT INTO Authors VALUES (5,'J','Bullard');


INSERT INTO Category VALUES (1, 'Economics');
INSERT INTO Category VALUES (2, 'Finance');
INSERT INTO Category VALUES (3, 'Systems');

INSERT INTO Articles  VALUES (2,'https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Daphne%20Chen.pdf','Corporate Income Tax, Legal Form of Organization, and Employment',2018,1,'10.1257/mac.20150035',1);
INSERT INTO Articles  VALUES (3,'https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Touhami%20Abdelkhalek.pdf','MICROECONOMETRIC ANALYSIS OF HOUSEHOLD SAVINGS DETERMINANTS IN MOROCCO',2010,1,'10.2307/41803204',2);
INSERT INTO Articles  VALUES (4,'https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Jorge%20Alonso-Ortiz.pdf','The productivity cost of sovereign default: evidence from the European debt crisis',2017,1,'10.2307/26704994',3);
INSERT INTO Articles  VALUES (5,'https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/JAMES%20BULLARD.pdf','Three Challenges to Central Bank Orthodoxy',2015,1,'10.2307/43678269',4);

INSERT INTO Writes VALUES (2,2);
INSERT INTO Writes VALUES (3,3);
INSERT INTO Writes VALUES (4,4);
INSERT INTO Writes VALUES (5,5);