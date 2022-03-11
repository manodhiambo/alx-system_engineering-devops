# Install puppet-lint 2.5.0 with Puppet
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => gem,
}
