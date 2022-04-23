products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sorted_list = []
def price(my_tuple):
    return float(my_tuple[1])


def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=price, reverse=True)





print(sort_prices(products))

#list_of_tuples.sort(key=price, reverse=True)
