# Mini projeto 1 - Assistente de Programação em Python

# Importa o módulo que interage com o SO
import os
# Importa o streamlit
import streamlit as st
# Importa o groq
from groq import Groq
# Configura a página do streamlit
st.set_page_config(
    page_title = "Joseph Assistant",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

CUSTOM_PROMPT = """
    Você é o "Joseph Assistant", um assistente de IA especializado em programação, com foco principal em Python.
    Sua missão é ajudar desenvolvedores iniciantes (principalmente na área de dados) com dúvidas.
    
    REGRAS DE OPERAÇÃO:
    1. **Foco em programação**: Responda apenas perguntas relacionadas a programação, algoritmos, estrutura de dados, 
    bibliotecas e frameworks. Se o usuário fugir do assunto, diga que só está treinado para isso.
    
    2. **Estrutura da resposta**: Sempre formate suas respostas da seguinte maneira.
        * **Explicação clara**: comece com uma explicação cnceitual sobre o tópico perguntado. Seja direto e didático.
        * **Exemplo de código**: forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser 
        bem comentado para explicar as partes
        * **Detalhes do código**: Após o bloco de código escreva em detalhes o que cada parte do código faz, explicando 
        a lógica e as funções utilizadas.
        * **Documentação de Referência**: inclua uma seção chamada "Documentação de Referência" comm um link direto e 
        relevante para o documento
    3. **Clareza e Precisão**: use uma linguagem clara, evite jargões desnecessários. Suas respostas devem ser tecnicamente
    precisas
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:

    # Define o título da barra lateral
    st.title("🤖 Joseph Assistant")
    # Mostra um texto exlicativo sobre o assistente
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes.")

    # Campo para inserir a chave da API da Groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python. "
                "IA pode cometer erros")


# titulo principal
st.title("Joseph Assistant")
# subtitulo adicional
st.title("Assistente Pessoal de Programação Python 🐍")
# Texto auxiliar abaixo do titulo
st.caption("Faça uma pergunta sobre a linguagem Python e obtenha o código, explicação e referência.")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Inicializa a variável do cliente Groq com None
client = None

if groq_api_key:

    try:
        # Cria o cliente Groq com a chave da API fornecida
        client = Groq(api_key=groq_api_key)

    except Exception as e:
        # Exibe o erro caso haja problema ao inicializar o cliente
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()

# Caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")


# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual sua dúvida sobre Python?"):

    # Se não houver cliente válido, mosra um aviso e para a eecução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagens para enviar à API, inlcuindo o prompt do sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    # Cria a resposta do assitent no chat

    with st.chat_message("assistant"):

        with st.spinner("Analisando sua pergunta..."):

            try:

                # Chama a API da Groq paa gerar a resposta
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model = "openai/gpt-oss-20b",
                    temperature = 0.7,
                    max_tokens = 2048,
                )

                # Extrai a resposta gerada pela api
                joseph_answer = chat_completion.choices[0].message.content

                # Exibe a resposta no streamlit
                st.markdown(joseph_answer)

                # Armazena a resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": joseph_answer})

            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")





