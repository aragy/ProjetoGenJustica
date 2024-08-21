from langchain.llms import Ollama

def generate_response(prompt: str) -> str:
    try:
        llm = Ollama(model="llama3.1")
        response = llm.invoke( input=prompt)
        return response
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar resposta: {e}")
