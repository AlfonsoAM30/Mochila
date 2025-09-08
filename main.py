
def funcionPorPeso(mochila):
    mochi = []
    for peso, valor in mochila.items():
        n = float(peso) / float(valor)
        mochi.append(n)
    return mochi

mochila = {}
pesos = []
valores = []
n = int(input("Dame el numero de objetos: "))
for _ in range(n):
    peso, valor = map(int, input().strip().split())
    mochila[valor] = peso
    pesos.append(peso)
    valores.append(valor)


pesoTotal = int(input("Dame el número máximo de peso en la mochila: "))
valorTotal = 0
mochi = funcionPorPeso(mochila)
final = [0] * len(mochi)
cuenta = 0
val = 0.9
for _ in range(n):
    maximo = mochi.index(max(mochi))
    mochi[maximo] = 0
    if pesos[maximo] < pesoTotal:
        final[maximo] = 1
        pesoTotal -= pesos[maximo]
        valorTotal += valores[maximo]
    else:
        if pesoTotal == 0:
            break
        while pesos[maximo] > pesoTotal:
            peso = pesos[maximo] * val
            val -= 0.1
            cuenta += 1
            if peso <= pesoTotal:
                break
        if val <= 0:
            break
        val = 0.9
        cuenta2 = 10 - cuenta
        cuenta2 /= 10
        final[maximo] = cuenta2
        pesoTotal -= pesos[maximo]
        valorTotal += valores[maximo] * cuenta2

print(final)
print(valorTotal)
