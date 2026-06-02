from .analise import *
from .leitura import *
from .limpeza import *
from .metricas import *
from .visualizacao import *
import pandas as pd
import numpy as np


class SalesInsight :
    def __init__(self, pd,np):
        self._pd = pd
        self._np = np

    #leitura
    def carregar_csv(self,file_path):
        df = self._pd.read_csv(file_path)
        print(f"[SalesInsight] Arquivo carregado: {file_path}")
        print(f"Registros carregados: {len(df)}")
        return df
    
    def carregar_dicionario(self, dict_data):
        df = self._pd.DataFrame(dict_data)
        print(f"[SalesInsight] Dicionário convertido para DataFrame")
        print(f"Registros carregados: {len(df)}")
        return df
    
    #inspecionar
    def inspecionar_dados(self, df):
        inspecionar_dados(df)
    
    #limpeza
    def limpar_dados(self, df):
        df_limpo, relatorio = limpar_dados(df)
        return df_limpo, relatorio
    
    def limpar_strings_com_regex(self, df):
        df_limpo = limpar_strings_com_regex(df)
        return df_limpo
    
    #analise
    def criar_colunas_derivadas(self, df):
        df = criar_colunas_derivadas(df)
        return df
    
    def calcular_metricas(self, df):
        metricas = calcular_metricas(df)
        return metricas
    
    def segmentar_clientes(self, df):
        df_segmentado = segmentar_clientes(df)
        return df_segmentado
    
    def calcular_estatisticas(self, df):
        estatisticas = calcular_estatisticas_numpy(df)
        return estatisticas
    
    #visualizacao
    def gerar_visualizacoes(self, df, metricas):
        gerar_visualizacoes(df, metricas)
