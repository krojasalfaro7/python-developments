input_number = int(input())

if (input_number % 3 == 0) and (input_number % 5 == 0):
    print("FizzBuzz")
elif input_number % 3 == 0:
    print("Fizz")
elif input_number % 5 == 0:
    print("Buzz")
