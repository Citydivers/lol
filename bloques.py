def constructor(color, ancho, alto, x, y, estado):
    bloque = {"tipo": "bloque"}
    setColor(bloque, color)
    setAlto(bloque, alto)
    setAncho(bloque, ancho)
    setX(bloque, x)
    setY(bloque, y)
    setEstado(bloque, estado)

    return bloque

def checkTipo(objeto):
    if "tipo" in objeto and objeto["tipo"] == "bloque":
        return True
    return False

def setX(objeto, nuevo_X):
    if type(nuevo_X) != int and type(nuevo_X) != float:
        print("Valor invalido: X tiene que ser un valor numérico.")
    elif "x" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["x"] = nuevo_X
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene x.")
    else:
        print("El objeto pasado no tiene x.")
    return objeto

def getX(objeto):
    if "x" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["x"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen x.")
    else:
        print("El objeto pasado no tiene x.")
    return None

def setY(objeto, nuevo_Y):
    if type(nuevo_Y) != int and type(nuevo_Y) != float:
        print("Valor invalido: Y tiene que ser un valor numérico.")
    elif "y" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["y"] = nuevo_Y
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene y.")
    else:
        print("El objeto pasado no tiene y.")
    return objeto

def getY(objeto):
    if "y" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["y"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen y.")
    else:
        print("El objeto pasado no tiene y.")
    return None

def setColor(objeto, nuevo_color):
    if type(nuevo_color) != tuple or len(nuevo_color) != 3:
        print("Valor invalido: Los colores van en una tupla de longitud 3.")
        return

    if "color" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
            return objeto["color"]
        elif "tipo" in objeto:
            print("Objetos de tipo", objeto["tipo"], "no tienen color.")
        else:
            print("El objeto pasado no tiene color.")
        return


def getColor(objeto):
    if checkTipo(objeto):
        return objeto["color"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen color.")
    else:
        print("El objeto pasado no tiene color.")
    return None

def setAncho(objeto, nuevo_ancho):
    if type(nuevo_ancho) != int or nuevo_ancho <= 0:
        print("Valor invalido: El tamaño tiene que ser un valor entero positivo.")
    elif "ancho" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["ancho"] = nuevo_ancho
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return objeto

def getAncho(objeto):
    if "ancho" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["ancho"]
    elif "tipo" in objeto:
        pdef constructor(color, ancho, alto, x, y, estado):
    bloque = {  "color": color,
                "ancho": ancho,
                "alto": alto,
                "x": x,
                "y": y,
                "estado": estado,
                "tipo": "bloque"    }
    return bloque

def setX(objeto, nuevo_X):
    if type(nuevo_X) != int and type(nuevo_X) != float:
        print("Valor invalido: X tiene que ser un valor numérico.")
    elif "x" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["x"] = nuevo_X
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene x.")
    else:
        print("El objeto pasado no tiene x.")
    return objeto

def getX(objeto):
    if "x" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["x"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen x.")
    else:
        print("El objeto pasado no tiene x.")
    return None

def setY(objeto, nuevo_Y):
    if type(nuevo_Y) != int and type(nuevo_Y) != float:
        print("Valor invalido: Y tiene que ser un valor numérico.")
    elif "y" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["y"] = nuevo_Y
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene y.")
    else:
        print("El objeto pasado no tiene y.")
    return objeto

def getY(objeto):
    if "y" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["y"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen y.")
    else:
        print("El objeto pasado no tiene y.")
    return None

def setColor(objeto, nuevo_color):
    if type(nuevo_color) != tuple or len(nuevo_color) != 3:
        print("Valor invalido: Los colores van en una tupla de longitud 3.")
        return

    if "color" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
            return objeto["color"]
        elif "tipo" in objeto:
            print("Objetos de tipo", objeto["tipo"], "no tienen color.")
        else:
            print("El objeto pasado no tiene color.")
        return


def getColor(objeto):
    if "color" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["color"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen color.")
    else:
        print("El objeto pasado no tiene color.")
    return None

def setAncho(objeto, nuevo_ancho):
    if type(nuevo_ancho) != int or nuevo_ancho <= 0:
        print("Valor invalido: El tamaño tiene que ser un valor entero positivo.")
    elif "ancho" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["ancho"] = nuevo_ancho
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return objeto

def getAncho(objeto):
    if "ancho" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["ancho"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return None

def setAlto(objeto, nuevo_alto):
    if type(nuevo_alto) != int or nuevo_alto <= 0:
        print("Valor invalido: El tamaño tiene que ser un valor entero positivo.")
    elif "alto" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        objeto["alto"] = nuevo_alto
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return objeto

def getAlto(objeto):
    if "alto" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["alto"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return None

def getAlto(objeto):
    if "alto" in objeto and "tipo" in objeto and objeto["tipo"] == "bloque":
        return objeto["alto"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen tamaño.")
    else:
        print("El objeto pasado no tiene tamaño.")
    return None
