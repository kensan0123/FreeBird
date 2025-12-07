class KennZennAPIError(Exception):
    """Kenn_Zenn APIのエラー"""

    def __init__(self, message: str, endpoint: str, status_code: int | None = None):
        self.message = message
        self.endpoint = endpoint
        self.status_code = status_code
        super().__init__(self.message)
