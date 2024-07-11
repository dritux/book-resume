import functions_framework
from models import pdf

@functions_framework.http
def main(request):

    if request.method == 'POST':
        request_json = request.get_json(silent=True)

        if request_json and 'prompt' in request_json:
            prompt = request_json['prompt']
            response = pdf(prompt)
            return response, 200

        return "Missing parameters", 422
    return "Method Not Allowed", 405