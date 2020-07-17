#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Escribir una función para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres alfabeticos,
  inclusive.
- Estar formada por mayor cantidad de letras minusculas que
  mayusculas.
- El ultimo caracter, debe ser una letra minuscula.
- La clave puede tener como maximo 2 caracteres que sean vocales.

*******************************************************************************
Aqui coloca tu Padron: 105743
Aqui coloca tu Apellido y Nombre: Lescano Nahuel
*******************************************************************************
"""

def validar_clave(clave):

    """ Casos de Prueba:

    >>> validar_clave("florencia25")
    False
    >>> validar_clave("eAEIOui")
    False
    >>> validar_clave("97532")
    False
    >>> validar_clave("1AE5b2")
    False
    >>> validar_clave("dia")
    False
    >>> validar_clave("dias")
    True
    >>> validar_clave("LuneS")
    False
    >>> validar_clave("Lunes")
    True
    >>> validar_clave("aBcdeio")
    False
    >>> validar_clave("aBcdenm")
    True
    >>> validar_clave("MartES")
    False
    >>> validar_clave("tarta")
    True
    >>> validar_clave("Nahuel")
    False
    >>> validar_clave("PiZzas")
    True
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    posicion = 0
    vocales = "aeiou"
    cont_vocales = 0
    cont_minusculas = 0
    devolver = True
    while ((posicion < len(clave)) and (4 <= len(clave) <= 10) and devolver):
        if ((clave[-1].islower() == False) or (clave[posicion].isalpha() == False) or cont_vocales > 2):
            devolver = False
        elif (clave[posicion].islower() == True):
            cont_minusculas += 1
        if (clave[posicion].lower() in vocales):
            cont_vocales += 1
        
        posicion += 1
    
    if (cont_minusculas < len(clave) // 2):
        devolver = False
    
    return devolver
# -------------------------------- Bloque Principal -----------------------------#
import doctest
doctest.testmod()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++