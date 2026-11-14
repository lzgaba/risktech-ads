import streamlit as st
import pandas as pd

st.set_page_config(page_title="RiskTech - Gestão de Riscos", page_icon="🛡️", layout="wide")

# Inicialização do estado da sessão para armazenar dados em memória no MVP
if "atividades" not in st.session_state:
    st.session_state.atividades = [
        {"id": 1, "nome": "Manutenção Preventiva em Painel Elétrico", "setor": "Manutenção", "descricao": "Inspeção e reaperto de conexões energizadas."},
        {"id": 2, "nome": "Operação de Prensa Hidráulica", "setor": "Produção", "descricao": "Conformação de peças metálicas em linha contínua."},
        {"id": 3, "nome": "Manuseio de Reagentes Químicos", "setor": "Laboratório", "descricao": "Preparo de soluções ácidas para análise de qualidade."}
    ]

if "riscos" not in st.session_state:
    st.session_state.riscos = [
        {
            "atividade": "Manutenção Preventiva em Painel Elétrico",
            "agente": "Choque elétrico e arco voltaico",
            "categoria": "Acidente",
            "probabilidade": 3,
            "severidade": 5,
            "medidas": "Bloqueio e etiquetagem (LOTO), uso de vestimenta antichama (ATP), luvas isolantes classe 0 e ferramenta isolada (NR-10)."
        },
        {
            "atividade": "Operação de Prensa Hidráulica",
            "agente": "Prensamento de membros superiores e ruído contínuo",
            "categoria": "Físico / Acidente",
            "probabilidade": 3,
            "severidade": 4,
            "medidas": "Cortina de luz na zona de prensagem, comando bimanual, protetor auricular tipo concha e treinamento específico (NR-12)."
        },
        {
            "atividade": "Manuseio de Reagentes Químicos",
            "agente": "Inalação de vapores ácidos e respingos",
            "categoria": "Químico",
            "probabilidade": 4,
            "severidade": 3,
            "medidas": "Uso obrigatório de capela de exaustão, óculos ampla visão, avental em PVC, luvas nitrílicas e máscara com filtro químico."
        }
    ]

def calcular_classificacao(prob, sev):
    score = prob * sev
    if score <= 4:
        return score, "Baixo", "🟢"
    elif score <= 9:
        return score, "Médio", "🟡"
    elif score <= 15:
        return score, "Alto", "🟠"
    else:
        return score, "Crítico", "🔴"

st.title("🛡️ RiskTech — Sistema de Gerenciamento de Riscos Ocupacionais")
st.caption("MVP — Projeto Integrador (ADS) | Desenvolvido por Luiz Gabriel Torres de Matos")

menu = st.sidebar.radio(
    "Navegação",
    [
        "1. Cadastro de Atividades",
        "2. Identificação e Classificação de Riscos",
        "3. Matriz de Riscos",
        "4. Medidas Preventivas"
    ]
)

# --- TELA 1: CADASTRO DE ATIVIDADES ---
if menu == "1. Cadastro de Atividades":
    st.header("📋 Cadastro de Atividades Ocupacionais")
    with st.form("form_atividade", clear_on_submit=True):
        col1, col2 = st.columns(2)
        nome = col1.text_input("Nome da Atividade *")
        setor = col2.text_input("Setor / Área *")
        descricao = st.text_area("Descrição detalhada da tarefa")
        submitted = st.form_submit_button("Cadastrar Atividade")

        if submitted:
            if nome.strip() and setor.strip():
                novo_id = len(st.session_state.atividades) + 1
                st.session_state.atividades.append({
                    "id": novo_id,
                    "nome": nome.strip(),
                    "setor": setor.strip(),
                    "descricao": descricao.strip() or "Sem descrição adicional."
                })
                st.success(f"Atividade '{nome}' cadastrada com sucesso!")
            else:
                st.error("Preencha os campos obrigatórios (Nome da Atividade e Setor).")

    st.subheader("Atividades Registradas")
    df_ativ = pd.DataFrame(st.session_state.atividades)
    st.dataframe(df_ativ, use_container_width=True, hide_index=True)

