votos = [0, 0, 0, 0, 0, 0, 0]

while True:
    voto = int(input("Digite seu voto: "))
    if voto == 0:
        break
    
    elif voto == 1:
        votos[1] += 1
    
    elif voto == 2:
        votos[2] += 1
    
    elif voto == 3:
        votos[3] += 1
    
    elif voto == 4:
        votos[4] += 1

    elif voto == 5:
        votos[5] += 1
    
    elif voto == 6:
        votos[6] += 1

for indice in range (len(votos)):
    total = sum(votos)
    #windows
    windows = (votos[1]/total) * 100
    #unix
    unix = (votos[2]/total) * 100
    #Linux
    linux = (votos[3]/total) * 100
    #Netware
    net = (votos[4]/total) * 100
    #macos
    mac = (votos[5]/total) * 100
    #outro
    outro = (votos[6]/total) * 100


print(windows)
print(unix)
print(linux)
print(net)
print(mac)
print(outro)
print(total)
print(votos[2])





