/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50636
Source Host           : localhost:3306
Source Database       : github_python

Target Server Type    : MYSQL
Target Server Version : 50636
File Encoding         : 65001

Date: 2018-02-28 15:55:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for infomation
-- ----------------------------
DROP TABLE IF EXISTS `infomation`;
CREATE TABLE `infomation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL COMMENT '标题',
  `front_cover_img` text NOT NULL COMMENT '封面图片地址',
  `content` text NOT NULL COMMENT '内容',
  `add_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of infomation
-- ----------------------------

-- ----------------------------
-- Table structure for manager
-- ----------------------------
DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login_name` text NOT NULL COMMENT '登陆账号',
  `login_password` text NOT NULL COMMENT '登陆密码（默认123456）',
  `last_login_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '最后登陆时间',
  `last_login_ip` text NOT NULL COMMENT '最后登陆ip',
  `login_count` int(11) NOT NULL DEFAULT '0' COMMENT '登陆次数',
  `is_enable` tinyint(4) NOT NULL DEFAULT '1' COMMENT '账号是否启用，1=true(启用)，0=false（禁用）',
  `add_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '注册时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager
-- ----------------------------
INSERT INTO `manager` VALUES ('1', 'peteryan', 'E10ADC3949BA59ABBE56E057F20F883E', '0000-00-00 00:00:00', '127.0.0.1', '1', '1', '2018-02-28 15:27:16');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL COMMENT '菜单名称或各个页面功能名称',
  `code` text NOT NULL COMMENT '产品编码',
  `product_class_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属产品分类',
  `standard` text NOT NULL COMMENT '产品规格',
  `quality_guarantee_period` text NOT NULL COMMENT '保质期',
  `place_of_origin` text NOT NULL COMMENT '产地',
  `front_cover_img` text NOT NULL COMMENT '封面图片地址（展示图片）',
  `content` text NOT NULL COMMENT '产品描述',
  `is_enable` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否启用，1=true(启用)，0=false（禁用）',
  `add_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------

-- ----------------------------
-- Table structure for product_class
-- ----------------------------
DROP TABLE IF EXISTS `product_class`;
CREATE TABLE `product_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL COMMENT '菜单名称或各个页面功能名称',
  `is_enable` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否启用，1=true(启用)，0=false（禁用）',
  `add_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_class
-- ----------------------------
SET FOREIGN_KEY_CHECKS=1;
