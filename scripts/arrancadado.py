import pdfplumber # primeira vez que uso
import pandas as pd
import re



def abrePDF(pdf_path_external):
#pdf_path = "./pdf/cadastro_de_empregadores.pdf"
    pdf_path = pdf_path_external
    print(f"Lendo: {pdf_path}")
    linhas = []

    with pdfplumber.open(pdf_path) as pdf: # conforme exemplo
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            
            for line in text.split("\n"):
                # tirar o cabeçalho de cada página
                if any(x in line for x in [
                    "Cadastro de Empregadores",
                    "Portaria Interministerial",
                    "Página",
                    "Atualização periódica",
                    "PUBLICAÇÃO DO CADASTRO"
                ]):
                    continue
                
                linhas.append(line.strip())

    # juntar linhas
    texto = "\n".join(linhas)

    # regex (aqui eu não sei se tõ fazendo certo)
    pattern = re.compile(
        r"(\d+)\s+"              # ID
        r"(\d{4})\s+"           # Ano
        r"([A-Z]{2})\s+"        # UF
        r"(.+?)\s+"             # Empregador
        r"(\d{2,3}\.?\d{3}\.?\d{3}\/?\d{2,4}-?\d{2})\s+"  # CNPJ/CPF
        r"(.+?)\s+"             # Estabelecimento
        r"(\d+)\s+"             # Trabalhadores
        r"([\d\-\/]+)\s+"       # CNAE
        r"(\d{2}/\d{2}/\d{4})\s+"  # Decisão
        r"(\d{2}/\d{2}/\d{4})"     # Inclusão
    ) #obrigado Copilot

    dados = []

    for match in pattern.finditer(texto):
        dados.append(match.groups())

    registros = []
    buffer = ""

    for line in linhas:
        # se começa com número → novo registro
        if re.match(r"^\d+\s", line):
            if buffer:
                registros.append(buffer.strip())
            buffer = line
        else:
            buffer += " " + line

    # último
    if buffer:
        registros.append(buffer.strip())

    # DataFrame
    df = pd.DataFrame(dados, columns=[
        "ID",
        "Ano",
        "UF",
        "Empregador",
        "CNPJ/CPF",
        "Estabelecimento",
        "Trabalhadores",
        "CNAE",
        "Data decisão",
        "Data inclusão"
    ])

    # converter
    df["ID"] = pd.to_numeric(df["ID"], errors="coerce")
    #df["ID"] = df["ID"].astype(int)
    df["Ano"] = df["Ano"].astype(int)
    df["Trabalhadores"] = df["Trabalhadores"].astype(int)

    # salvar em outros formatos
    df.to_csv("empregadores.csv", index=False)
    #df.to_excel("empregadores.xlsx", index=False)

    print(df.head)

    return df

#abrePDF("./pdf/cadastro_de_empregadores.pdf")
#acima foi para testes :)