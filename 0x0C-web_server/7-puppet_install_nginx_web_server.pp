# Install Nginx web server with puppet
exec { 'installNginx':
  command  =>  'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" > /var/www/html/index.nginx-debian.html ;  sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
  provider =>  shell,
}