# --- TELA 2: IDENTIFICAÇÃO E CLASSIFICAÇÃO DE RISCOS ---
elif menu == "2. Identificação e Classificação de Riscos":
    st.header("⚠️ Identificação e Classificação de Riscos")
    nomes_atividades = [a["nome"] for a in st.session_state.atividades]

    with st.form("form_risco", clear_on_submit=True):
        atividade_sel = st.selectbox("Selecione a Atividade Ocupacional *", nomes_atividades)
        col1, col2 = st.columns(2)
        categoria = col1.selectbox("Categoria do Risco *", ["Físico", "Químico", "Biológico", "Ergonômico", "Acidente"])
        agente = col2.text_input("Agente / Fator de Risco * (ex: Ruído, Choque elétrico)")

        col3, col4 = st.columns(2)
        probabilidade = col3.slider("Probabilidade (1 = Rara, 5 = Muito Provável)", 1, 5, 3)
        severidade = col4.slider("Severidade (1 = Leve, 5 = Catastrófica)", 1, 5, 3)

        medidas = st.text_area("Medidas Preventivas e EPIs/EPCs Recomendados *")
        submitted_risco = st.form_submit_button("Registrar Risco")

        if submitted_risco:
            if agente.strip() and medidas.strip():
                st.session_state.riscos.append({
                    "atividade": atividade_sel,
                    "agente": agente.strip(),
                    "categoria": categoria,
                    "probabilidade": probabilidade,
                    "severidade": severidade,
                    "medidas": medidas.strip()
                })
                st.success("Risco identificado e classificado com sucesso!")
            else:
                st.error("Informe o agente de risco e as medidas preventivas.")

    st.subheader("Riscos Mapeados")
    dados_tabela = []
    for r in st.session_state.riscos:
        score, nivel, icone = calcular_classificacao(r["probabilidade"], r["severidade"])
        dados_tabela.append({
            "Atividade": r["atividade"],
            "Categoria": r["categoria"],
            "Agente de Risco": r["agente"],
            "Prob.": r["probabilidade"],
            "Sev.": r["severidade"],
            "Grau (P×S)": score,
            "Classificação": f"{icone} {nivel}"
        })
    st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)

# --- TELA 3: MATRIZ DE RISCOS ---
elif menu == "3. Matriz de Riscos":
    st.header("📊 Matriz de Riscos (Probabilidade × Severidade)")
    st.markdown("Distribuição quantitativa dos riscos cadastrados conforme cruzamento de **Probabilidade (linhas)** e **Severidade (colunas)**.")

    matriz = [[0 for _ in range(5)] for _ in range(5)]
    for r in st.session_state.riscos:
        p_idx = 5 - r["probabilidade"]  # Linha 0 = Probabilidade 5
        s_idx = r["severidade"] - 1     # Coluna 0 = Severidade 1
        matriz[p_idx][s_idx] += 1

    df_matriz = pd.DataFrame(
        matriz,
        index=["Prob. 5 (Muito Alta)", "Prob. 4 (Alta)", "Prob. 3 (Média)", "Prob. 2 (Baixa)", "Prob. 1 (Rara)"],
        columns=["Sev. 1 (Leve)", "Sev. 2 (Menor)", "Sev. 3 (Moderada)", "Sev. 4 (Grave)", "Sev. 5 (Catastrófica)"]
    )
    st.table(df_matriz)

    st.markdown("""
    **Legenda de Criticidade (P × S):**
    * 🟢 **1 a 4 (Baixo):** Manter controles existentes e monitoramento de rotina.
    * 🟡 **5 a 9 (Médio):** Avaliar melhorias nos controles e reforçar treinamentos.
    * 🟠 **10 a 15 (Alto):** Priorizar ações corretivas e barreiras coletivas (EPCs).
    * 🔴 **16 a 25 (Crítico):** Intervenção imediata obrigatória antes da continuidade da tarefa.
    """)

# --- TELA 4: MEDIDAS PREVENTIVAS ---
elif menu == "4. Medidas Preventivas":
    st.header("🦺 Plano de Medidas Preventivas e Controles")
    filtro_nivel = st.selectbox("Filtrar por Nível de Risco", ["Todos", "Crítico", "Alto", "Médio", "Baixo"])

    for r in st.session_state.riscos:
        score, nivel, icone = calcular_classificacao(r["probabilidade"], r["severidade"])
        if filtro_nivel != "Todos" and nivel != filtro_nivel:
            continue

        with st.expander(f"{icone} [{nivel.upper()} - Score {score}] {r['atividade']} — {r['agente']}", expanded=True):
            st.write(f"**Categoria:** {r['categoria']} | **Probabilidade:** {r['probabilidade']}/5 | **Severidade:** {r['severidade']}/5")
            st.info(f"**Medidas Preventivas Recomendadas:** {r['medidas']}")
