from itertools import combinations
import pandas as pd
from dotenv import load_dotenv
from os import getenv


class AnaliseCombinatoria:
    load_dotenv()

    def __init__(self, lst_campos: list, n_jogos_por_res: int,
                 dados: dict) -> None:
        self.__campos = lst_campos
        self.__n_jogos_linha = n_jogos_por_res
        self.__dados = dados
        self.__linha_res = {}

    def combinar_campos(self) -> None:
        campos = combinations(self.__campos, self.__n_jogos_linha)
        linha = 0
        for c in campos:
            linha += 1
            res = []
            for value in c:
                res.extend(self.__dados[value])
            self.__linha_res[linha] = res
        table = getenv("loc_name_xls")
        df = pd.DataFrame.from_dict(data=self.__linha_res, orient='index')
        df.to_excel(table)
