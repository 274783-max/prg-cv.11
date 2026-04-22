import random

def random_numbers(count, low=0, high=100):
    """Funkce vygeneruje count náhodných čisel v rozmezí od low po high"""
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers.copy()
    sorted_list = []
    while numbers:
        minimum = min(numbers)
        sorted_list.append(minimum)
        numbers.remove(minimum)

    #for i in range(len(numbers)):
    #    minimum = min(numbers)
    #    if i == minimum:
    #        sorted_list.append(i)
    return sorted_list


        #for i in range n:
        #    n -= 1


        #if minimum < numbers[0]:
        #    numbers[minimum] = numbers[0]
