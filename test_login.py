from login import login

def test_valid_login():
    assert login("admin@caresync.com", "admin123") == True

def test_invalid_password():
    assert login("admin@caresync.com", "wrong123") == False

def test_invalid_user():
    assert login("unknown@gmail.com", "admin123") == False
