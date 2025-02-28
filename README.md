# FPAA-trabalho-individual-01
Repositório do primeiro trabalho individual da disciplina de fundamentos de projeto e análise de algoritmos


# Algoritmo de Karatsuba (Python)
> [Implementação em Rust](karatsuba_rust/README.md)

O **algoritmo de Karatsuba** é um método eficiente para multiplicar números grandes, reduzindo o número de operações necessárias em comparação com o método tradicional de multiplicação. Ele foi desenvolvido por Anatolii Alexeevitch Karatsuba em 1960 e é um exemplo clássico de **divisão e conquista**, uma técnica que divide um problema em subproblemas menores, resolve-os recursivamente e combina os resultados.

---

## Como Funciona o Algoritmo?

O algoritmo de Karatsuba baseia-se na ideia de que a multiplicação de dois números grandes pode ser simplificada dividindo-os em partes menores e realizando operações mais simples. A seguir, descrevemos os passos principais:

1. **Divisão dos Números**:
   - Dados dois números \(x\) e \(y\), cada um é dividido em duas partes de tamanho aproximadamente igual.
   - Por exemplo, se \(x\) e \(y\) têm \(n\) dígitos, eles são divididos em:
     \[
     x = 10^m \cdot x_1 + x_0
     \]
     \[
     y = 10^m \cdot y_1 + y_0
     \]
     Onde \(m = \lfloor n/2 \rfloor\), \(x_1\) e \(y_1\) são as partes "altas", e \(x_0\) e \(y_0\) são as partes "baixas".

2. **Multiplicações Recursivas**:
   - O algoritmo realiza três multiplicações recursivas:
     \[
     z_0 = x_0 \cdot y_0
     \]
     \[
     z_1 = (x_1 + x_0) \cdot (y_1 + y_0)
     \]
     \[
     z_2 = x_1 \cdot y_1
     \]

3. **Combinação dos Resultados**:
   - O resultado final é obtido combinando as três multiplicações:
     \[
     x \cdot y = z_2 \cdot 10^{2m} + (z_1 - z_2 - z_0) \cdot 10^m + z_0
     \]

---

## Vantagens do Algoritmo

- **Redução de Operações**:
  - O método tradicional de multiplicação requer \(O(n^2)\) operações para multiplicar dois números de \(n\) dígitos.
  - O Karatsuba reduz isso para \(O(n^{\log_2 3}) \approx O(n^{1.585})\), o que é significativamente mais eficiente para números grandes.

- **Aplicações**:
  - É amplamente utilizado em sistemas de computação que lidam com números muito grandes, como criptografia e aritmética de precisão arbitrária.

---

## Métodos para Contar Operações

Para contar as operações no algoritmo de Karatsuba, seguimos os seguintes passos:

1. **Identificação de Operações**:
   - Cada operação básica (adição, subtração, multiplicação, divisão, etc.) é contabilizada.
   - Operações de atribuição e chamadas de função também são consideradas.

2. **Análise por Função**:
   - A função `karatsuba` é analisada linha por linha, contando as operações em cada passo.
   - Funções auxiliares, como `dividir` e `contar_digitos`, também são incluídas na contagem.

3. **Somatório**:
   - O total de operações é obtido somando as operações de todas as funções envolvidas.

---

## Cálculo da Complexidade Ciclomática

A **complexidade ciclomática** é uma métrica que mede o número de caminhos independentes em um programa. Para calcular a complexidade ciclomática do algoritmo de Karatsuba, utilizamos a seguinte abordagem:

1. **Construção do Grafo de Controle de Fluxo**:
   - O código é representado como um grafo, onde os nós são blocos de código e as arestas são transições entre eles.
   - Por exemplo, condicionais (`if`) e loops (`while`) criam bifurcações no grafo.

2. **Aplicação da Fórmula**:
   - A complexidade ciclomática \(V(G)\) é calculada usando a fórmula:
     \[
     V(G) = E - N + 2
     \]
     Onde:
     - \(E\) = número de arestas.
     - \(N\) = número de nós.

3. **Resultado**:
   - No caso do algoritmo de Karatsuba, a complexidade ciclomática é **1**, indicando um fluxo de controle simples e direto.

---

