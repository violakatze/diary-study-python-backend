from fastapi.responses import JSONResponse

class ApiError(JSONResponse):
    def __init__(self, code: str):
        super().__init__(status_code=400, content=code)
