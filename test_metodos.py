import Bloque
import Pelota
import Plataforma

bloque = Bloque.constructor((0, 0, 0), 100, 50, 20, 20, 1)

print(Bloque.getColor(bloque))
print(Bloque.getAncho(bloque))
print(Bloque.getAlto(bloque))
print(Bloque.getX(bloque))
print(Bloque.getY(bloque))
print(Bloque.getEstado(bloque))

pelota = Pelota.constructor((0, 0, 0), 50, 20, 20, 10)

print(Pelota.getColor(pelota))
print(Pelota.getRadio(pelota))
print(Pelota.getX(pelota))
print(Pelota.getY(pelota))
print(Pelota.getVelocidad(pelota))

plataforma = Plataforma.constructor((0, 0, 0), 100, 50, 20, 20, 10)

print(Plataforma.getColor(plataforma))
print(Plataforma.getAncho(plataforma))
print(Plataforma.getAlto(plataforma))
print(Plataforma.getX(plataforma))
print(Plataforma.getY(plataforma))
print(Plataforma.getVelocidad(plataforma))
