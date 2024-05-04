import pandas as pd

cotizacion = pd.read_csv('bd/precios.csv')

def consultarCotizacion(destino_consultado, temporada, cantidad_personas, cantidad_dias):
    destino_consultado = cotizacion.query(f"Destino == '{destino_consultado}'").head(1)
    print(destino_consultado)
    if temporada =='TemporadaAlta':
        precio = destino_consultado["Temp_Alta"]
    if temporada =='TemporadaBaja':
        precio = destino_consultado["Temp_Baja"]
    
    costo =  precio * cantidad_personas * cantidad_dias
    return costo
