import requests
from langchain import PromptTemplate


GENERATIVE_SERVICE_URL = "http://generative_service:8000/generate/"

template = """
Você é um operador de direito do poder judiciário brasileiro. \
Sua tarefa é escrever o relatório do resultado da decisão em um processo judicial proferido por um magistrado. \
Para fazer esse relatório você precisa simplificar a linguagem usada de forma que o leitor deste relátorio são pessoas simples sem formação acadêmica. \
No relatório evite jargões jurídicos. \
Faça o texto em até três parágrafos que estarão disposto como um texto fluído: \
primeiro um texto relatando o histórico do processo, petição inicial, pedidos, defesas, etc, ou seja, um resumo com linguagem simplificada do relatório do processo.\
Esse primeiro parágrafo é opcional, devendo ser escrito apenas se hover preferimento de relatório na decisão.\
O segundo parágrafo deve citar sobre a linha argumentativo do magistrado.\
O terceiro parágrafo deve resumir o resultado da decisão do magistrado.\
Após esse texto agora escreva um resumo em tópicos em bullet point com os tópicos decididos referente a cada pedido feito.\
Agora  faça o relatório para o texto de decisão a seguir:
Texto Documento:```{input_text}```  \
Relatório:
"""


def process_prompt(input_text: str) -> str:
    processed_prompt = PromptTemplate.from_template(
            template=template
        ).format(input_text=input_text)
    
    # Encaminha o prompt processado para o serviço generative_service
  
    try:

        response = requests.post(GENERATIVE_SERVICE_URL, json={"prompt": processed_prompt})
        response.raise_for_status()
        return response.json().get("response", "No response from generative service")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro ao comunicar com o generative_service: {e}")
