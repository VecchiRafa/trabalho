-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: aunimalhotel
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cobranca_forma`
--

DROP TABLE IF EXISTS `cobranca_forma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cobranca_forma` (
  `id_cobranca_forma` int unsigned NOT NULL,
  `id_cobranca` int unsigned NOT NULL,
  `id_forma` int unsigned NOT NULL,
  PRIMARY KEY (`id_cobranca_forma`),
  UNIQUE KEY `id_cobranca_forma_UNIQUE` (`id_cobranca_forma`),
  KEY `fk_cobranca_forma_cobranca_idx` (`id_cobranca`),
  KEY `fk_cobranca_forma_forma_idx` (`id_forma`),
  CONSTRAINT `fk_cobranca_forma_cobranca` FOREIGN KEY (`id_cobranca`) REFERENCES `cobranca` (`id_cobranca`) ON DELETE RESTRICT,
  CONSTRAINT `fk_cobranca_forma_forma` FOREIGN KEY (`id_forma`) REFERENCES `forma` (`id_forma`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cobranca_forma`
--

LOCK TABLES `cobranca_forma` WRITE;
/*!40000 ALTER TABLE `cobranca_forma` DISABLE KEYS */;
/*!40000 ALTER TABLE `cobranca_forma` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-14 17:19:18
