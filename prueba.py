pro = ["El", "La", "Ellos", "Ellas"]
sujeto = ["niño", "perro","niña", "gata"]
verbo = ["come", "juega", "corre", "brinca"]
cosa = ["feliz", "manzanas", "croquetas", "solo"]

ruta = 'hello.txt'
archivo = open (ruta, 'r')

Oracion = (archivo.read())

print(Oracion)

Oracion = Oracion.split(" ")

correcta = "  "
print(Oracion)
print(  )

for i in range(len(pro)):
    for j in range(len(Oracion)):
        if (Oracion [j] == pro[i]):
            correcta = Oracion[j]


for i in range(len(sujeto)):
    for j in range(len(Oracion)):
        if (Oracion [j] == sujeto[i]):
            correcta = correcta+" " + Oracion[j]

for i in range(len(verbo)):
    for j in range(len(Oracion)):
        if (Oracion [j] == verbo[i]):
            correcta = correcta +" "+ Oracion[j]


for i in range(len(cosa)):
    for j in range(len(Oracion)):
        if (Oracion [j] == cosa [i]):
            correcta = correcta+" " + Oracion[j]

print(correcta)