def exponencial (n):
    if n == 0:
        print('0^0 = 0')
        return
    elif n == 1:
        print('1^0 = 1')
        return
    b = 2
    while True:
        k = 0
        resultado = 1
        while resultado < n:
            resultado = b ** k
            k = k + 1
        if resultado == n:
            print(f' {b}^{k - 1} = {n}')
            break
        else:
            b = b + 1


exponencial(2)
exponencial(5)