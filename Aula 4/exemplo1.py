A = int(input("Medida lado A:"))
B = int(input("Medida lado B:"))
C = int(input("Medida lado C:"))

if (A + B < C) or (A + C < B) or (B + C < A):
    print("Triangulo não existe")

if (A == B) and (C == B):
    print("Triangulo equilatero")

elif (A == B) or (A == C) or (B == C):
    print("Triangulo isosceles")

if A != B and B != C and A != C:
    print("Triangulo escaleno")