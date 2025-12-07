from fastapi import APIRouter, HTTPException
from schemas.publish_schemas import PublishRequest, PublishResponse
from services.publish_service import publish_article
from exceptions.api_exception import KennZennAPIError

router = APIRouter(prefix="/publish", tags=["Publish"])


@router.post("/")
def publish(req: PublishRequest) -> PublishResponse:
    """
    Publish an article to Kenn_Zenn service

    :param req: Publish request containing slug to publish
    :type req: PublishRequest
    :return: {"status": ["published!" or "failed"], "slug": str}
    :rtype: PublishResponse
    :raises HTTPException: If the Kenn_Zenn API request fails
    """

    try:
        publish_response: PublishResponse = publish_article(req=req)
        return publish_response
    except KennZennAPIError as e:
        raise HTTPException(
            status_code=e.status_code or 500,
            detail={
                "error": "Kenn_Zenn API Error",
                "message": e.message,
                "endpoint": e.endpoint,
            },
        )
