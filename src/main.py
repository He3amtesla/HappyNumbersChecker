def happy_number(n: int) -> bool:
    """
    _summary_:It takes a number and separates its digits.
    After separating, it raises each digit to the 
    power of 2. Then, it sums up the squared digits.
    This process continues until the end. If the 
    um of the digits becomes 1, the number is 
    **Happy Number**; otherwise, it is not.
    
    :param n: input number
    :return: True --> is HappyNumber / False --> is not HappyNumber
    
    Example:
    >>> happy_number(7)
    True
    
    >>> happy_number(45)
    False
    """
    numbers = set()
    while (n != 1) and (n not in numbers):
        numbers.add(n)
        n = sum([int(_)**2 for _ in str(n)])
        #numbers.add(n)
    if n == 1:
        return True
    else:
        return False
    
if __name__ == "__main__":
    assert happy_number(7) is True
    assert happy_number(45) is False 