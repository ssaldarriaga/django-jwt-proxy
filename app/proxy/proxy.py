import httpx

from fastapi import Request, Response

from app import utils
from app.settings import TARGET_BASE_URL_API, JWT_HEADER

class RequestProxy():
    def __init__(self, real_request: Request, real_response: Response) -> None:
        self._real_request = real_request
        self._real_response = real_response

    async def post(self, data: dict) -> Response:
        path = self._get_path()
        headers = self._get_headers(data.get("name"))
        async with httpx.AsyncClient() as client:
            response = await client.post("{base}{path}".format(base=TARGET_BASE_URL_API, path=path), data=data, headers=headers)

            self._real_response.body = response.content
            self._real_response.status_code = response.status_code
            return self._real_response

    def _get_headers(self, username: str) -> dict:
        payload = {"username": username, "date": str(utils.get_now())}        
        headers = {JWT_HEADER: utils.generate_jwt(payload)}
        return headers

    def _get_path(self) -> str:
        return self._real_request.url.components.path


