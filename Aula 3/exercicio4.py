salario = float(input("Digite seu salario: "))

if salario > 1250:
    n_salario = salario * 1.1
    print(f"Seu novo salario é: {n_salario:.2f}")

else:
    n_salario2 = salario * 1.15
    print(f"Seu novo salario é: {n_salario2:.2f}")
