-- Adminer 4.6.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

CREATE DATABASE `produit` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `produit`;

DROP TABLE IF EXISTS `marque`;
CREATE TABLE `marque` (
  `id_marque` int(11) NOT NULL AUTO_INCREMENT,
  `nom_marque` varchar(100) NOT NULL,
  PRIMARY KEY (`id_marque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `modele_marque`;
CREATE TABLE `modele_marque` (
  `id_produit` bigint(16) NOT NULL,
  `id_marque` int(11) NOT NULL,
  KEY `id_produit` (`id_produit`),
  KEY `id_marque` (`id_marque`),
  CONSTRAINT `modele_marque_ibfk_1` FOREIGN KEY (`id_produit`) REFERENCES `produit` (`pr_cd_pr`),
  CONSTRAINT `modele_marque_ibfk_2` FOREIGN KEY (`id_marque`) REFERENCES `marque` (`id_marque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `produit`;
CREATE TABLE `produit` (
  `pr_cd_pr` bigint(16) NOT NULL AUTO_INCREMENT,
  `pr_desi` varchar(100) NOT NULL,
  `pr_stre` int(11) NOT NULL DEFAULT '0',
  `pr_douane` varchar(14) NOT NULL DEFAULT '0',
  `pr_prac` decimal(8,2) NOT NULL DEFAULT '0.00',
  `pr_deg` int(11) NOT NULL DEFAULT '0',
  `pr_pdn` int(11) NOT NULL DEFAULT '0',
  `pr_four` int(11) NOT NULL DEFAULT '0',
  `pr_refour` varchar(40) NOT NULL,
  `pr_codebarre` bigint(14) DEFAULT NULL,
  `pr_modele` varchar(30) NOT NULL,
  `pr_prix` decimal(8,2) NOT NULL,
  `pr_pack` int(11) NOT NULL,
  PRIMARY KEY (`pr_cd_pr`)
) AUTO_INCREMENT=1000000 ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 2018-07-13 16:54:01
