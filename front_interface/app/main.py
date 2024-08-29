import streamlit as st
import requests

PROMPT_SERVICE_URL = "http://prompt_service:8001/process_prompt/"

st.set_page_config(page_title="Projeto GenJustiça", page_icon=":speech_balloon:")

st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center; border-bottom: 2px solid red; padding: 10px; background-color: white;">
        <img src="https://www.tjms.jus.br/storage/cms-arquivos/3a9585dff89cf61ef2256f1db0b6ddd1.png" alt="TJMS" style="height: 60px; margin-right: 20px;">
        <h3 style="color: black; margin: 0;">Tribunal de Justiça de Mato Grosso do Sul</h3>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;  
    }
    .stMarkdown h2, .stMarkdown h1, .stMarkdown h3 {
        color: black;  
        border-bottom: 2px solid red;
        padding-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Projeto GenJustiça - Interface")

st.write("Digite o texto da decisão judicial para gerar o relatório simplificado:")

input_text = st.text_area("Texto da Decisão", height=200)

if st.button("Gerar Relatório"):
    if input_text.strip():
        try:
            response = requests.post(PROMPT_SERVICE_URL, json={"prompt": input_text})
            response.raise_for_status()
            result = response.json().get("response", "Erro: resposta vazia do serviço de prompt")
            st.subheader("Relatório Gerado")
            st.write(result)
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao comunicar com o serviço de prompt: {e}")
    else:
        st.warning("Por favor, insira o texto da decisão para gerar o relatório.")
