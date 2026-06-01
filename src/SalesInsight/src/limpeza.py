import pandas as pd
import re

def inspecionar_dados(df):
    """Exibe informações básicas do DataFrame."""
    print('=' * 40)
    print("=== INSPEÇÃO INICIAL DO DATASET ===")
    print('=' * 40)
    print(f"Shape: {df.shape}")
    print('=' * 40)
    print(f"\nColunas: {list(df.columns)}")
    print('=' * 40)
    print(f"\nTipos de dados:\n{df.dtypes}")
    print('=' * 40)
    print(f"\nValores nulos por coluna:\n{df.isnull().sum()}")
    print('=' * 40)
    print(f"\nPrimeiros registros:\n{df.head()}")
    print('=' * 40)
    print(f"\nEstatísticas descritivas:\n{df.describe()}")
    print('=' * 40)

def limpar_dados(df):
    """
    Limpa e trata o DataFrame de vendas.
    Retorna o DataFrame limpo e um relatório com contagens de remoções.
    """
    n_inicial = len(df)
    relatorio = {}
    
    # 1. Remover espaços extras nas colunas de texto
    colunas_texto = df.select_dtypes(include="object, str").columns
    for col in colunas_texto:
        df[col] = df[col].astype(str).str.strip()
        
    # 2. Converter data e remover datas inválidas
    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
    n_datas_invalidas = df["data_venda"].isnull().sum()
    df = df.dropna(subset=["data_venda"])
    relatorio["datas_invalidas_removidas"] = n_datas_invalidas
    
    # 3. Remover linhas com quantidade ou preço nulos
    n_antes = len(df)
    df = df.dropna(subset=["quantidade", "preco_unitario"])
    relatorio["linhas_nulas_removidas"] = n_antes - len(df)
    
    # 4. Garantir tipos numéricos corretos
    df["quantidade"] = df["quantidade"].astype(int)
    df["preco_unitario"] = df["preco_unitario"].astype(float)
    
    n_final = len(df)
    relatorio["registros_iniciais"] = n_inicial
    relatorio["registros_finais"] = n_final
    relatorio["registros_removidos_total"] = n_inicial - n_final
    
    print("=== RELATÓRIO DE LIMPEZA ===")
    for chave, valor in relatorio.items():
        print(f"  {chave}: {valor}")
        
    return df, relatorio

def limpar_strings_com_regex(df):
    """
    Usa expressões regulares para limpeza de colunas de texto.
    Exemplos: remover caracteres especiais, padronizar formatos.
    """
    # 1. Remover caracteres não alfanuméricos do nome do cliente (exceto underline e espaço)
    df["cliente_limpo"] = df["cliente"].apply(
        lambda s: re.sub(r"[^a-zA-Z0-9_ ]", "", str(s)).strip()
    )

    # 2. Identificar registros com padrão de ID inválido (deve ser "Cliente_XXX")
    padrao_cliente = re.compile(r"^Cliente_\d{3}$")
    df["cliente_valido"] = df["cliente_limpo"].apply(
        lambda s: bool(padrao_cliente.match(s))
    )

    n_invalidos = (~df["cliente_valido"]).sum()
    print(f"\n=== LIMPEZA COM REGEX ===")
    print(f"  Clientes com formato inválido encontrados: {n_invalidos}")
    print(f"  Amostra de clientes limpos: {df['cliente_limpo'].head(5).tolist()}")

    return df

