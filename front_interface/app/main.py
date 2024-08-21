import streamlit as st
import requests

PROMPT_SERVICE_URL = "http://prompt_service:8001/process_prompt/"

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
