def square_area(side_length):
    return side_length * side_length
def test_square_area_8():
    result= square_area(8)
    assert result == 64

def test_square_area_6():
    result = square_area(6)
    assert result == 36

square_area(side_length)
test_square_area_8()
test_square_area_6()