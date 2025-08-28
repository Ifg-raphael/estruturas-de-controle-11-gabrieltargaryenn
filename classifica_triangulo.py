# Sua solução aqui

# Leitura dos valores
a = int(input())
b = int(input())
c = int(input())

# Verifica se os lados formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Verifica o tipo de triângulo
    if a == b and b == c:
        print("equilátero")
    elif a == b or b == c or a == c:
        print("isósceles")
    else:
        print("escaleno")
else:
    print("Não forma triângulo")

