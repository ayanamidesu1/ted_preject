-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: ted
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '22280e92-05be-11ef-ba69-80fa5b5f0ae3:1-15,
ef18a94f-0601-11ef-b34a-00155de60230:1-3724';

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `avatar_path` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户头像名称',
  `sex` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `birthday` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '生日',
  `introduce` longtext COLLATE utf8mb4_unicode_ci COMMENT '作者简介',
  `self_website` longtext COLLATE utf8mb4_unicode_ci COMMENT '作者个人网站',
  `self_website_introduce` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '作者个人网站简介',
  `user_tags` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '作者头衔/标签',
  `user_status` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户个人账号状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'123456','2024-09-25 18:54:08.000000',1,'admin','sun','yuanling','344215394@qq.com',1,1,'2024-09-25 18:55:01.000000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'pbkdf2_sha256$720000$CeR10ZAvpNXn0zlRk27TEv$2uUsyXHkd5+caQ3SaY5UxxmYmGIBMPnAvsySQHHFs1s=',NULL,1,'test_user','','','admin@example.com',1,1,'2024-09-25 11:11:21.338294',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'pbkdf2_sha256$720000$jtua63bnd9cpqJmTbuPZmh$BDj3x7Xle5NW/Nl2PafPyZ75kYAG/kyT1bHLPPxfRoc=','2024-09-26 00:43:30.000000',0,'aaa','sun','yuanling','11232@qq.com',1,1,'2024-09-26 00:43:30.000000','956953952044960592652','女','2024-09-26',NULL,NULL,NULL,NULL,NULL),(4,'pbkdf2_sha256$720000$NiewqXI0clrvACICrXXnks$ruVPGN5GWMhf0AvHlKfEgV7VNOWVVarD5NFeaqcBUbQ=','2024-09-26 15:36:54.000000',0,'testuser','sun','yuanling','123456@aa.com',1,1,'2024-09-26 15:36:54.000000','821241793609919129143','男','2024-09-26','这是一个简单的介绍','https://www.baidu.com/','别想那么多，这就是一个百度','计算机算法专家',NULL);
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collect_table`
--

DROP TABLE IF EXISTS `collect_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collect_table` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `video_id` int NOT NULL COMMENT '视频id',
  `user_id` int DEFAULT NULL COMMENT '观看视频的用户ID',
  `collect_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '视频收藏时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collect_table`
--

