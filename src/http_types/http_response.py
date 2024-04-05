from typing import Dict


class HttpResponse:
    def __init__(self, body: Dict, status_code: int) -> None:
        self.body = body
        self.status_code = status_code

    # def __str__(self):
    #     return f"HttpResponse(status_code={self.status_code}, headers={self.headers}, body={self.body})"