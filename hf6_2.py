bekert = input("Adj meg egy szót vagy szöveget az angol ABC betűivel: ")
nagybetuk = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
kisbetuk = []
kiirando = []


for i in range(len(nagybetuk)):
    pici = nagybetuk[i].lower()
    kisbetuk.append(pici)

for a in range(len(bekert)):
    for b in range(len(nagybetuk)):
        if bekert[a] == nagybetuk[b]:
            kicsi = bekert[a].lower()
            kiirando.append(kicsi)
    for c in range(len(kisbetuk)):
        if bekert[a] == kisbetuk[c]:
            nagy = bekert[a].upper()
            kiirando.append(nagy)
print(kiirando)

