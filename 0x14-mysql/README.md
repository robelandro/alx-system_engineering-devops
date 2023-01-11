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
SHOW DATABASES;
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
> creat replica user
```
mysql -uholberton_user -p -e "select user,host from mysql.user;" # see users

sudo mysql
CREATE USER 'replica_user'@'%' IDENTIFIED BY '12345678';
GRANT REPLICATION SLAVE  ON *.* TO 'holberton_user'@'localhost
FLUSH PRIVILEGES

mysql -uholberton_user -p -e "select user,host from mysql.user;" # see users
```
> setup replica and source
For source:

`sudo ufw allow from replica_server_ip to any port 3306`
Be sure to replace replica_server_ip with your replica server’s actual IP address.
go to /etc/mysql/mysql.conf.d/mysqld.cnf
add this line
```
server-id         = 1
log_bin           = /var/log/mysql/mysql-bin.log
binlog_do_db      = tyrell_corp
```
bind-address, just comment out this parameter

`sudo systemctl restart mysql`

`sudo mysqldump -u root tyrell_corp > db.sql`

`scp db.sql ubuntu@54.85.131.160:/tmp/`

`sudo mysql tyrell_corp < /tmp/db.sql`
For replica 

`sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf`

add 
```
server-id         = 2
log_bin           = /var/log/mysql/mysql-bin.log
binlog_do_db      = tyrell_corp
relay-log         = /var/log/mysql/mysql-relay-bin.log
```
`sudo systemctl restart mysql`
```
sudo cat /etc/mysql/mysql.conf.d/mysqld.cnf >> 4-mysql_configuration_replica
sudo cat /etc/mysql/mysql.conf.d/mysqld.cnf >> 4-mysql_configuration_primary
```
