from ping_tool import ping_host

def test_ping_localhost():
    assert ping_host("127.0.0.1") == "Ping OK"
