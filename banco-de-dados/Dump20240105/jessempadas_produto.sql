-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: jessempadas
-- ------------------------------------------------------
-- Server version	8.0.30

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
INSERT INTO `produto` VALUES (1,'0001','2024-02-10',5,2.00,'empadas doces','gostoso','empada tradicional','11.555.666/0007-00'),(126,'13','2024-02-10',100,2.00,'empadas doces','empada doce - prestigio (P)','empada prestigio','11.555.666/0007-00'),(300,'90','2024-01-08',1,60.00,'bolos','Bolo de 1kg','bolo','11.555.666/0007-00'),(1114,'0001','2024-01-14',20,5.00,'empadas salgadas','Empada de bacon','Empada de Bacon','11.555.666/0007-00'),(1411,'0001','2024-01-14',20,5.00,'empadas doces','Empada de Maracuja','Empada de Maracuja','11.555.666/0007-00');
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

-- Dump completed on 2024-01-05 15:46:18
