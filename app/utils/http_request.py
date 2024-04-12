import httpx
from app.models.coverage import Coverage

def make_request(url):
        response = httpx.get(url)
        return response.json()

def parse_api_response(api_response, field_mapping):
    parsed_result = {}
    try:
        for api_field, model_field in field_mapping.items():
            try:
                value = api_response[api_field]
                parsed_result[model_field] = value
            except KeyError:
                parsed_result[model_field] = 0 # Since only dealing with numbers, 0 is a good default value
        return Coverage.model_validate( parsed_result)
    except Exception as e:
        print(f"Error while parsing response {api_response}: {e}")
    
