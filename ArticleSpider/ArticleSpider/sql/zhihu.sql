DROP TABLE IF EXISTS `zhihu_question`;
CREATE TABLE `zhihu_question` (
  `zhihu_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `topics` varchar(255) DEFAULT NULL,
  `url` varchar(300) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` LONGTEXT NOT NULL,
  `create_time` DATETIME DEFAULT NULL,
  `answer_time` DATETIME DEFAULT NULL,
  `answer_num` int(11) NOT NULL,
  `comments_num` int(11) NOT NULL,
  `watch_user_num` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `crawl_time` DATETIME NOT NULL,
  `crawl_update_time` DATETIME DEFAULT NULL,
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `zhihu_answer`;
CREATE TABLE `zhihu_answer` (
  `zhihu_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(300) NOT NULL,
  `question_id` bigint(20) NOT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `content` LONGTEXT NOT NULL,
  `praise_num` int(11) NOT NULL,
  `comments_num` int(11) NOT NULL,
  `create_time` DATE NOT NULL,
  `update_time` DATE NOT NULL,
  `crawl_time` DATETIME NOT NULL,
  `crawl_update_time` DATETIME DEFAULT NULL,
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;