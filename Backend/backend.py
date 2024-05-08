import pandas as pd
import locale

cotizacion = pd.read_csv('bd/precios.csv')

def consultarCotizacion(destino_consultado, temporada, cantidad_personas, cantidad_dias):
    locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
    destino_consultado = cotizacion.query(f"Destino == '{destino_consultado}'").head(1)
    print(destino_consultado)
    if temporada =='TemporadaAlta':
        precio = destino_consultado["Temp_Alta"]
    if temporada =='TemporadaBaja':
        precio = destino_consultado["Temp_Baja"]
    
    costo =  precio * cantidad_personas * cantidad_dias
    costo = costo.iloc[0]
    valor_formateado = locale.currency(costo, grouping=True)

    return valor_formateado