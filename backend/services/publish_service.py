from schemas.publish_schemas import PublishRequest, PublishResponse
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError
from core.settings import KENN_ZENN_URL
from exceptions.api_exception import KennZennAPIError
from core.logger import logger


def publish_article(req: PublishRequest) -> PublishResponse:
    """
    Publish an article to Kenn_Zenn service

    :param req: Publish request containing slug
    :type req: PublishRequest
    :return: Publish response with status and slug
    :rtype: PublishResponse
    :raises KennZennAPIError: If API request fails or returns invalid response
    """
    logger.info(f"Publishing article with slug: {req.slug}")

    try:
        response = requests.post(
            f"{KENN_ZENN_URL}/publish", json=req.model_dump(), timeout=30
        )

        response.raise_for_status()

    except Timeout:
        logger.error(f"Request to Kenn_Zenn API timed out for slug: {req.slug}")
        raise KennZennAPIError(
            message="Request to Kenn_Zenn API timed out",
            endpoint="/publish",
            status_code=None,
        )
    except ConnectionError:
        logger.error(f"Failed to connect to Kenn_Zenn API at {KENN_ZENN_URL}")
        raise KennZennAPIError(
            message=f"Failed to connect to Kenn_Zenn API at {KENN_ZENN_URL}",
            endpoint="/publish",
            status_code=None,
        )
    except HTTPError as e:
        logger.error(
            f"HTTP error occurred: {str(e)}, status_code: {e.response.status_code}"
        )
        raise KennZennAPIError(
            message=f"HTTP error occurred: {str(e)}",
            endpoint="/publish",
            status_code=e.response.status_code,
        )
    except RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        raise KennZennAPIError(
            message=f"Request failed: {str(e)}", endpoint="/publish", status_code=None
        )

    try:
        response_json = response.json()
    except ValueError:
        logger.error("Invalid JSON response from Kenn_Zenn API")
        raise KennZennAPIError(
            message="Invalid JSON response from Kenn_Zenn API",
            endpoint="/publish",
            status_code=response.status_code,
        )

    status = response_json.get("status")
    slug = response_json.get("slug")

    if not status or not slug:
        logger.error(
            f"Missing required fields in API response. status: {status}, slug: {slug}"
        )
        raise KennZennAPIError(
            message="Missing required fields in API response",
            endpoint="/publish",
            status_code=response.status_code,
        )

    publish_response: PublishResponse = PublishResponse(status=status, slug=slug)
    logger.info(f"Article published successfully. slug: {slug}, status: {status}")

    return publish_response
