import pandas as pd


#importamos el archivo de departamentos
cotizacion = pd.read_csv('bd\precios.csv')

def consultarCotizacion(destino_consultado, temporada, cantidad_personas, cantidad_dias):
    destino_consultado = cotizacion.query(f"Destino == '{destino_consultado.upper()}'")
    
    precio = cantidad_personas*cantidad_dias
    # if result:
    #     ciudad_seleccion = result.get['Temp_Alta']
    return "sdf"