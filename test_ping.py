from ping_tool import ping

def test_ping_google():
    assert ping("127.0.0.1") is True

