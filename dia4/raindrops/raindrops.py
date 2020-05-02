def convert(number):
    try:
        salida = ''
        if not (number % 3): 
            salida = salida + "Pling"
        if (number % 5) == 0:
            salida += "Plang"
        if not (number % 7):
            salida = salida + "Plong"
        if salida == '':
            salida = str(number)

        return salida

    except Exception as identifier:
        raise Exception("Meaningful message indicating the source of the error")
