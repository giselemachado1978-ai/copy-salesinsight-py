from .analise import *
from .leitura import *
from .limpeza import *
from .metricas import *
from .visualizacao import *
import json
import os
import re

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
        estatisticas = calcular_estatisticas_numpy(df,np = self._np)
        return estatisticas
    
    #visualizacao
    def gerar_visualizacoes(self, df, metricas):
        gerar_visualizacoes(df, metricas)

    # transformação
    def processar_coluna(self, df_input, coluna, funcao_transformacao):
        """
        Aplica uma função de transformação a uma coluna do DataFrame.
        Demonstra o uso de funções como argumentos (higher-order function / callback).
        """
        df_input[f"{coluna}_transformado"] = df_input[coluna].apply(funcao_transformacao)
        print(f"  Coluna '{coluna}_transformado' criada com sucesso.")
        return df_input
    
    def limpar_strings_com_regex(self, df):
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
    
    # exportar
    def exportar_resultados(self,metricas, clientes, stats_numpy):
        """Exporta resultados em CSV e JSON."""
        os.makedirs("outputs", exist_ok=True)

        # Exportar CSV com métricas por mês
        caminho_csv = "outputs/metricas_por_mes.csv"
        metricas["por_mes"].to_csv(caminho_csv, index=False, encoding="utf-8-sig")
        print(f"  CSV exportado: {caminho_csv}")

        # Exportar segmentação de clientes em CSV
        caminho_clientes = "outputs/segmentacao_clientes.csv"
        clientes.to_csv(caminho_clientes, index=False, encoding="utf-8-sig")
        print(f"  CSV exportado: {caminho_clientes}")

        # Exportar estatísticas gerais em JSON
        caminho_json = "outputs/estatisticas_gerais.json"
        stats_serializaveis = {k: round(float(v), 2) for k, v in stats_numpy.items()}
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(stats_serializaveis, f, indent=4, ensure_ascii=False)
        print(f"  JSON exportado: {caminho_json}")

        # Ler e exibir o JSON exportado para confirmar
        with open(caminho_json, "r", encoding="utf-8") as f:
            dados_lidos = json.load(f)
        print(f"\n  Conteúdo do JSON exportado:\n  {json.dumps(dados_lidos, indent=2)}")

class SalesProjection(SalesInsight):
    def __init__(self, pd, np, meses_projecao=6, projecoes=[]):
        super().__init__(pd, np)
        self._meses_projecao = meses_projecao
        self._projecoes = projecoes
        self.metricas = None
        
    def projetar_tendencia(self, dataset):
        """
        Projeta a receita dos próximos meses com base na média móvel dos últimos 3 meses.
        Método simples sem machine learning – baseado em médias.
        """
        if type(dataset) == dict:
            df = self.carregar_dicionario(dataset)
        elif type(dataset) == str:
            df = self.carregar_csv(dataset)
        elif isinstance(dataset, self._pd.DataFrame):
            df = dataset
        else:
            print("[AVISO] Tipo de dataset não suportado para projeção.")
            return self
        
        self.metricas = self.calcular_metricas(df)
        
        if not self.metricas or "por_mes" not in self.metricas:
            print("[AVISO] Rode .analisar() antes de projetar.")
            return self

        por_mes = self.metricas["por_mes"].sort_values("mes")
        receitas_historicas = por_mes["receita_total"].to_numpy()

        # Média móvel dos últimos 3 meses como base da projeção
        ultimos_3 = receitas_historicas[-3:]
        media_movel = np.mean(ultimos_3)
        tendencia = np.std(ultimos_3) * 0.1  # fator de crescimento simples

        ultimo_mes = int(por_mes["mes"].max())

        print("\n=== PROJEÇÃO DE TENDÊNCIA (Média Móvel Simples) ===")
        print(f"  Base: média dos últimos 3 meses = R$ {media_movel:,.2f}")
        self._projecoes = []

        for i in range(1, self._meses_projecao + 1):
            mes_projetado = (ultimo_mes + i - 1) % 12 + 1
            receita_projetada = media_movel + (tendencia * i)
            self._projecoes.append({"mes": mes_projetado, "receita_projetada": round(receita_projetada, 2)})
            print(f"  Mês {mes_projetado:02d} (projeção): R$ {receita_projetada:,.2f}")

    def exibir_projecao_detalhada(self):
        """Exibe as projeções calculadas."""
        if not self._projecoes:
            print("[AVISO] Nenhuma projeção disponível. Rode .projetar_tendencia() primeiro.")
            return
        print("\n=== DETALHAMENTO DAS PROJEÇÕES ===")
        for p in self._projecoes:
            print(f"  Mês {p['mes']:02d}: R$ {p['receita_projetada']:,.2f}")
