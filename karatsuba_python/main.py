def karatsuba(x, y):
    if x < 10 or y < 10: # 2 operações
        return x * y # 1 operação

    n = max_numero_digitos(x, y) # 1 operação de chamada da função, 1 atribuição
    m = n // 2

    alta1, baixa1 = dividir(x, m) # 1 operação de chamada da função, 2 atribuições
    alta2, baixa2 = dividir(y, m) # 1 operação de chamada da função, 2 atribuições

    z0 = karatsuba(baixa1, baixa2) # 1 operação de chamada da função, 1 atribuição
    z1 = karatsuba((baixa1 + alta1), (baixa2 + alta2)) # 2 operações, 1 chamada de função, 1 atribuição
    z2 = karatsuba(alta1, alta2) # 1 chamada de função, 1 atribuição

    resultado = (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0 # 7 operações, 1 atribuição
    return resultado # 1 operação

def dividir(num, m):
    divisor = 10 ** m # 1 operação, 1 atribuição
    alta = num // divisor # 1 operação, , 1 atribuição
    baixa = num % divisor  # 1 operação, , 1 atribuição
    return alta, baixa # 1 operação

def max_numero_digitos(x, y):
    x_digitos = contar_digitos(x) # 1 chamada de função, 1 atribuição
    y_digitos = contar_digitos(y) # 1 chamada de função, 1 atribuição
    return max(x_digitos, y_digitos) # 1 operação

def contar_digitos(num):
    if num == 0: # 1 comparação
        return 1 # 1 retorno
    contagem = 0 # 1 atribuição
    n = num # 1 atribuição
    while n != 0: # 1 comparação
        n //= 10 # 1 operação, 1 atribuição
        contagem += 1 # 1 operação, 1 atribuição
    return contagem # 1 operação de retorno

def main():
    print("Resultado de 5 * 6:", karatsuba(5, 6))
    print("Resultado de 123 * 456:", karatsuba(123, 456))
    print("Resultado de 123456789 * 987654321:", karatsuba(123456789, 987654321))

if __name__ == "__main__":
    main()