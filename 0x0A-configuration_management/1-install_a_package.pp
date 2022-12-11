# Installs flask, version 2.1.0

package { 'pip3':
  ensure   => '2.1.0',
  provider => 'flask',
}
