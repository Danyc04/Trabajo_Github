import pandas as pd

global cotizacion
#importamos el archivo de departamentos
cotizacion = pd.read_csv('bd\precios.csv')
print(cotizacion)


def consultarCotizacion(ciudad_buscada):
    #hacemos consulta del departamento buscado
    busqueda_ciudad = cotizacion.query(f"Destino == '{ciudad_buscada.upper()}'")
    if result:
        ciudad_seleccion = result.get['Temp_Alta']
    return cotizacion_unica