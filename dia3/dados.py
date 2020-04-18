#!/usr/bin/env python

from sys import argv
from random import randint

usage = '''Uso:
dados.py numtiradas [dados]

- numtiradas Parámetro obligatorio
             É o número de tiradas a simular, ten que ser un enteiro positivo.

- dados Parámetro opcional
        E o número de dados que imos usar, ten que ser un enteiro maior que 2
'''


def validarArgumentos():
    dados = 2

    if len(argv) < 2 :
        raise SystemExit(usage)

    try:
        tiradas = int(argv[1])
        if len(argv) == 3:
            dados = int(argv[2])
    except Exception as identifier:
        print(type(identifier))
        raise SystemExit(usage)

    return(tiradas,dados)

def main():
    tiradas, dados = validarArgumentos()

    print(f"Simulacion {tiradas} tiradas de {dados} datos.")

    results = {i: 0 for i in range(dados, (6 * dados) + 1)}
    
    for i in range(tiradas):
        result = 0 
        for j in range(dados):
            result = result + randint(1,6)
        results[result] = results[result] + 1

    maximo_valor_key = max(results.keys())
    maximo_valor_values = max(results.values())
    for i in results:
        estrellas = round((results[i] * 20 ) / maximo_valor_values)
        estrellas_str = "*" * estrellas
        print(  str(i).zfill(len(str(maximo_valor_key))) + 
                " : [" + str(results[i]).zfill(len(str(maximo_valor_values))) + "] " + 
                estrellas_str
            ) 
       



if __name__ == "__main__":
    main()