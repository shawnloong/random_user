CREATE TABLE `user_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `login_name` varchar(64) DEFAULT NULL,
  `login_pass` varchar(128) DEFAULT NULL,
  `real_name` varchar(64) DEFAULT NULL,
  `sex` varchar(4) DEFAULT NULL,
  `link_mobile` varchar(16) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `address` varchar(512) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `id_card` varchar(20) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `modify_time` datetime DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3358901 DEFAULT CHARSET=utf8mb4
