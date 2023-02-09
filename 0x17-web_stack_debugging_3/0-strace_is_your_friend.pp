# Fixes wordpress setting where file extension is incorrectly specified

exec { '/usr/bin/env sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php': }
