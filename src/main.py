from SalesInsight import SalesInsight, SalesProjection
import pandas as pd
import numpy as np
from gerador_dataset import gerar_dataset_vendas
from IPython.display import display


if __name__ == "__main__":
 
    #criar instancia da classe
    si = SalesInsight(pd, np)
    sp = SalesProjection(pd, np)

    #gerar datase
    dataset_vendas = (gerar_dataset_vendas())
    
    #carregar
    df_bruto = si.carregar_dicionario(dataset_vendas)
    
    #inspecionar
    si.inspecionar_dados(df_bruto)
    #limpeza
    df_limpo, relatorio = si.limpar_dados(df_bruto)
    
    #criação de colunas derivadas
    df_derivado = si.criar_colunas_derivadas(df_limpo)
    
    #calcular métricas
    metricas = si.calcular_metricas(df_derivado)
    
    #Segmentação de clientes
    df_segmentado = si.segmentar_clientes(df_derivado)
    
    #calcular estatísticas
    estatisticas = si.calcular_estatisticas(df_derivado)
    
    #visualização
    si.gerar_visualizacoes(df_derivado, metricas)
    
    #Projeções futuras (exemplo)
    sp.projetar_tendencia(df_derivado)
    sp.exibir_projecao_detalhada()
    
    # Lambda em apply (transformação condicional de coluna)
    df_derivado["desconto"] = df_derivado["receita_total"].apply(lambda x: 0.10 if x > 10000 else 0.05)

    # Lambda como filtro rápido
    vendas_alto_valor = df_derivado[df_derivado["receita_total"].apply(lambda x: x > 5000)]

    print("=== EXEMPLOS DE FUNÇÕES LAMBDA ===")
    print("\nDataFrame com coluna 'desconto':")
    display(df_derivado[['receita_total', 'desconto']].head())

    print("\nVendas de alto valor (primeiras 5 linhas):")
    display(vendas_alto_valor.head())

    #processar transformação de coluna
    df_transformado = si.processar_coluna(df_derivado.copy(), "receita_total", lambda x: round(x / 1000, 2))
    display(df_transformado[['receita_total', 'receita_total_transformado']].head())

    df_transformado2= si.processar_coluna(df_derivado.copy(), "quantidade", lambda x: "Alto" if x > 5 else "Baixo")
    display(df_transformado2[['quantidade', 'quantidade_transformado']].head())

    #limpar strings com regex
    df_com_regex_limpo = si.limpar_strings_com_regex(df_bruto.copy())
    display(df_com_regex_limpo.head())
    
    #exportar resultados
    si.exportar_resultados(metricas, df_segmentado, estatisticas)
    
    #exportar csv
    si.exportar_csv(df_segmentado, "vendas_segmentadas.csv")
