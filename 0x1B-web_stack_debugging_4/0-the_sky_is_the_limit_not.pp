# fix nginx server client requests so that we get to 0 errors
exec { 'increase ulimit':
  command  => "sed -i 's/15/30000/g' /etc/default/nginx; sudo service nginx reload; sudo service nginx restart",
  provider => shell,
}
