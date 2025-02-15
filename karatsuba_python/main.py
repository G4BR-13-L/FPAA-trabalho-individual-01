def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max_numero_digitos(x, y)
    m = n // 2

    alta1, baixa1 = dividir(x, m)
    alta2, baixa2 = dividir(y, m)

    z0 = karatsuba(baixa1, baixa2)
    z1 = karatsuba((baixa1 + alta1), (baixa2 + alta2))
    z2 = karatsuba(alta1, alta2)

    resultado = (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0
    return resultado

def dividir(num, m):
    divisor = 10 ** m
    alta = num // divisor
    baixa = num % divisor
    return alta, baixa

def max_numero_digitos(x, y):
    x_digitos = contar_digitos(x)
    y_digitos = contar_digitos(y)
    return max(x_digitos, y_digitos)

def contar_digitos(num):
    if num == 0:
        return 1
    contagem = 0
    n = num
    while n != 0:
        n //= 10
        contagem += 1
    return contagem

def main():
    print("Resultado de 5 * 6:", karatsuba(5, 6))
    print("Resultado de 123 * 456:", karatsuba(123, 456))
    print("Resultado de 123456789 * 987654321:", karatsuba(123456789, 987654321))

if __name__ == "__main__":
    main()