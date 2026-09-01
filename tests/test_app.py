from app.app import add, hello

def test_add():
    assert add(2, 3) == 5

def test_hello():
    assert hello("Cloud") == "Hello, Cloud!"