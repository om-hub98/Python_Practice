# while True:
#     num = int(input("Enter a number: "))
#     is_prime = True
#     if num <=1 :
#         print(f"{num} Not a prime number")
#     else:
#         for i in range(2, int(num/2)+1):
#             if num%i == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             print(f"{num} Prime number")
#         else:
#             print(f"{num} Not a prime number")

#     exit = input("Do you want to exit? (y/n): ")
#     if exit.lower() != 'y':
#         print("Exiting the program.")
#         break

        



## Check if a number is prime or not
while True: 
    num = int(input("Enter a number: "))
    is_prime = True
    if num <= 1:
        print(f"{num} Not a prime number")
    else:
        for i in range(2, int(num/2)+1):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} Prime number")
        else:
            print(f"{num} Not a prime number")

    exit = input("Do you want to exit? (y/n): ")
    if exit.lower() == 'y':
        print("Exiting the program.")
        break
    
