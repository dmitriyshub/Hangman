def chocolate_maker(small, big, x):
    """
    This function calculates if the all chocloate pieces can be placed in X (chocolate package)
    :param small: small pieces of chocolates 1 cm each
    :param big: Big pieces of chocolates 5 cm each
    :param x: chocolate package size
    :return: True if the chocolate pieces can be place in chocolade package
    """
    small_parts = small * 1
    big_parts = big * 5
    if (small_parts + big_parts <= x):
        return True
    else:
        return False

print(chocolate_maker(5,5,17))
