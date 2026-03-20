while True:
    lista_str = []
    try:
        binary = input("Binary: ")
        for digit in binary:
            if digit != "0" and digit != "1":
                raise ValueError
            lista_str.append(digit)
        if binary == "":
            raise ValueError
        break
    except ValueError:
        print("Only binary numbers are valid.")

print(lista_str)
lista_int = []
for digit in lista_str:
    lista_int.append(int(digit))

lista_int.reverse()
lista_number = []
for i in range(len(lista_int)):
    print(i)

print(lista_int)