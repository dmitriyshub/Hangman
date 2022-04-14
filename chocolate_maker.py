def chocolate_maker(small, big, x):
    small_parts = small * 1
    big_parts = big * 5
    if (small_parts + big_parts <= x):
        return True
    else:
        return False

print(chocolate_maker(5,5,17))