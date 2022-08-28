
def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    return sum(x % divide == 0 for x in numbers)

class ListDivideException(Exception):
    pass

def test_list_divide():
    """
    Test listDivide
    """
    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30, 54, 63,98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
    except:
        raise ListDivideException


if __name__ == "__main__":
    test_list_divide()
