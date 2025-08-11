# Ejemplo de uso de clases. para organizar el codigo y agrupar datos(atributos) y funciones(metodos) relacionados
# creamos objetos similares pero independientes, y cada objeto "sabe" como hacer ciertas cosas. Ej, una auto sabe como acelerar 

class Auto:   # define una clase llamada AUTO, crea el "molde"
    def __init__(self,color,marca):  #metodo constructor. color y marca son datos que le paso para darle caracteristicas cuando se crea el auto
        self.color = color 
        self.marca = marca 
        self.velocidad = 0

# con los metodos definimos una función que pertenece al objeto

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self):
        self.velocidad = 0


def puntos_fuerza_inicial(civilizacion:str) -> int :
    if civilizacion == "chinos" :
        puntos = 300
    elif civilizacion == "ingleses" :
        puntos = 350
    elif civilizacion == "bizantinos":
        puntos = 405
    return puntos 


def civilizacion_inicial(civilizacion:str) :
    if civilizacion == "chinos":
        cantidad_piqueros = 2
        cantidad_arqueros = 25
        cantidad_caballeros = 2 
    
    elif civilizacion == "ingleses":
        cantidad_piqueros = 10
        cantidad_arqueros = 10
        cantidad_caballeros = 10
    
    elif civilizacion == "bizantinos":
        cantidad_piqueros = 5
        cantidad_arqueros = 8
        cantidad_caballeros = 15

    return (cantidad_piqueros,cantidad_arqueros,cantidad_caballeros)



# para agregar las unidades como objetos de una clase dentro de mi diccionario EJERCITO, 
# primero defino la clase UNIDAD. luego, para cada tipo de unidad (piquero, arquero, caballero) creo las instancias correspondientes y agregarlas a una lista o estructura dentro del diccionaro EJERCITO 

# la clase es como el molde que define las caracteristicas y comportamientos comnes(atributos y metodos) 

#la instancia es un objeto concreto creado a partir de una clase. 

# en mi caso, tengo la clase UNIDAD que define con atributos como TIPO, PUNTOS_FUERZA .
# para representar todas las unidades de un ejercito, creo muchas instancias (objetos) de la clase UNIDAD y los guardo en una lista
# entonces, la lista tiene muchos objetos UNIDAD diferentes, cada uno representando un piquero, arquero o caballero con sus puntos, años de vida, etc. 


"""
Acceder a las propiedades y métodos de un auto específico
Si querés saber el color de auto1:

print(auto1.color)    # Imprime: rojo
Si querés acelerar el auto2 en 30 km/h:

auto2.acelerar(30)
print(auto2.velocidad)  # Imprime: 30

"""


# desarrollo borrador del modelado 


unidades_iniciales = {
    'chinos' : {'piqueros': 2, 'arqueros': 25, 'caballeros': 2},
    'ingleses' : {'piqueros': 10, 'arqueros': 10, 'caballeros': 10},
    'bizantinos' : {'piqueros': 5, 'arqueros': 8, 'caballeros': 15}
}



def crear_ejercito(civilizacion: str) -> dict:
# inicializo las estructuras. el diccionario del ejercito, las listas de unidades.
    ejercito = {}
    piqueros = []
    arqueros = []
    caballeros = []

# obtener cantidades segun civilizacion 
    cantidad_piqueros = unidades_iniciales[civilizacion]['piqueros'] 
    cantidad_arqueros = unidades_iniciales[civilizacion]['arqueros']
    cantidad_caballeros = unidades_iniciales[civilizacion]['caballeros']

    for i in range(cantidad_piqueros):
        piqueros.append(Unidad(tipo = 'piquero', fuerza= 5, años_vida=0))
        
    for i in range(cantidad_arqueros):
        arqueros.append(Unidad(tipo = 'arquero', fuerza= 10, años_vida=0))
        
    for i in range(cantidad_caballeros):
        caballeros.append(Unidad(tipo = 'caballero', fuerza= 20, años_vida=0))

# creo las claves - valor del ejercito 
    ejercito['civilizacion']= civilizacion
    ejercito['monedas'] = 1000
    ejercito['historial batallas'] = []
    ejercito['unidades'] = [piqueros,arqueros,caballeros]
    return ejercito
    





# definocion de la clase UNIDAD 

class Unidad:
    def __init__(self, tipo, fuerza, años_vida):
        self.tipo = tipo 
        self.fuerza = fuerza 
        self.años_vida = años_vida

    def __repr__(self):
        return f'Unidad tipo = {self.tipo} , fuerza={self.fuerza}, años_vida={self.años_vida}'

    def entrenamiento(self):
        if self.tipo == "piquero":
            self.años_vida += 1
            beneficio = 3
        elif self.tipo == "arquero":
            self.años_vida += 2
            beneficio = 7
        elif self.tipo == "caballero":
            self.años_vida += 5
            beneficio = 10
        else:
            beneficio = 0
            
        self.fuerza += beneficio 

    def costo_entrenamiento(self):
        if self.tipo== "piquero":
            costo = 10
        elif self.tipo== "arquero":
            costo= 20
        elif self.tipo == "caballero":
            costo= 30
        else:
            costo = 0
        return costo 

    def transformacion(self):
        if self.tipo == "piquero":
            self.tipo = "arquero" 
            self.fuerza = 10
            self.años_vida += 5
            
        elif self.tipo == "arquero":
            self.tipo = "caballero"
            self.fuerza = 20
            self.años_vida += 5
            

    def costo_transformacion(self):
        if self.tipo== "piquero":
            costo_t = 30
        elif self.tipo== "arquero":
            costo_t= 40
        else:
            costo_t = 0
        return costo_t
    
        

