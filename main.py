supermercados = {
    'Supermercado Assai': {
        'Arroz Prato fino': 26.0,
        'Azeite': 18.0,
        'Macarrão': 4.0,
        'Carne': 20.0
    },
    'Supermercado Tenda': {
        'Arroz Prato fino': 11.0,
        'Azeite': 17.5,
        'Macarrão': 3.5,
        'Carne': 18.0
    },
    'Supermercado Carrefour': {
        'Arroz Prato fino': 9.5,
        'Azeite': 18.5,
        'Macarrão': 4.5,
        'Carne': 22.0
    }
}

lista_compras = {
    'Arroz Prato fino': 2,
    'Azeite': 3,
    'Macarrão': 4,
    'Carne': 2
}

supermercados_mais_baratos = {produto: 'desconhecido' for produto in lista_compras}

for produto, quantidade in lista_compras.items():
    for supermercado, precos in supermercados.items():
        if produto in precos:
            preco = precos[produto]
            if supermercados_mais_baratos[produto] == 'desconhecido' or preco < supermercados[supermercados_mais_baratos[produto]][produto]:
                supermercados_mais_baratos[produto] = supermercado

print('Lista de Compras:')
for produto, quantidade in lista_compras.items():
    print(f'{produto} ({quantidade}): {supermercados_mais_baratos[produto]}')
