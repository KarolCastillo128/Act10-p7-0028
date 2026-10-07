# Karol Castillo NC = 0028
# ==========================================
# 1. CONDICIÓN IF
# ==========================================
print("+-+-+-+-+-+-+ 1. CONDICION IF -+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 1
edad = 20

if edad >= 18:
    print("Ejemplo 1: Eres mayor de edad")


# Ejemplo 2
temperatura = 15

if temperatura < 20:
    print("Ejemplo 2: Hace frío")


# ==========================================
# 2. CONDICIÓN IF + ELIF
# ==========================================
print("+-+-+-+-+-+-+ 2. CONDICION IF + ELIF -+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 1
calificacion = 8

if calificacion == 10:
    print("Ejemplo 1: Excelente")
elif calificacion >= 6:
    print("Ejemplo 1: Aprobado")


# Ejemplo 2
dia = 3

if dia == 1:
    print("Ejemplo 2: Lunes")
elif dia == 2:
    print("Ejemplo 2: Martes")
elif dia == 3:
    print("Ejemplo 2: Miércoles")


# ==========================================
# 3. CONDICIÓN IF + ELSE
# ==========================================
print("+-+-+-+-+-+-+ 3. CONDICION IF + ELSE -+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 1
numero = 10

if numero % 2 == 0:
    print("Ejemplo 1: El número es par")
else:
    print("Ejemplo 1: El número es impar")


# Ejemplo 2
edad = 16

if edad >= 18:
    print("Ejemplo 2: Puedes votar")
else:
    print("Ejemplo 2: No puedes votar")


# ==========================================
# 4. BUCLE FOR
# ==========================================
print("+-+-+-+-+-+-+ 4. BUCLE FOR -+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 1
for numero in range(1, 6):
    print("Ejemplo 1:", numero)


# Ejemplo 2
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print("Ejemplo 2:", fruta)


# ==========================================
# 5. BUCLE WHILE
# ==========================================
print("+-+-+-+-+-+-+ 5. BUCLE WHILE -+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 1
contador = 1

while contador <= 5:
    print("Ejemplo 1:", contador)
    contador += 1


# Ejemplo 2
numero = 5

while numero > 0:
    print("Ejemplo 2:", numero)
    numero -= 1

print("¡Despegue!")

print("Karol Castillo NC = 0028")