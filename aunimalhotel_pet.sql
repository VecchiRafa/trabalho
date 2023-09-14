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
-- Table structure for table `pet`
--

DROP TABLE IF EXISTS `pet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pet` (
  `id_pet` int unsigned NOT NULL AUTO_INCREMENT,
  `data_criacao` timestamp NOT NULL,
  `nome` varchar(50) NOT NULL,
  `peso` decimal(5,2) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `porte` varchar(2) NOT NULL,
  `nascimento` date NOT NULL,
  `descricao` tinytext,
  `id_especie` int unsigned NOT NULL,
  `id_raca` int unsigned NOT NULL,
  PRIMARY KEY (`id_pet`),
  UNIQUE KEY `id_UNIQUE` (`id_pet`),
  KEY `fk_pet_especie_idx` (`id_especie`),
  KEY `fk_id_raca_idx` (`id_raca`),
  CONSTRAINT `fk_id_raca` FOREIGN KEY (`id_raca`) REFERENCES `raca` (`id_raca`),
  CONSTRAINT `fk_pet_especie` FOREIGN KEY (`id_especie`) REFERENCES `especie` (`id_especie`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet`
--

LOCK TABLES `pet` WRITE;
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
INSERT INTO `pet` VALUES (1,'2023-09-14 18:42:05','la',30.00,'m','p','2000-05-10','lindo',2,4),(2,'2023-09-14 18:42:05','feijão',15.00,'m','pp','2000-03-10','peludo',2,2),(3,'2023-09-14 18:49:08','brother',50.00,'m','g','2010-12-30','marrom',2,2);
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-14 17:19:19
