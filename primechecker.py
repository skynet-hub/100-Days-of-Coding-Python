def prime_checker(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if number == 0:
        print("It is not a prime")
    elif number == 1:
        print("It is not a prime")
    elif is_prime:
        print("It is a prime...")
    else:
        print("It is not a prime")

n = int(input("Enter the number you would like to test..."))
prime_checker(number=n)                            