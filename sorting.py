import random
import matplotlib.pyplot as plt

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
    plt.ion()  # Vytvoří prázdný plot
    plt.show()  # Ukáže prázdný plot

    numbers = numbers.copy()
    for it in range(len(numbers) - 1):
        for idx in range(len(numbers) - 1 - it): #Prochází seznam po délku seznamu, kromě posledního prvku, který je již seřazený, a odečítá od toho již seřazené prvky it
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]


                index_highlight1 = idx
                index_highlight2 = idx + 1
                colors = ["steelblue"] * len(numbers)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(numbers)), numbers, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)

    plt.ioff()
    plt.show()
    return numbers