LOCK TABLES `collect_table` WRITE;
/*!40000 ALTER TABLE `collect_table` DISABLE KEYS */;
INSERT INTO `collect_table` VALUES (3,1,4,'2024-10-01 23:30:01');
/*!40000 ALTER TABLE `collect_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_interaction`
--

DROP TABLE IF EXISTS `comment_interaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment_interaction` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL COMMENT '操作的用户',
  `comment_id` bigint DEFAULT NULL COMMENT '交互的评论',
  `comment_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '评论的类型',
  `interaction_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '交互的时间',
  `interaction_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '交互类型：like,not_like',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_interaction`
--

LOCK TABLES `comment_interaction` WRITE;
/*!40000 ALTER TABLE `comment_interaction` DISABLE KEYS */;
INSERT INTO `comment_interaction` VALUES (1,4,1,'comment','2024-9-29 23:24:27','like'),(6,4,2,'comment','2024-09-30 23:58:42','like'),(7,4,4,'reply','2024-09-30 23:58:41','like'),(8,4,6,'reply','2024-09-30 23:58:50','like'),(9,4,2,'reply','2024-09-30 23:58:52','like'),(10,4,7,'comment','2024-09-30 23:58:52','like'),(11,4,3,'reply','2024-09-30 23:59:03','like');
/*!40000 ALTER TABLE `comment_interaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_reply_table`
--

DROP TABLE IF EXISTS `comment_reply_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment_reply_table` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `comment_level` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '评论分级',
  `comment_content` longtext COLLATE utf8mb4_unicode_ci COMMENT '评论内容',
  `send_user_id` int DEFAULT NULL COMMENT '发送者的ID',
  `reply_comment_id` bigint DEFAULT NULL COMMENT '回复的评论ID',
  `send_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发送的时间',
  `belong_to_video_id` bigint DEFAULT NULL COMMENT '所属的视频ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_reply_table`
--

LOCK TABLES `comment_reply_table` WRITE;
/*!40000 ALTER TABLE `comment_reply_table` DISABLE KEYS */;
INSERT INTO `comment_reply_table` VALUES (1,'1','回复主评论1测试',4,1,'2024-9-27 15:24:11',1),(2,'1','回复主评论1测试2',4,1,'2024-9-27 15:24:31',1),(3,'1','回复主评论2测试',4,2,'2024-9-27 15:27:32',1),(4,'1','回复主评论2测试2',4,2,'2024-9-27 15:29:18',1),(6,'1','测试',4,2,'2024-09-30 00:43:47',1),(7,'1','子评论回复评论测试',4,6,'2024-09-30 18:28:32',1);
/*!40000 ALTER TABLE `comment_reply_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_table`
--

DROP TABLE IF EXISTS `comment_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment_table` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `send_user_id` int DEFAULT NULL COMMENT '评论发送id',
  `comment_content` longtext COLLATE utf8mb4_unicode_ci COMMENT '评论内容',
  `comment_level` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '评论等级，0主，1副',
  `reply_comment_id` bigint DEFAULT NULL COMMENT '回复的主评论的id，主评论时为空',
  `send_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '评论发送的时间',
  `video_id` int DEFAULT NULL COMMENT '评论所属的视频的id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_table`
--

LOCK TABLES `comment_table` WRITE;
/*!40000 ALTER TABLE `comment_table` DISABLE KEYS */;
INSERT INTO `comment_table` VALUES (1,4,'主评论测试','0',NULL,'2024-9-27 15:23:14',1),(2,4,'主评论测试','0',NULL,'2024-9-27 15:23:46',1),(7,4,'主评论发送测试','0',NULL,'2024-09-30 16:16:12',1);
/*!40000 ALTER TABLE `comment_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'auth','group'),(1,'auth','permission'),(3,'auth','user'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-25 10:41:28.338093'),(2,'contenttypes','0002_remove_content_type_name','2024-09-25 10:41:28.399581'),(3,'auth','0001_initial','2024-09-25 10:41:28.944688'),(4,'auth','0002_alter_permission_name_max_length','2024-09-25 10:41:29.002934'),(5,'auth','0003_alter_user_email_max_length','2024-09-25 10:41:29.022975'),(6,'auth','0004_alter_user_username_opts','2024-09-25 10:41:29.030498'),(7,'auth','0005_alter_user_last_login_null','2024-09-25 10:41:29.079006'),(8,'auth','0006_require_contenttypes_0002','2024-09-25 10:41:29.083221'),(9,'auth','0007_alter_validators_add_error_messages','2024-09-25 10:41:29.090806'),(10,'auth','0008_alter_user_username_max_length','2024-09-25 10:41:29.149564'),(11,'auth','0009_alter_user_last_name_max_length','2024-09-25 10:41:29.225284'),(12,'auth','0010_alter_group_name_max_length','2024-09-25 10:41:29.243117'),(13,'auth','0011_update_proxy_permissions','2024-09-25 10:41:29.253636'),(14,'auth','0012_alter_user_first_name_max_length','2024-09-25 10:41:29.310937'),(15,'sessions','0001_initial','2024-09-25 10:41:29.349035');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_table`
--

DROP TABLE IF EXISTS `like_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_table` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `video_id` int NOT NULL COMMENT '视频id',
  `user_id` int DEFAULT NULL COMMENT '点赞/喜欢视频的用户',
  `like_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_table`
--

LOCK TABLES `like_table` WRITE;
/*!40000 ALTER TABLE `like_table` DISABLE KEYS */;
INSERT INTO `like_table` VALUES (3,1,4,'2024-10-01 23:30:02');
/*!40000 ALTER TABLE `like_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video_info`
--

DROP TABLE IF EXISTS `video_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `video_info` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '视频标题',
  `author` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '作者',
  `author_id` int NOT NULL COMMENT '作者id',
  `introduce` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '视频简介',
  `create_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '视频上传时间',
  `tags` longtext COLLATE utf8mb4_unicode_ci COMMENT '视频相关标签',
  `video_file_path` longtext COLLATE utf8mb4_unicode_ci COMMENT '视频文件所在路径',
  `video_status` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '视频目前状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video_info`
--

LOCK TABLES `video_info` WRITE;
/*!40000 ALTER TABLE `video_info` DISABLE KEYS */;
INSERT INTO `video_info` VALUES (1,'测试视频一','testuser',4,'这是一个简单的视频简介','2024-9-27 15:55:12','游戏,实况,核爆','v1.mp4','1');
/*!40000 ALTER TABLE `video_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watch_table`
--

DROP TABLE IF EXISTS `watch_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `watch_table` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `video_id` int NOT NULL COMMENT '视频id',
  `user_id` int NOT NULL COMMENT '观看视频的用户ID',
  `watch_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '观看视频的时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watch_table`
--

LOCK TABLES `watch_table` WRITE;
/*!40000 ALTER TABLE `watch_table` DISABLE KEYS */;
INSERT INTO `watch_table` VALUES (1,1,4,'2024-10-01 17:32:57');
/*!40000 ALTER TABLE `watch_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ted'
--

--
-- Dumping routines for database 'ted'
--
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-02 23:42:11
