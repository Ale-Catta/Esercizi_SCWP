def test_divide_valid():
    from f_for_test import divide
    assert divide(10, 2) == 5

def test_divide_zero():
    from f_for_test import divide
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Denominator cannot be zero."