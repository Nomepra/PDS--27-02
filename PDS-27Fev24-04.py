a = int(input("digite um número de 0 até 5: "))
b = int(input("digite um número superior a 10: "))

if a == b:
    print(f"a é igual a b")
elif a != b:
    print(f"a é diferente de b")

if a < b:
    print(f"a é menor que b")
elif a > b:
    print(f"a é maior que b")

if a <= 5:
    print(f"a é menor ou igual a 5")
if b >= 10:
    print(f"b é maior ou igual a 10")