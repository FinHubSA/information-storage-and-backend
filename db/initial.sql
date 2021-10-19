CREATE DATABASE aarons_kit_backend;
use aarons_kit_backend;

-- table creation

CREATE TABLE Category(
CategoryID int not null AUTO_INCREMENT,
CategoryName varchar(20),
primary key(CategoryID)
);

CREATE TABLE Journals(
JournalID int not null AUTO_INCREMENT,
JournalName varchar(45),
primary key(JournalID)
);

CREATE TABLE Authors(
AuthorID int not null AUTO_INCREMENT,
AuthorInitial varchar(1),
AuthorSurname varchar(45),
primary key(AuthorID)
);

CREATE TABLE Articles(
ArticleID int not null AUTO_INCREMENT,
URL varchar(150),
Title varchar(150),
YearPublished int not null,
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

ALTER TABLE Category AUTO_INCREMENT=100;
ALTER TABLE Journals AUTO_INCREMENT=100;
ALTER TABLE Authors AUTO_INCREMENT=100;
ALTER TABLE Articles AUTO_INCREMENT=100;
ALTER TABLE Writes AUTO_INCREMENT=100;

-- inserting dummy data into tables

INSERT INTO Journals (JournalName) VALUES ('American Economic Journal: Macroeconomics'), 
('African Review of Money Finance and Banking'), 
('Economic Theory'), 
('Business Economics'), 
('Cambridge Journal of Economics'), 
('The European Journal of Health Economics'), 
('Annual Review of Financial Economics'), 
('Econometric Theory'), 
('Journal of Political Economy'), 
('The Journal of Law & Economics'), 
('Journal of Southeast Asian Economies'), 
('Journal of Post Keynesian Economics');


INSERT INTO Authors (AuthorInitial, AuthorSurname) VALUES ('S','Wiliamson'),
('D','Chen'),
('T','Abdelkhalek'),
('J','Alonso-Ortiz'),
('J','Bullard'),
('G','Gandolfo'),
('S','Zambelli'),
('R','Terkola'),
('B','Kaiser'),
('H','Jürges'),
('L','Laeven'),
('Y','Chen'),
('B','Hansen'),
('J','Shachat'),
('C','Hafner'),
('F','Guvenen'),
('D','Autor'),
('J','Milyo'),
('S','Morrison'), 
('J','Berkowitz'), 
('G','Montinola'),
('J','Takahata'),
('A','Girón'),
('E','Correa'),
('E','Febrero');


INSERT INTO Category (CategoryName) VALUES ('Economics'), ('Finance'), ('Systems');


INSERT INTO Articles (URL, Title, YearPublished, DOI, CategoryID, JournalID) VALUES ('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Stephen%20D.%20Williamson.pdf','Low Real Interest Rates, Collateral Misrepresentation, and Monetary Policy',2018,'10.1257/mac.20150035', 100, 100), 
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Daphne%20Chen.pdf','Corporate Income Tax, Legal Form of Organization, and Employment',	2018, '10.1257/mac.20150035', 100, 100), 
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Touhami%20Abdelkhalek.pdf','MICROECONOMETRIC ANALYSIS OF HOUSEHOLD SAVINGS DETERMINANTS IN MOROCCO', 2010, '10.2307/41803204', 100, 101), 
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Jorge%20Alonso-Ortiz.pdf','The productivity cost of sovereign default: evidence from the European debt crisis',2017, '10.2307/26704994', 100, 102),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/JAMES%20BULLARD.pdf','Three Challenges to Central Bank Orthodoxy', 2015, '10.2307/43678269', 100, 103), 
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Giancarlo%20Gandolfo.pdf','The Tobin tax in a continuous-time non-linear dynamic model of the exchange rate',	2015, '10.1093/cje/bev054',100, 104),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Stefano%20Zambelli.pdf','Dynamical coupling, the non-linear accelerator and the persistence of business cycles',2015,'10.1093/cje/bev052',100, 104),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Robert%20Terkola.pdf','Economic evaluation of personalized medicine: a call for real-world data',2017,'10.1007/s10198-016-0861-7',100,105),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Boris%20Kaiser.pdf','Gender-specific practice styles and ambulatory health care expenditures',	2017,'10.1007/s10198-017-0890-x',100,105),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Hendrik%20J%C3%BCrges.pdf','Financial incentives, timing of births, and infant health: a closer look into the delivery room',2017,'10.1007/s10198-016-0766-5', 100,105),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Luc%20Laeven.pdf','Corporate Governance: Whats Special About Banks?',	2013,'10.11 46/annurev-financial-02 1113 -07442 1', 100, 106),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Ying%20Chen.pdf','MODELING NONSTATIONARY AND LEPTOKURTIC FINANCIAL TIME SERIES',	2015,'10.1017/S0266466614000528', 100, 	107),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Bruce%20E.%20Hansen.pdf','SHRINKAGE EFFICIENCY BOUNDS',2015,'10.1017/S0266466614000693', 100, 107),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Jason%20Shachat.pdf',	'A HIDDEN MARKOV MODEL FOR THE DETECTION OF PURE AND MIXED STRATEGY PLAY IN GAMES',	2015,	'10.1017/S026646661400053X', 100, 107),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Christian%20M.%20Hafner.pdf',	'Asymptotic Theory for a Factor GARCH Model',	2009,'10.1017/S026646660809011', 100, 107),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Fatih%20Guvenen.pdf',	'The Nature of Countercyclical Income Risk',	2014,'10.1086/675535', 100, 108),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/David%20H.%20Autor.pdf',	'Housing Market Spillovers: Evidence from the End of Rent Control in Cambridge, Massachusetts',	2014,'10.1086/675536', 100, 108),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/David%20H.%20Autor.pdf',	'The Electoral Effects of Incumbent Wealth',	1999,'10.1086/467439', 100, 109),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Steven%20A.%20Morrison.pdf',	'Fundamental Flaws of Social Regulation: The Case of Airplane Noise',	1999,'10.1086/467440', 100, 109),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Jeremy%20Berkowitz.pdf',	'Bankruptcy Exemptions and the Market for Mortgage Loans',	1999,'10.1086/467443', 100, 109),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Gabriella%20R.%20Montinola.pdf',	'Tax Reform and Demands for Accountability in the Philippines',	2021,'10.1355/ae38-1a', 100,110),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Junichiro%20Takahata.pdf',	'Intergovernmental Transfers in Indonesia',	2021,'10.1355/ae38-1d', 100, 110),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Alicia%20Gir%C3%B3n.pdf',	'Securitization and financialization',	2012,'10.2753/PKE0160-3477350201', 100, 111),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Eugenia%20Correa.pdf',	'Financialization in Mexico: trajectory and limits',	2012,'10.2753/PKE0160-3477350205', 100, 111),
('https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/Eladio%20Febrero.pdf',	'Three Difficulties with Neo-Chartalism', 2009,	'10.2753/PKE0160-3477310308', 100,111);


INSERT INTO Writes (ArticleID, AuthorID) VALUES (100, 100),
(101, 101),
(102, 102),
(103, 103),
(104, 104),
(105, 105),
(106, 106),
(107, 107),
(108, 108),
(109, 109),
(110, 110),
(111, 111),
(112, 112),
(113, 113),
(114, 114),
(115, 115),
(116, 116),
(117, 117),
(118, 118),
(119, 119),
(120, 120),
(121, 121),
(122, 122),
(123, 123),
(124, 124);