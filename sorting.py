import random

def random_numbers(count, low=0, high=100):
    """Funkce vygeneruje count náhodných čisel v rozmezí od low po high"""
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    """Funkce projde seznam a pokud se aktuální prvek rovná minimu, vymění prvek na 1. místo v seznamu"""
    numbers = numbers.copy()

    for it in range(len(numbers)):
        minimum = it
        for idx in range(it + 1, len(numbers)):
            if numbers[idx] < numbers[minimum]:
                minimum = idx
        #if minimum != idx: # Pokud by byl seznam seřazený, neprovedlo by se vyměnění
            numbers[it], numbers[minimum] = numbers[minimum], numbers[it]
            # ALTERNATIVNI VERZE
            # sorted_list = []
            # while numbers:
            #    minimum = min(numbers)
            #    sorted_list.append(minimum)
            #    numbers.remove(minimum)
            # return sorted_list
    return numbers

def bubble_sort(numbers):
    for it in range(len(numbers) - 1):
        for idx in range(len(numbers) - 1 - it): #Prochází seznam po délku seznamu, kromě posledního prvku, který je již seřazený, a odečítá od toho již seřazené prvky it
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
    return numbers

