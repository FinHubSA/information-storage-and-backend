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
URL varchar(80),
Title varchar(80),
DatePublished date,
DOI varchar(80),
CategoryID int not null,
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

INSERT INTO Journals
VALUES (1, 'Economic Theory');