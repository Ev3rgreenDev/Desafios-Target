import json

with open('dados.json', 'r') as file:
    data = json.load(file)  

filtro = [entry for entry in data if entry['valor'] > 0]

menorValor = min(filtro, key=lambda x: x['valor'])

maiorValor = max(data, key=lambda x: x['valor'])

media = sum(entry['valor'] for entry in filtro) / len(filtro)

acimaMedia = [entry for entry in filtro if entry['valor'] > media]
numAcimaMedia = len(acimaMedia)


print(f"Menor valor de faturamento ocorrido em um dia do mês: Dia {menorValor['dia']} com valor de {menorValor['valor']}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: Dia {maiorValor['dia']} com valor de {maiorValor['valor']}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {numAcimaMedia}")