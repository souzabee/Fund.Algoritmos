# def media (x, y, z, w):
#     if w == "A":
#        media_a = (x + y + z) / 3
#        return media_a
#     elif w == "P":
#         media_p = ((x * 5) + (y * 3) + (z * 2)) / 10
#         return media_p


# def quadrado (x):
#     for indice in range (len(x)):
#         x[indice] = x[indice] ** 2
#     return x

# z = []
# n = []
# while True:
#     num = int(input(""))
#     if num == 0:
#         break
#     if num < 0:
#         n.append(num)
#     if num > 0:
#         z.append(num)
    



# print(n + z)

print("Digite o vetor 1: ")


v1 = []
v2 = []
for a in range (3):
    n = int(input())
    v1.append(n)

print("Digite o vetor 2:")

for b in range(3):
    n = int(input())
    v2.append(n)

def linear(v1, v2):
    total = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])
    return total

print(linear(v1,v2))