## Exemplo de Implementação em Python

[Algoritmo implementado em python](karatsuba_python/main.py)

## Análise do Algoritmo de Karatsuba

### Quantidade de Operações

#### Função `karatsuba(x, y)`:
- **Total de operações:** 30 operações.

#### Função `dividir(num, m)`:
- **Total de operações:** 7 operações.

#### Função `max_numero_digitos(x, y)`:
- **Total de operações:** 5 operações.

#### Função `contar_digitos(num)`:
- **Caso base (`num == 0`)**: 2 operações.
- **Caso geral**: 8 + 5 * número de dígitos.

### Complexidade Ciclomática

#### Grafo do algoritmo `karatsuba`:
- **Nós:** 12
- **Arestas:** 11
- **Complexidade ciclomática:** \(V(G) = E - N + 2 = 11 - 12 + 2 = 1\)

### Grafo de Controle de Fluxo

![grafo_karatsuba](img/grafo_python.png)

### Tabela de Operações

A tabela de operações permanece a mesma, mas agora as chamadas recursivas estão claramente representadas no grafo:

| Número | Operação                                                                 |
|--------|-------------------------------------------------------------------------|
| 1      | `if x < 10 or y < 10` (2 operações)                                     |
| 2      | `return x * y` (1 operação)                                             |
| 3      | `n = max_numero_digitos(x, y)` (1 chamada de função, 1 atribuição)      |
| 4      | `m = n // 2` (1 operação)                                               |
| 5      | `alta1, baixa1 = dividir(x, m)` (1 chamada de função, 2 atribuições)    |
| 6      | `alta2, baixa2 = dividir(y, m)` (1 chamada de função, 2 atribuições)    |
| 7      | `z0 = karatsuba(baixa1, baixa2)` (1 chamada de função, 1 atribuição)    |
| 8      | `z1 = karatsuba((baixa1 + alta1), (baixa2 + alta2))` (2 operações, 1 chamada de função, 1 atribuição) |
| 9      | `z2 = karatsuba(alta1, alta2)` (1 chamada de função, 1 atribuição)      |
| 10     | `resultado = (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0` (7 operações, 1 atribuição) |
| 11     | `return resultado` (1 operação)                                         |
| 12     | `divisor = 10 ** m` (1 operação, 1 atribuição)                         |
| 13     | `alta = num // divisor` (1 operação, 1 atribuição)                     |
| 14     | `baixa = num % divisor` (1 operação, 1 atribuição)                     |
| 15     | `return alta, baixa` (1 operação)                                       |
| 16     | `x_digitos = contar_digitos(x)` (1 chamada de função, 1 atribuição)     |
| 17     | `y_digitos = contar_digitos(y)` (1 chamada de função, 1 atribuição)     |
| 18     | `return max(x_digitos, y_digitos)` (1 operação)                         |
| 19     | `if num == 0` (1 comparação)                                            |
| 20     | `return 1` (1 retorno)                                                  |
| 21     | `contagem = 0` (1 atribuição)                                           |
| 22     | `n = num` (1 atribuição)                                                |
| 23     | `while n != 0` (1 comparação)                                           |
| 24     | `n //= 10` (1 operação, 1 atribuição)                                   |
| 25     | `contagem += 1` (1 operação, 1 atribuição)                              |
| 26     | `return contagem` (1 operação de retorno)                               |

## Estrutura do Repositório

```
├── karatsuba_python
│   ├── main.py
│   ├── __pycache__
│   │   ├── main.cpython-313.pyc
│   │   └── test_karatsuba.cpython-313-pytest-8.3.4.pyc
│   ├── requirements.txt
│   ├── test_karatsuba.py
│   └── venv
│       ├── bin
│       ├── include
│       ├── lib
│       ├── lib64 -> lib
│       └── pyvenv.cfg
├── karatsuba_rust
│   ├── Cargo.lock
│   ├── Cargo.toml
│   ├── src
│   │   └── main.rs
│   └── target
│       ├── CACHEDIR.TAG
│       └── debug
├── README.md
├── test.sh
└── Trabalho individual 1 - Valor 5 pontos.pdf
```

## Licença

Este projeto está licenciado sob a Licença MIT.
```
