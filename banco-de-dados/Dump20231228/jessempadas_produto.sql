-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: jessempadas
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `codproduto` int NOT NULL,
  `lote` varchar(200) DEFAULT NULL,
  `vencimento` date NOT NULL,
  `quantidade` int NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `nomeCategoria` varchar(200) NOT NULL,
  `descricao` text,
  `nome` varchar(200) NOT NULL,
  `cnpjFornecedor` varchar(18) NOT NULL,
  PRIMARY KEY (`codproduto`),
  UNIQUE KEY `codproduto_UNIQUE` (`codproduto`),
  KEY `idcategoria_idx` (`nomeCategoria`),
  KEY `fk_produto_fornecedor1_idx` (`cnpjFornecedor`),
  CONSTRAINT `fk_produto_fornecedor1` FOREIGN KEY (`cnpjFornecedor`) REFERENCES `fornecedor` (`cnpj`),
  CONSTRAINT `idcategoria` FOREIGN KEY (`nomeCategoria`) REFERENCES `categoria` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (1,'1','2023-12-31',100,2.00,'empadas doces','Tradicional','Empada Doce Tradicional\n30g','11.111.111/0001-11'),(2,'2','2023-12-31',100,2.00,'empadas doces','Chocolate','Empada Doce Chocolate\n30g','11.111.111/0001-11'),(9,'9','2023-12-31',100,2.50,'empadas doces','Oreo','Empada Doce Oreo 30g','11.111.111/0001-11'),(10,'10','2023-12-31',100,2.50,'empadas doces','KitKat','Empada Doce KitKat 30g','11.111.111/0001-11'),(11,'11','2023-12-31',100,3.50,'empadas doces','Ninho com Nutella','Empada Doce\nNinho com Nutella 30g','11.111.111/0001-11'),(21,'21','2023-12-31',100,4.00,'empadas doces','Tradicional','Empada Doce\nTradicional 60g','11.111.111/0001-11'),(22,'22','2023-12-31',100,4.50,'empadas doces','Oreo','Empada Doce Oreo 60g','11.111.111/0001-11'),(31,'31','2023-12-31',100,3.50,'empadas salgadas','Frango','Empada Salgada de\nFrango 90g','11.111.111/0001-11'),(32,'32','2023-12-31',100,7.50,'empadas salgadas','Frango','Empada Salgada de\nFrango 200g','11.111.111/0001-11'),(41,'41','2023-12-31',100,6.00,'tortinhas','Chocolate','Tortinha de Chocolate','11.111.111/0001-11'),(42,'42','2023-12-31',100,6.00,'tortinhas','Oreo','Tortinha de Oreo','11.111.111/0001-11'),(51,'51','2023-12-31',100,40.00,'tortas salgadas','tortas salgadas','Torta Salgada 10\nfatias','11.111.111/0001-11'),(52,'52','2023-12-31',100,70.00,'tortas salgadas','tortas salgadas','Torta Salgada 20\nfatias','11.111.111/0001-11'),(61,'61','2023-12-31',100,60.00,'Bolos',NULL,'Bolo 1kg','11.111.111/0001-11'),(62,'62','2023-12-31',100,170.00,'Bolos',NULL,'Bolo 3kg','11.111.111/0001-11'),(63,'63','2023-12-31',100,280.00,'Bolos',NULL,'Bolo 5kg','11.111.111/0001-11'),(71,'71','2023-12-31',100,60.00,'cheesecake',NULL,'Cheesecake','11.111.111/0001-11'),(81,'81','2023-12-31',100,9.50,'caixinhas presentáveis',NULL,'Caixinha 4 empadas\n30g','11.111.111/0001-11'),(82,'82','2023-12-31',100,13.50,'caixinhas presentáveis',NULL,'Caixinha 6 empadas\n30g','11.111.111/0001-11'),(83,'83','2023-12-31',100,9.50,'caixinhas presentáveis',NULL,'Caixinha 2 empadas\n60g','11.111.111/0001-11'),(84,'84','2023-12-31',100,17.50,'caixinhas presentáveis',NULL,'Caixinha 4 empadas\n60g','11.111.111/0001-11'),(91,'91','2023-12-31',100,7.00,'Combos',NULL,'Caixinha 4 empadas 30g','11.111.111/0001-11'),(92,'92','2023-12-31',100,10.00,'Combos',NULL,'Caixinha 6 empadas 30g','11.111.111/0001-11'),(93,'93','2023-12-31',100,20.00,'Combos',NULL,'Caixinha 2 empadas 60g','11.111.111/0001-11'),(94,'94','2023-12-31',100,28.00,'Combos',NULL,'Caixinha 4 empadas 60g','11.111.111/0001-11');
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-28 23:01:35
