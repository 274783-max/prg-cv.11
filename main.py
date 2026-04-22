from sorting import random_numbers, selection_sort




def main():

    numbers = random_numbers(20)
    print(numbers)
    print(selection_sort(numbers))



# small = random_numbers(5, low=0, high=20)
# print(small)

# my_list[1], my_list[3] = my_list[3], my_list[1]
if __name__ == "__main__":
    main()
