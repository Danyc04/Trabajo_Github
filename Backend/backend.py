import pandas as pd

#importamos el archivo de departamentos
cotizacion = pd.read_csv('Trabajo\\bd\\precios.csv')
print(cotizacion)


def consultarCotizacion(ciudad_buscada):
    #hacemos consulta del departamento buscado
    busqueda_ciudad = cotizacion.query(f"Destino == '{ciudad_buscada.upper()}'")
    return busqueda_ciudad
