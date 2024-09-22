from pick1 import *
def test_check_guess_correct():
    assert check_guess(5,5) ==0

def test_check_guess_too_high():
    assert check_guess(6,5)==1

def check_guess_too_low():
    assert check_guess(3,5)==2

if __name__ == "__main__":
    import pytest
    pytest.main()