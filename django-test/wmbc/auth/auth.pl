#!/usr/bin/perl
use Authen::Krb5::Simple;

my $krb = Authen::Krb5::Simple->new();
$krb->realm('UMBC.EDU');

$username = <STDIN>;
$password = <STDIN>;
chomp $username;
chomp $password;

my $authen = $krb->authenticate($username, $password);
if ($authen) {
  print "Success";
}
else {
  print "Failed";
}
