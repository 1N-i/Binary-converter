while True:
    try:
        number = int(input("Number: "))
        if number < 0:
            raise ValueError
        break
    except ValueError:
        print("Only positive integers numbers are valid.")

def converter(number):
    binary_number = []
    while number > 0:
        resto = number % 2
        binary_number.insert(0, str(resto))
        number //= 2
    return binary_number

if number >= 1:
    binary_number = converter(number)
else:
    binary_number = ["0"]

print("".join(binary_number))