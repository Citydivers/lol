def constructor(color, ancho, alto, x, y, estado):
    bloque = {"tipo": "bloque"}
    setColor(bloque, color)
    setAncho(bloque, ancho)
    setAlto(bloque, alto)
    setX(bloque, x)
    setY(bloque, y)
    setEstado(bloque, estado)
    return bloque

def checkTipo(objeto):
    return True if "tipo" in objeto and objeto["tipo"] == "bloque" else False

def getColor(objeto):
    if checkTipo(objeto):
        return objeto["color"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen color.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setColor(objeto, nuevo_color):
    if type(nuevo_color) != tuple or len(nuevo_color) != 3:
        print("Valor invalido: Los colores van en una tupla de longitud 3.")
        return

    for i in range(3):
        if type(nuevo_color[i]) != int or nuevo_color[i] < 0 or nuevo_color[i] > 255:
            print("Valor invalido: El código de color RGB son numeros enteros >= 0 y <= 255.")
            return

    if checkTipo(objeto):
        objeto["color"] = nuevo_color
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene color.")
    else:
        print("El objeto pasado no tiene tipo.")
    return objeto

def getAncho(objeto):
    if checkTipo(objeto):
        return objeto["ancho"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen ancho.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setAncho(objeto, nuevo_ancho):
    if type(nuevo_ancho) != int or nuevo_ancho <= 0:
        print("Valor invalido: El ancho tiene que ser un valor entero positivo.")
    elif checkTipo(objeto):
        objeto["ancho"] = nuevo_ancho
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene ancho.")
    else:
        print("El objeto pasado no tiene tipo.")
    return objeto

def getAlto(objeto):
    if checkTipo(objeto):
        return objeto["alto"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen alto.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setAlto(objeto, nuevo_alto):
    if type(nuevo_alto) != int or nuevo_alto <= 0:
        print("Valor invalido: El alto tiene que ser un valor entero positivo.")
    elif checkTipo(objeto):
        objeto["alto"] = nuevo_alto
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene alto.")
    else:
        print("El objeto pasado no tiene tipo.")
    return objeto

def getX(objeto):
    if checkTipo(objeto):
        return objeto["x"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen x.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setX(objeto, nuevo_x):
    if type(nuevo_x) != int and type(nuevo_x) != float:
        print("Valor invalido: X tiene que ser un valor numérico.")
    elif checkTipo(objeto):
        objeto["x"] = nuevo_x
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene x.")
    else:
        print("El objeto pasado no tiene x.")
    return objeto

def getY(objeto):
    if checkTipo(objeto):
        return objeto["y"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen y.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setY(objeto, nuevo_y):
    if type(nuevo_y) != int and type(nuevo_y) != float:
        print("Valor invalido: Y tiene que ser un valor numérico.")
    elif checkTipo(objeto):
        objeto["y"] = nuevo_y
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene y.")
    else:
        print("El objeto pasado no tiene x.")
    return objeto

def getEstado(objeto):
    if checkTipo(objeto):
        return objeto["estado"]
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tienen estado.")
    else:
        print("El objeto pasado no tiene tipo.")
    return None

def setEstado(objeto, nuevo_estado):
    if type(nuevo_estado) != int or nuevo_estado <= 0:
        print("Valor invalido: El estado tiene que ser un valor entero positivo.")
    elif checkTipo(objeto):
        objeto["estado"] = nuevo_estado
    elif "tipo" in objeto:
        print("Objetos de tipo", objeto["tipo"], "no tiene estado.")
    else:
        print("El objeto pasado no tiene tipo.")
    return objeto

def getTipo(objeto):
    if "tipo" in objeto:
        return objeto["tipo"]
    else:
        print("El objeto pasado no tiene tipo.")
    return None
