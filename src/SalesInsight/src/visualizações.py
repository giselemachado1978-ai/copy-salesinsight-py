import os
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_visualizacoes(df, metricas, output_dir="outputs/graficos"):
    """Gera e exporta visualizações dos dados de vendas."""
    os.makedirs(output_dir, exist_ok=True)

    # Configurações visuais globais
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12

    # Gráfico 1: Receita por Mês
    fig1, ax1 = plt.subplots()
    por_mes = metricas["por_mes"]
    ax1.plot(por_mes["mes"], por_mes["receita_total"], marker="o", linewidth=2, color="#2196F3")
    ax1.fill_between(por_mes["mes"], por_mes["receita_total"], alpha=0.15, color="#2196F3")
    ax1.set_title("Receita Total por Mês (2024)")
    ax1.set_xlabel("Mês")
    ax1.set_ylabel("Receita Total (R$)")
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"], rotation=45)
    plt.tight_layout()
    caminho1 = os.path.join(output_dir, "vendas_por_mes.png")
    plt.savefig(caminho1, dpi=150)
    plt.show()  # Renderizar no notebook
    print(f" Gráfico exportado: {caminho1}\n")
    
    # Gráfico 2: Top 5 Produtos
    fig2, ax2 = plt.subplots()
    top = metricas["top_produtos"]
    sns.barplot(data=top, y="produto", x="receita_total", ax=ax2, hue="produto", legend=False, palette="Blues_d")
    ax2.set_title("Top 5 Produtos por Receita Total")
    ax2.set_xlabel("Receita Total (R$)")
    ax2.set_ylabel("Produto")
    for container in ax2.containers:
        ax2.bar_label(container, fmt="R$ %.0f", padding=5)
    plt.tight_layout()
    caminho2 = os.path.join(output_dir, "top_produtos.png")
    plt.savefig(caminho2, dpi=150)
    plt.show()
    print(f" Gráfico exportado: {caminho2}\n")
    
    # Gráfico 3: Distribuição de Receita por Região (boxplot)
    fig3, ax3 = plt.subplots()
    sns.boxplot(data=df, x="regiao", y="receita_total", ax=ax3, hue="regiao", legend=False, palette="Set2")
    ax3.set_title("Distribuição de Receita por Transação – Por Região")
    ax3.set_xlabel("Região")
    ax3.set_ylabel("Receita por Venda (R$)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    caminho3 = os.path.join(output_dir, "distribuicao_regioes.png")
    plt.savefig(caminho3, dpi=150)
    plt.show()
    print(f" Gráfico exportado: {caminho3}\n")
    print("=== VISUALIZAÇÕES GERADAS E EXPORTADAS COM SUCESSO ===")
