input = {"one": 1, "two": 2, "three": 3}

def dict_iteration_type_1(input: dict)-> None:
    for key, value in input.items():
        print(f"Key: {key}, Value: {value}")


if __name__ == "__main__":
    print("Iterating through dictionary using items():")
    dict_iteration_type_1(input)