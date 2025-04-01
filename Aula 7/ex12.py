def quoci_resto(dividendo, divisor):
    quociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        quociente = quociente + 1

    print(f'O quociente é {quociente} e o resto é {dividendo}')

dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Dgite o divisor: '))

(quociente, resto) = quoci_resto(dividendo, divisor)
print(f'O quociente da divisão é {quociente} e o resto é {resto}')
