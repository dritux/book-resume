# Gemini AI


Example Model:
```
gemini-1.5-flash-001
```

### Setup

1. Install dependêncies
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

2. Export google service account 
```
export GOOGLE_APPLICATION_CREDENTIALS=/path/service_account.json

Example: export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/service_account.json
```

3. Create file .env in root projeto and inputs values

```
PROJECT_ID={YOUR GOOGLE PROJECT ID}
URL_STORAGE={YOUR URL GS STORAGE BOOKS}
LOCATION={LOCATION}
MODEL_NAME={MODEL}
``` 


### Running Function
```
functions-framework --target main --debug
```

### Example request
```
curl -X POST http://localhost:8080 \
-H "Content-Type: application/json" \
-d '{
  "prompt": "Você é um especialista em resumo de documentos muito profissional. Por favor, resuma o documento fornecido crie indice do resumo e responda em português."
}'
```