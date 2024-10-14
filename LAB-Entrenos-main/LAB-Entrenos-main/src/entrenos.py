from datetime import datetime
import csv
from collections import namedtuple
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
def formatear_fecha(cadena):
    return datetime.strptime(cadena,'%d/%m/%Y %H:%M')
def fromatear_bool(cadena):
    if cadena=='S':
        return True
    return False
def leer_entrenos(ruta):
    resultado=[]
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        #for linea in f: 'Tenis,27/9/2020 10:17,Huelva,97,338,16.41,115,S'
        for campos in lector: #campos=['Tenis','27/9/2020 10:17','Huelva,97','338','16.41','115','S']
            registro = Entreno(campos[0],
                        formatear_fecha(campos[1]),
                        campos[2],
                        int(campos[3]),
                        int(campos[4]),
                        float(campos[5]),
                        int(campos[6]),
                        fromatear_bool(campos[7]))
            resultado.append(registro)
    return resultado
def tipos_entreno(entrenos):
    ''' 
    recibe una lista de tuplas de tipo Entreno
    y devuelve una lista con todos los tipos de entrenamientos
    en orden alfabético y sin repetir ninguno
    '''
    pass
    resultado=set()
    for entreno in entrenos :
        tipo=entreno.tipo
        resultado.add(tipo)
    return sorted(list(resultado))
    #return sorted(list({entreno.tipo for entreno in entrenos}))
def entrenos_duracion_superior(entrenos,d): 
    '''recibe una lista de tuplas de tipo Entreno y un valor entero d
    y devuelve una lista con todos los entrenamientos que tienen una duración superior
    al valor d.
    '''
    pass
    resultado=[]
    for entreno in entrenos:
        if entreno.duracion >d:
            resultado.append(entreno)
    return resultado
    '''
    #resultado alternativo
    return [entreno for entreno in entrenos if entreno.duracion>d ]
    '''
def suma_calorias(entrenos,f_inicio,f_fin):
    '''
    recibe una lista de tuplas de tipo Entreno y dos fechas f_inicio y f_fin
    y devuelve la suma de las calorías quemadas en todos los entrenamientos 
    realizados entre las dos fechas f_inicio y f_fin, ambas incluidas.
    '''
    pass
    resultado=[]
    for entreno in entrenos:
        if f_inicio<= entreno.fechahora<=f_fin:
            resultado.append(entreno.calorias)
    return sum(resultado)
    #return sum[entreno.calorias for entreno in entrenos if f_inicio<= entreno.fechahora<=f_fin]