def entrenar(ejercito:dict,tipo_unidad: int, numero_unidad: int) :

    unidad = ejercito['unidades'][tipo_unidad][numero_unidad] 
    costo = unidad.costo_entrenamiento()

    if ejercito['monedas'] >= costo:
        unidad.entrenamiento()
        billetera(ejercito,-costo)
    else:
        print("no hay monedas suficientes")


def transformar(ejercito:dict, tipo_unidad:int, numero_unidad:int) :
    unidad = ejercito['unidades'][tipo_unidad][numero_unidad]
    costo_trans = unidad.costo_transformacion()

    if ejercito['monedas'] >= costo_trans:
        unidad.transformacion()
        billetera(ejercito,-costo_trans)
    else:
        print("no hay monedas suficientes")



def billetera(ejercito:dict,cantidad:int):
    ejercito['monedas'] += cantidad


def preguntar_años_vida(ejercito:dict,tipo:int,unidad:int):
    unidad = ejercito['unidades'][tipo][unidad]
    años_de_vida = unidad.años_vida
    return años_de_vida


def puntos_fuerza(ejercito: dict):
    puntos = 0
    for tipos in ejercito['unidades']:
        for unidad in tipos:
            puntos += unidad.fuerza
    return puntos


def perder_unidad(ejercito:dict):
    
    mayor = ejercito['unidades'][0][0]
    tipo_mayor = 0
    unidad_mayor = 0

    for t in range(len(ejercito['unidades'])):
        for u in range(len(ejercito['unidades'][t])):

            if ejercito['unidades'][t][u].fuerza > mayor.fuerza:
                mayor = ejercito['unidades'][t][u]
                tipo_mayor = t
                unidad_mayor = u
    
    del ejercito['unidades'][tipo_mayor][unidad_mayor]




def batalla(ejercito1:dict,ejercito2:dict):
    puntos1 = puntos_fuerza(ejercito1)
    puntos2 = puntos_fuerza(ejercito2)

    nombre1 = ejercito1['civilizacion']  
    nombre2 = ejercito2['civilizacion']

    if puntos1 > puntos2:  
        billetera(ejercito1,100)
        historial1 = { 'oponente': nombre2, 'resultado': "ganador" }
        ejercito1['historial batallas'].append(historial1)
        print("¡El ejercito 1 es ganador!")

        historial2 = { 'oponente': nombre1, 'resultado': "perdedor" }
        ejercito2['historial batallas'].append(historial2)

        perder_unidad(ejercito2)
        perder_unidad(ejercito2)
       

    elif puntos2 > puntos1:  
        billetera(ejercito2,100) 
        historial2 = { 'oponente': nombre1, 'resultado': "ganador" }
        ejercito2['historial batallas'].append(historial2)
        print("¡El ejercito 2 es ganador!")

        # perdida perdedor 
        perder_unidad(ejercito1)
        perder_unidad(ejercito1)
        historial1 = { 'oponente': nombre2, 'resultado': "perdedor" }
        ejercito1['historial batallas'].append(historial1)

    elif puntos1 == puntos2:
        perder_unidad(ejercito1)
        perder_unidad(ejercito2)
        print("¡Es un empate!")

        historial1 = {'oponente': nombre2, 'resultado': "empate"}
        ejercito1['historial batallas'].append(historial1)

        historial2 = {'oponente': nombre1, 'resultado': "empate"}
        ejercito2['historial batallas'].append(historial2)
    


ejercito_chino = crear_ejercito("chinos")

ejercito_ingles = crear_ejercito("ingleses")

print("Puntos de fuerza iniciales de cada army")
print(puntos_fuerza(ejercito_chino))
print(puntos_fuerza(ejercito_ingles))


print("billetera inicial de cada army ")
billetera1 = ejercito_chino['monedas']
billetera2 = ejercito_ingles['monedas']
print(billetera1)
print(billetera2)

entrenar(ejercito_chino,0,1)
entrenar(ejercito_ingles,1,1)
entrenar(ejercito_chino,2,1) 

transformar(ejercito_chino,0,1)
transformar(ejercito_ingles,1,3)
transformar(ejercito_ingles,2,7)

print("puntos de fuerza despues de entrenar y transformar ")
print(puntos_fuerza(ejercito_ingles))
print(puntos_fuerza(ejercito_chino))


print("billetera despues de partida")
billetera0 = ejercito_chino['monedas']
billetera3 = ejercito_ingles['monedas']
print(billetera0)
print(billetera3)


print("pregunto por años de vida a una unidad")


print("los años de vida de determinadas unidades son:")

print("unidad1:")
print(preguntar_años_vida(ejercito_chino,0,1))
 

print("unidad2:")
print(preguntar_años_vida(ejercito_chino,2,1))

print("unidad3:")
print(preguntar_años_vida(ejercito_ingles,1,1))


print("batalla final ")

print(batalla(ejercito_chino,ejercito_ingles))


print("billetera despues de partida")
billetera7 = ejercito_chino['monedas']
billetera8 = ejercito_ingles['monedas']
print(billetera7)
print(billetera8)



print("Puntos de fuerza despues de batalla de cada army")
print(puntos_fuerza(ejercito_chino))
print(puntos_fuerza(ejercito_ingles))
