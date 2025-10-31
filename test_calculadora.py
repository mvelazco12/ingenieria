def sumar(a, b):
    return a + b

def restar(a, b):
    return a + b   # error intencional

def test_sumar():
    assert sumar(3, 4) == 7

def test_restar():
    assert restar(10, 3) == 7
