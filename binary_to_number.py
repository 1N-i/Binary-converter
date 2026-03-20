while True:
    list_str = []
    try:
        binary = input("Binary: ")
        for digit in binary:
            if digit != "0" and digit != "1":
                raise ValueError
            list_str.append(digit)
        if binary == "":
            raise ValueError
        break
    except ValueError:
        print("Only binary numbers are valid.")

list_int = []
for digit in list_str:
    list_int.append(int(digit))

list_int.reverse()
number = 0
for i in range(len(list_int)):
    if list_int[i] == 1:
        number += 2 ** i

print(number)