from schemas.generate_schema import GenerateRequest, GeneratedResponse
import requests
from core.settings import KENN_ZENN_URL


def generate_article(req: GenerateRequest) -> GeneratedResponse:
    """
    Docstring for generate_article
    
    :param req: Description
    :type req: GenerateRequest
    :return: Description
    :rtype: GeneratedResponse
    """
    response = requests.post(f"{KENN_ZENN_URL}/generate", json=req.model_dump())

    response_json = response.json()
    generate_response: GeneratedResponse = GeneratedResponse(
        status=response_json.get("status"), slug=response_json.get("slug")
    )

    return generate_response
