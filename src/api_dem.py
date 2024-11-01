import sys
import os
import http.client
import json
import pandas as pd # type: ignore

import sys
sys.path.append("../")
from src import support as su

def get_datos_demanda_evolucion(input_anio, geo_ids):

    result = dict()
    try:
        anio = input_anio

        conn = http.client.HTTPSConnection("apidatos.ree.es")

        headers = {
            "Accept": "application/json;",
            "Content-Type": "application/json",
            "Host": "apidatos.ree.es"
        }

        url = f"/es/datos/demanda/evolucion?start_date={input_anio}-01-01T00:00&end_date={input_anio}-12-31T23:59&time_trunc=month&geo_limit=ccaa&geo_ids={geo_ids}"

        conn.request("GET", url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        dicc_datos = json.loads(data.decode("utf-8"))

        result = dicc_datos['included'][0]['attributes']['values']

    except:
        print(f"Error al hacer peticion api, en get_datos: {url}")
    return result

def alamacenar_datos_in_csv():
     list_anios=[2019,2021,2022]
     for x, y in su.cod_comunidades.items():
        for i in list_anios:
            diccionario = get_datos_demanda_evolucion(i, y)
            df_final = pd.DataFrame(diccionario)
            df_final.to_csv(f"../data/demanda/{i}_demanda_evolucion_{x}_{y}.csv")