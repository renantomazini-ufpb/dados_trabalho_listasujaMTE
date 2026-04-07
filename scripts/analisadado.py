import os
import arrancadado
import matplotlib.pyplot as plt
import pandas as pd

# isso [e só no windows] :/
os.makedirs("./output", exist_ok=True)

df = arrancadado.abrePDF("./pdf/cadastro_de_empregadores.pdf") #atualizar ano após ano?

# erro anterior por aqui 
df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
df["Trabalhadores"] = pd.to_numeric(df["Trabalhadores"], errors="coerce") 
df = df.dropna(subset=["Ano", "UF", "Trabalhadores"])
df = df.sort_values("Ano")

print("Anos disponíveis:")
print(df["Ano"].value_counts())



# estados por ano :?
def top_estados_por_ano(df, ano):
    df_ano = df[df["Ano"] == ano]

    if df_ano.empty:
        print(f"Sem dados para {ano}")
        return
    
    top = (
        df_ano.groupby("UF")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )
    
    top.plot(kind="bar")
    plt.title(f"10 estados por quantidade de ações fiscais - {ano}")
    plt.xlabel("Estado")
    plt.ylabel("Quantidade de ações fiscais")
    plt.xticks(rotation=45)
    plt.tight_layout()  # coloquei isso aqui para nao ficar ano quebrado como ponto flutuante
    
    plt.savefig(f"./output/top_estados_{ano}.png")
    plt.clf()


for ano in [2024, 2025, 2026]:
    top_estados_por_ano(df, ano)



# ações evolução

acoes_por_ano = df.groupby("Ano").size().sort_index()

plt.plot(acoes_por_ano.index, acoes_por_ano.values, marker="o")
plt.title("Evolução de ações fiscais por ano")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.xticks(acoes_por_ano.index.astype(int))
plt.grid()
plt.tight_layout()

plt.savefig("./output/acoes_por_ano.png")
plt.clf()


# número de trabalhadores 
top_trab_geral = (
    df.groupby("UF")["Trabalhadores"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_trab_geral.plot(kind="bar")
plt.title("10 estados por número de trabalhadores (geral)")
plt.xlabel("Estado")
plt.ylabel("Total de trabalhadores")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("./output/top_trabalhadores_geral.png")
plt.clf()



# trabalhadores por ano
def top_trabalhadores_por_ano(df, ano):
    df_ano = df[df["Ano"] == ano]

    if df_ano.empty:
        print(f"Sem dados de trabalhadores para {ano}")
        return

    top = (
        df_ano.groupby("UF")["Trabalhadores"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    
    top.plot(kind="bar") 
    plt.title(f"10 estados por quantidade de trabalhadores - {ano}")
    plt.xlabel("Estado")
    plt.ylabel("Total de trabalhadores")
    plt.xticks(rotation=45) #magia
    plt.tight_layout()

    plt.savefig(f"./output/top_trabalhadores_{ano}.png")
    plt.clf()


for ano in [2023, 2024, 2025, 2026]:
    top_trabalhadores_por_ano(df, ano)



# ações + trabalhadores
acoes = df.groupby("Ano").size()
trabalhadores = df.groupby("Ano")["Trabalhadores"].sum()

plt.plot(acoes.index, acoes.values, marker="o", label="Ações fiscais")
plt.plot(trabalhadores.index, trabalhadores.values, marker="o", label="Trabalhadores")

plt.title("Evolução de ações fiscais e trabalhadores")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.legend()
plt.xticks(list(map(int, acoes.index))) # coloquei isso aqui para nao ficar ano quebrado como ponto flutuante
plt.grid()
plt.tight_layout()

plt.savefig("./output/acoes_trabalhadores.png")
plt.clf()