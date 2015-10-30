/*creation*/
delimiter $$
DROP SCHEMA IF EXISTS `entropy2`$$
CREATE DATABASE `entropy2` /*!40100 DEFAULT CHARACTER SET utf8mb4 */$$
USE entropy2$$
CREATE TABLE `twitter` (
  `user_id` varchar(255) CHARACTER SET latin1 NOT NULL,
  `tweet_id` varchar(255) CHARACTER SET latin1 NOT NULL,
  `tweet_time` timestamp NULL DEFAULT NULL,
  `tweet_score` int(11) DEFAULT NULL,
  `tweet_text` text CHARACTER SET utf8 NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
   PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4$$

 
/**addition of index**/
ALTER TABLE `entropy2`.`twitter` 
ADD INDEX `user_tweet_time` (`user_id` ASC, `tweet_time` ASC) $$

/**addition of decode procedure**/
/**http://stackoverflow.com/questions/11062330/mysql-decode-unicode-to-utf-8-function**/
CREATE DEFINER=`root`@`%` FUNCTION `STRINGDECODE`(str TEXT CHARSET utf8) RETURNS text CHARSET utf8
    DETERMINISTIC
BEGIN
declare pos         int;
declare escape      char(6) charset utf8;
declare unescape    char(3) charset utf8;
set pos = locate('\\u', str);
while pos > 0 do
    set escape = substring(str, pos, 6);
    set unescape = char(conv(substring(escape,3),16,10) using ucs2);
    set str = replace(str, escape, unescape);
    set pos = locate('\\u', str, pos+1);
end while;
return str;
END$$

