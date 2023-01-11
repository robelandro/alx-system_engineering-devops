# Mysql Alx configration : web server
> set up 
- copy public [Signature](https://dev.mysql.com/doc/refman/8.0/en/replication-howto-repuser.html)
- save on signature.key
```
sudo apt-key add signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
sudo apt-get update
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```
> setup username and password
```
sudo mysql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost
FLUSH PRIVILEGES;
```
> Creat database and table populate date into that tabel
```
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6(id INT unsigned NOT NULL AUTO_INCREMENT, name VARCHAR(150) NOT NULL,);
CREATE TABLE nexus6 ( id INT unsigned NOT NULL AUTO_INCREMENT, name VARCHAR(150) NOT NULL, PRIMARY KEY (id) );
SHOW TABLES;
DESCRIBE nexus6;
INSERT INTO nexus6 ( name ) VALUES ( 'Leon') ;
SELECT * FROM nexus6;
```
* Result 
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
