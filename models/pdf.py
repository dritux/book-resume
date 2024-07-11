import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel, Part

load_dotenv()

# Obter variáveis de ambiente
PROJECT_ID = os.getenv("PROJECT_ID")
URL_STORAGE = os.getenv("URL_STORAGE")
LOCATION = os.getenv("LOCATION")
MODEL_NAME = os.getenv("MODEL_NAME")

def pdf(prompt):
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    model = GenerativeModel(model_name=MODEL_NAME)

    pdf_file = Part.from_uri(URL_STORAGE, mime_type="application/pdf")
    contents = [pdf_file, prompt]

    response = model.generate_content(contents)
    return response.text