def two_fer(name = "you"):
    try:
        salida = "One for " + name + ", one for me."

        return salida
    except Exception as identifier:
        raise Exception("Meaningful message indicating the source of the error")
