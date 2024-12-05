from fastapi.responses import JSONResponse
from typing import Any, Dict


def error_response(msg: str, err_type: int) -> JSONResponse:
    response = {"result": False, "error_message": f"{msg}", "error_type": f"{err_type}"}

    return JSONResponse(content=response, status_code=err_type)


def ok_response(
    resp: Any | None = None, name: str | None = None
) -> dict[str, bool | Any]:
    response = {"result": True}
    if isinstance(resp, dict) and name is None:
        result = resp
    else:
        result = {f"{name}": resp}

    return response | result if resp is not None else response
