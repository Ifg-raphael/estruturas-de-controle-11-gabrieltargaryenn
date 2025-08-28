# Sua solução aqui

# Leitura dos valores
a = int(input('escreva um valor'))
b = int(input('escreva um valor'))
c = int(input('escreva um valor'))

# Verifica se forma triângulo
if a < b + c or b < a + c or c < a + b:
    # Verifica o tipo de triângulo
    if a == b == c:
        print("equilátero")
    elif a == b or b == c or a == c:
        print("escaleno")
    else:
        print("isósceles")
else:
    print("Não forma triângulo")
