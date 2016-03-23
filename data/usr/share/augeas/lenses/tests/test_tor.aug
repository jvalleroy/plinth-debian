module Test_Tor =

test Tor.lns get "\n" = { }
test Tor.lns get "# comment\n" = { "#comment" = "comment" }
test Tor.lns get "SocksPort 9050\n" = { "SocksPort" = "9050" }
test Tor.lns get "SocksPort 0.0.0.0:9050\n" = { "SocksPort" = "0.0.0.0:9050" }
test Tor.lns get "SocksPort [::]:9050\n" = { "SocksPort" = "[::]:9050" }
test Tor.lns get "ExitPolicy reject *:*\n" = { "ExitPolicy" = "reject *:*" }
test Tor.lns get "VirtualAddrNetworkIPv4 10.192.0.0/10\n" = { "VirtualAddrNetworkIPv4" = "10.192.0.0/10" }
test Tor.lns get "ServerTransportPlugin obfs3,obfs4 exec /usr/bin/obfs4proxy\n" = { "ServerTransportPlugin" = "obfs3,obfs4 exec /usr/bin/obfs4proxy" }
test Tor.lns get "HiddenServiceDir /var/lib/tor/hidden_service/\n" = { "HiddenServiceDir" = "/var/lib/tor/hidden_service/" }
