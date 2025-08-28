import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração inicial
st.set_page_config(page_title="Meu Dashboard Pessoal", page_icon="📊", layout="wide")

st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")
st.sidebar.markdown("Desenvolvido por Prof. Tiago Marum [THM Estatística](https://thmestatistica.com)")


# --- FUNÇÃO DE ANÁLISE DE DADOS ---
def analise_dados():
    st.title("📊 Análise de Dados")

    # Caminho do seu arquivo CSV
    caminho_arquivo = "dados.csv"  # <-- troque pelo nome do seu CSV

    try:
        # Lê o CSV usando encoding latin1 (resolve problemas de caracteres especiais)
        df = pd.read_csv(caminho_arquivo, encoding='latin1')
    except FileNotFoundError:
        st.error(f"Arquivo '{caminho_arquivo}' não encontrado. Verifique o caminho.")
        return
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return

    # --- 1. Tabela de Dados ---
    st.header("1. Tabela de Dados")
    st.dataframe(df.head())
    st.write("Tipos de variáveis:")
    st.write(df.dtypes)

    # --- 2. Estatísticas Descritivas ---
    st.header("2. Estatísticas Descritivas")
    st.write(df.describe())
    st.write("**Moda das variáveis numéricas:**")
    st.write(df.mode().iloc[0])

    # --- 3. Matriz de Correlação ---
    st.header("3. Matriz de Correlação")
    num_cols = df.select_dtypes(include=['float', 'int']).columns
    if len(num_cols) > 1:
        fig, ax = plt.subplots()
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.info("Dataset não possui colunas numéricas suficientes para calcular correlação.")

    # --- 4. Filtros Interativos ---
    st.header("4. Filtros Interativos")
    filtro_colunas = st.multiselect("Escolha colunas para filtrar", df.columns)
    df_filtrado = df.copy()
    for col in filtro_colunas:
        valores = st.multiselect(f"Valores de {col}", df[col].unique())
        if valores:
            df_filtrado = df_filtrado[df_filtrado[col].isin(valores)]
    st.write("Tabela filtrada:")
    st.dataframe(df_filtrado)

    # --- 5. Gráficos ---
    st.header("5. Gráficos")
    col_grafico = st.multiselect("Escolha colunas numéricas para gráfico", num_cols)
    if col_grafico:
        st.bar_chart(df_filtrado[col_grafico])

# --- BARRA LATERAL MODERNA ---
with st.sidebar:
    st.markdown("## 🏠 Meu Dashboard")
    st.markdown("---")
    
    st.markdown("### 🔎 Navegação")
    aba = st.radio(
        "",
        ["🏠 Home", "🎓 Formação e Experiência", "🛠️ Skills", "📂 Projetos", "📬 Contato", "📊 Análise de Dados"],
        label_visibility="collapsed"
    )

    
    st.markdown("---")
    st.markdown("💡 **Dicas:**")
    st.markdown("""
    - Use a aba **Análise de Dados** para visualizar estatísticas.  
    - Filtre colunas diretamente no painel da aba de análise.  
    - Clique nos ícones para navegar rapidamente.
    """)


# --- HOME ---
if aba == "🏠 Home":
    st.title("Bem-vindo ao meu Dashboard Pessoal 👋")
    
    # Imagem que aparece apenas na Home
    st.image("imagem.jpeg", width=100)
    
    st.subheader("Olá")
    st.write("""
    Olá, meu nome é André.  
    Sou estudante e tenho como objetivo me tornar um programador de Python.  
    """)
    st.write("🔗 Conecte-se comigo: [LinkedIn](https://www.linkedin.com/in/andre-giovane-6378b5327/) | [GitHub](https://github.com)")

# --- FORMAÇÃO E EXPERIÊNCIA ---
elif aba == "🎓 Formação e Experiência":
    st.title("Formação e Experiência")
    st.subheader("📘 Formação Acadêmica")
    st.write("""
    - **Curso Eng Software – FIAP (2024 - 2027)**  
    - Banco de Dados Oracle – FIAP  
    """)
    st.subheader("💼 Experiência Profissional")
    st.write("""
    - Desenvolvimento de um app
    """)

# --- SKILLS ---
elif aba == "🛠️ Skills":
    st.title("Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💻 Tecnologias e Ferramentas")
        st.write("""
        - Python, Java, SQL  
        - AR/VR
        - Git/GitHub  
        """)
    with col2:
        st.subheader("🤝 Soft Skills")
        st.write("""
        - Comunicação  
        - Trabalho em equipe  
        - Resolução de problemas
        - Atencioso
        - Focado  
        """)

# --- PROJETOS ---
elif aba == "📂 Projetos":
    st.title("Projetos")
    st.write("Aqui estão alguns dos meus principais projetos:")
    st.markdown("""
    🔹 Projeto feito sobre FÓRMULA E para MAHINDRA – Projeto de front end em HTML  
    [GitHub](https://github.com/peyzin/cp5_web_development)  
    """)

# --- CONTATO ---
elif aba == "📬 Contato":
    st.title("Contato")
    st.write("📧 Email: andregdm8@gmail.com")  
    st.write("🔗 LinkedIn: [LinkedIn](https://www.linkedin.com/in/andre-giovane-6378b5327/)")  
    st.write("💻 GitHub: [GitHub](https://github.com/peyzin)")  

    st.subheader("Formulário de Contato")
    with st.form("contato_form"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        mensagem = st.text_area("Mensagem")
        enviar = st.form_submit_button("Enviar")
        if enviar:
            st.success(f"Obrigado, {nome}! Sua mensagem foi enviada.")

# --- ANÁLISE DE DADOS ---
elif aba == "📊 Análise de Dados":
    analise_dados()
