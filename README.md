# 🛡️ RiskTech — Sistema de Gerenciamento de Riscos Ocupacionais

MVP desenvolvido para a disciplina de **Projeto Integrador** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

**Autor:** Luiz Gabriel Torres de Matos

## 📌 Sobre o Projeto
O **RiskTech** é uma aplicação web desenvolvida em Python para auxiliar empresas e profissionais de Segurança do Trabalho (SESMT) no mapeamento, classificação e controle de riscos ocupacionais.

### Funcionalidades Implementadas
1. **Cadastro de Atividades Ocupacionais:** Registro de tarefas e setores operacionais.
2. **Identificação e Classificação de Riscos:** Associação de agentes de risco (Físico, Químico, Biológico, Ergonômico e Acidente) com escala de Probabilidade e Severidade (1 a 5).
3. **Geração de Matriz de Riscos:** Cruzamento automático (Probabilidade × Severidade) categorizando os riscos em *Baixo*, *Médio*, *Alto* e *Crítico*.
4. **Apresentação de Medidas Preventivas:** Exibição filtrável de recomendações técnicas, EPCs e EPIs aplicáveis.

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Streamlit** (Interface web interativa)
- **Pandas** (Manipulação e estruturação de tabelas/matriz)

## ⚙️ Como Executar Localmente
```bash
# Clone o repositório
git clone [https://github.com/SEU-USUARIO/risktech-ads.git](https://github.com/SEU-USUARIO/risktech-ads.git)

# Acesse a pasta do projeto
cd risktech-ads

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
