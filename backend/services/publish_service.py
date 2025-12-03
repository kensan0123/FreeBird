from schemas.publish_schemas import PublishRequest, PublishResponse
import requests
from core.settings import KENN_ZENN_URL

def publish_article(req: PublishRequest) -> PublishResponse:
    """
    Docstring for publish_article
    
    :param req: Description
    :type req: PublishRequest
    :return: Description
    :rtype: PublishResponse
    """

    response = requests.post(f"{KENN_ZENN_URL}/publish", json=req.model_dump())

    response_json = response.json()
    publish_response: PublishResponse = PublishResponse(
        status=response_json.get("status"), slug=response_json.get("slug")
    )

    return publish_response
