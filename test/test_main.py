from src.main import mac_welcome


def test_not_on_mac():
    not_mac = mac_welcome()
    assert not_mac == "You are NOT on a Mac!"

def test_on_mac():
    not_mac = mac_welcome()
    assert not_mac == "You are on a Mac!"    