input = [1, 2, 3, 4, 5]

def iterate_list_type_1(numbers: list)-> None:
    for num in numbers:
        print(num)


def iterate_list_type_2(numbers: list)-> None:
    for i in range(len(numbers)):
        print(numbers[i])

def iterate_list_type_3(numbers: list)-> None:
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

if __name__ == "__main__":
    print("Iterating using type 1:")
    iterate_list_type_1(input)

    print("\nIterating using type 2 - using range:")
    iterate_list_type_2(input)

    print("\nIterating using type 3 - using while loop:")
    iterate_list_type_3(input)