trabalha_por_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = int(input("Digite o numero de horas trabalhadas no mes: "))
salario_bruto = trabalha_por_hora * horas_trabalhadas
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - IR - INSS - sindicato
print(f"+ Salario Bruto: {salario_bruto:.2f}  - INSS {INSS:.2f} - Sindicato {sindicato:.2f} + {salario_liquido:.2f}")
print(f"- IR (11%) {IR:.2f}")
print(f"- INSS (8%) {INSS:.2f}")
print(f"- Sindicato (5%) {sindicato:.2f}")
print(f"+ {salario_liquido:.2f}")