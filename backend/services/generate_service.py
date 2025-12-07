from schemas.generate_schema import GenerateRequest, GeneratedResponse
import requests
from core.settings import KENN_ZENN_URL
from exceptions.api_exception import KennZennAPIError
from requests.exceptions import Timeout, ConnectionError, HTTPError
from core.logger import logger


def generate_article(req: GenerateRequest) -> GeneratedResponse:
    """
    Docstring for generate_article

    :param req: Description
    :type req: GenerateRequest
    :return: Description
    :rtype: GeneratedResponse
    """
    try:
        logger.info(f"Generating article with theme: {req.title}")
        response = requests.post(
            f"{KENN_ZENN_URL}/generate", json=req.model_dump(), timeout=20
        )
        logger.info("Article generation request completed")
        logger.info(f"Response body: {response.text}")
        response.raise_for_status()
    except Timeout:
        logger.error("Request to Kenn_Zenn API timed out at /generate endpoint")
        raise KennZennAPIError("timeout error", endpoint="/generate")
    except ConnectionError:
        logger.error(
            f"Failed to connect to Kenn_Zenn API at {KENN_ZENN_URL}. Check network connection"
        )
        raise KennZennAPIError("networks error", endpoint="/generate")
    except HTTPError as e:
        if 500 <= e.response.status_code < 600:
            logger.error(f"Server error occurred: status_code={e.response.status_code}")
            raise KennZennAPIError(
                "server error", endpoint="/generate", status_code=e.response.status_code
            )
        else:
            logger.error(f"Client error occurred: status_code={e.response.status_code}")
            raise KennZennAPIError(
                "client error", endpoint="/generate", status_code=e.response.status_code
            )
    except requests.exceptions.RequestException as e:
        logger.error(f"Unknown request error occurred: {str(e)}")
        raise KennZennAPIError("unknown error", endpoint="/generate")

    try:
        response_json = response.json()
    except ValueError:
        logger.error("Invalid JSON response from Kenn_Zenn API")
        raise KennZennAPIError(
            message="Invalid JSON response from Kenn_Zenn API",
            endpoint="/generate",
            status_code=response.status_code,
        )

    generate_response: GeneratedResponse = GeneratedResponse(
        status=response_json.get("status"), slug=response_json.get("slug")
    )

    logger.info(
        f"Article generated successfully. slug: {generate_response.slug}, status: {generate_response.status}"
    )

    return generate_response
