/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50537
Source Host           : localhost:3306
Source Database       : passwords_manager

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2021-09-15 10:44:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `computer`
-- ----------------------------
DROP TABLE IF EXISTS `computer`;
CREATE TABLE `computer` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `host` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of computer
-- ----------------------------
INSERT INTO `computer` VALUES ('31', 'device2', '196.168.100.2');
INSERT INTO `computer` VALUES ('32', 'device1', '192.168.100.1');
INSERT INTO `computer` VALUES ('33', 'device3', '192.168.100.3');
INSERT INTO `computer` VALUES ('34', 'device4', '192.168.100.6');
INSERT INTO `computer` VALUES ('35', 'device5', '192.168.100.8');

-- ----------------------------
-- Table structure for `model`
-- ----------------------------
DROP TABLE IF EXISTS `model`;
CREATE TABLE `model` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `type` int(20) NOT NULL DEFAULT '0',
  `location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of model
-- ----------------------------
INSERT INTO `model` VALUES ('8', 'passGAN', '1', '1810.04805v1.pdf');
INSERT INTO `model` VALUES ('9', 'SeqGAN', '1', '1910.01108v2.pdf');
INSERT INTO `model` VALUES ('10', 'HashCat-best64', '2', 'myrule.rule');
INSERT INTO `model` VALUES ('11', 'HashCat-rockyou-60000', '2', 'myrule.rule');
INSERT INTO `model` VALUES ('12', 'FLA', '3', 'myrule.rule');

-- ----------------------------
-- Table structure for `password`
-- ----------------------------
DROP TABLE IF EXISTS `password`;
CREATE TABLE `password` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `type` int(20) NOT NULL DEFAULT '0',
  `location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of password
-- ----------------------------
INSERT INTO `password` VALUES ('7', 'password_2', '1', 'password2.txt');
INSERT INTO `password` VALUES ('8', 'password_1', '1', 'password.txt');
INSERT INTO `password` VALUES ('9', 'password_3', '1', 'atest.txt');
INSERT INTO `password` VALUES ('10', 'password_4', '1', 'aa_test.txt');
