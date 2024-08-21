# ProjetoGenJustica

**ProjetoGenJustica** is an AI-powered solution designed to generate simplified reports from the text of judicial decisions. The project includes services for prompt generation, prompt engineering, and a user interface for interacting with these components.

## Project Structure

   - `front_interface`: A Streamlit-based interface for interacting with the services.
   - `generative_service`: Handles prompt generation and communication with the model.
   - `prompt_service`: Manages prompt engineering and interacts with the `generative_service`.

## Requirements

   - Docker
   - NVIDIA GPU with drivers and CUDA installed
   - Python 3.10 (for local development)

## Getting Started
1. Clone the Repository


```bash
git clone git@github.com:aragy/ProjetoGenJustica.git
cd ProjetoGenJustica
```

2. Set Up Environment

Ensure your environment variables are correctly set up. Use a .env file if necessary.

3. Build the `custom_ollama_base` Image

To create the custom_ollama_base image, navigate to the project root directory where the Dockerfile is located and run:

```bash
sudo docker build -t custom_ollama_base -f Dockerfile .
```

4. Build and Run Docker Containers

Build the containers and start the services:


```bash
sudo docker-compose up --build
```
5. Start the Ollama Service
Access the qa_pipeline_service container via terminal and start the Ollama service:

```bash
sudo docker exec -it qa_pipeline_service bash
ollama serve
```

6. Access the Application

  -  Generative Service: Available on http://localhost:8000
  -  Prompt Service: Available on http://localhost:8001
  -  Front Interface: Accessible via http://localhost:8501

7. Stopping the Services

To stop the services, run:


```bash
sudo docker-compose down

```
## Usage

   - Upload the text of a judicial decision via the front interface.
   - The text is processed by the prompt_service to generate a simplified prompt.
   - The processed prompt is sent to the generative_service to generate a simplified report.
   - The simplified report is displayed in the front interface.

## Customization

   - Model Weights: The project uses custom model weights. Ensure that these are correctly downloaded and placed in the appropriate directory.
   - GPU Allocation: Modify the docker-compose.yml file to specify GPU allocation.

## Troubleshooting

   - Ensure your GPU is correctly configured and accessible by Docker.
   - Verify internet connectivity if models fail to download.


## License

This project is licensed under the MIT License.