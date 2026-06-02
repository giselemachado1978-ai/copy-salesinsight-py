from SalesInsight import SalesInsight
import pandas as pd
import numpy as np
from gerador_dataset import gerar_dataset_vendas



if __name__ == "__main__":
 
    si = SalesInsight(pd, np)

    dataset_vendas = si.carregar_dicionario(gerar_dataset_vendas())
    
    
    print(dataset_vendas.head())
