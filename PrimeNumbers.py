# Program to check whether a number is a prime number or not.

# To take input from the user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than or equal to 1, it is not prime.
else:
    print(num, "is not a prime number")
