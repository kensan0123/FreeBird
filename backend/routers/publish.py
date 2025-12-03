from fastapi import APIRouter
from schemas.publish_schemas import PublishRequest, PublishResponse
from services.publish_service import publish_article

router = APIRouter(prefix="/publish", tags=["Publish"])

@router.post("/")
def publish(req: PublishRequest) -> PublishResponse:
    """
    Docstring for publish
    
    :param req: Description
    :type req: PublishRequest
    :return: {"status": ["success" or "fail"], "slug": str}
    :rtype: Any
    """

    publish_response: PublishResponse = publish_article(req=req)
    
    return publish_response
