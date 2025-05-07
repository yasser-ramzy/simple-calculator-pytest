from calculator import add , subtract , multiply , divide
def test_add():
    assert add(2,3)==5

def test_subtract():
    assert subtract(10,2)==8

def test_multiply():
    assert multiply(2,3)==6

def test_divide():
    assert divide(2,2)==1

def test_divide_by_zero():
    assert divide(2,0)=="cannot divide by zero"