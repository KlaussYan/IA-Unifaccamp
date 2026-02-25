print("=== CALCULADORA ===")

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Raiz Quadrada")

ope = int(input("Digite o número da operação: "))

a = float(input("Digite o 1º valor: "))

# Se não for raiz quadrada, pede segundo valor
if ope != 6:
    b = float(input("Digite o 2º valor: "))

if ope == 1:
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

elif ope == 2:
    resultado = a - b
    print(f"{a} - {b} = {resultado}")

elif ope == 3:
    resultado = a * b
    print(f"{a} × {b} = {resultado}")

elif ope == 4:
    if b == 0:
        print("Erro: Não é possível fazer uma divisão por zero")
    else:
        resultado = a / b
        print(f"{a} ÷ {b} = {resultado}")

elif ope == 5:
    resultado = a ** b
    print(f"{a} ^ {b} = {resultado}")

elif ope == 6:
    if a < 0:
        print("Erro: não existe raiz real de número negativo")
    else:
        resultado = a ** 0.5
        print(f"√{a} = {resultado}")

else:
    print("Operação inválida!")


input()