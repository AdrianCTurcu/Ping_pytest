from ping_tool import ping

def test_ping_google():
    assert ping("8.8.8.8") is True

