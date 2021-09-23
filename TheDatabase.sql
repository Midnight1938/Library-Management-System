-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: Library
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4


--
-- Table structure for table `Authors`
--

DROP TABLE IF EXISTS `Authors`;
CREATE TABLE `Authors` (
  `idAuthor` int NOT NULL AUTO_INCREMENT,
  `Author_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idAuthor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Authors`
--

LOCK TABLES `Authors` WRITE;
INSERT INTO `Authors` VALUES (1,'Rick Riordan'),(2,'Roald Dahl'),(3,'Lewis Caroll'),(4,'Neil Gaiman');
UNLOCK TABLES;

--
-- Table structure for table `Book`
--

DROP TABLE IF EXISTS `Book`;
CREATE TABLE `Book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Book_name` varchar(45) DEFAULT NULL,
  `Book_describe` varchar(100) DEFAULT NULL,
  `Book_code` varchar(45) DEFAULT NULL,
  `Book_category` varchar(30) DEFAULT NULL,
  `Book_author` varchar(30) DEFAULT NULL,
  `Book_publisher` varchar(30) DEFAULT NULL,
  `Book_price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Book`
--

LOCK TABLES `Book` WRITE;
INSERT INTO `Book` VALUES (1,'American Gods','The extraordinary, highly acclaimed novel from storytelling genius Neil Gaiman ','000001','3','3','3',352),(2,'Coraline','A dark fantasy childrens novel.','000002','4','3','3',221);
UNLOCK TABLES;

--
-- Table structure for table `Categories`
--

DROP TABLE IF EXISTS `Categories`;
CREATE TABLE `Categories` (
  `idCategory` int NOT NULL AUTO_INCREMENT,
  `Category_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCategory`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Categories`
--

LOCK TABLES `Categories` WRITE;
INSERT INTO `Categories` VALUES (1,'Action'),(2,'Drama'),(3,'Romance'),(4,'Fantasy'),(5,'Dark Fantasy');
UNLOCK TABLES;

--
-- Table structure for table `Client`
--

DROP TABLE IF EXISTS `Client`;
CREATE TABLE `Client` (
  `idClient` int NOT NULL,
  `Client_name` varchar(45) DEFAULT NULL,
  `Client_email` varchar(45) DEFAULT NULL,
  `Client_ID` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idClient`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Client`
--

LOCK TABLES `Client` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `Day-To-Day_Tasks`
--

DROP TABLE IF EXISTS `Day-To-Day_Tasks`;
CREATE TABLE `Day-To-Day_Tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Book_name` varchar(45) DEFAULT NULL,
  `Type` int DEFAULT NULL,
  `Duration` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Client` varchar(45) DEFAULT NULL,
  `To_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Day-To-Day_Tasks`
--

LOCK TABLES `Day-To-Day_Tasks` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `Publishers`
--

DROP TABLE IF EXISTS `Publishers`;
CREATE TABLE `Publishers` (
  `idPublisher` int NOT NULL AUTO_INCREMENT,
  `Publisher_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPublisher`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Publishers`
--

LOCK TABLES `Publishers` WRITE;
INSERT INTO `Publishers` VALUES (1,'Puffin Books'),(2,'Orient'),(3,'S Chand and Co.'),(4,'Harper Collins');
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `idUsers` int NOT NULL AUTO_INCREMENT,
  `User_name` varchar(45) DEFAULT NULL,
  `User_email` varchar(45) DEFAULT NULL,
  `User_pwd` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUsers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
UNLOCK TABLES;


-- Dump completed on 2020-10-21 17:23:35
