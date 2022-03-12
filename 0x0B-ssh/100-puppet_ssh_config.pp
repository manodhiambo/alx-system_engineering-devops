# ssh Client configuration file
file_line { 'ssh identity':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  multiple => false,
}
file_line { 'ssh PassAuth':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  multiple => false,
}
file_line { 'ssh BatchMode':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'BatchMode no',
  multiple => false,
}
