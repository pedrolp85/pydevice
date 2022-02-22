from typing import Dict, Type

from fastapi import Request
from fastapi.responses import JSONResponse
from repository.exceptions import (
    MyBaseException,
    ResourceAlreadyExistsException,
    ResourceNotFoundException,
)

_EXCEPTION_CONFIG: Dict[Type[Exception], int] = {
    ResourceAlreadyExistsException: 409,
    ResourceNotFoundException: 404,
}
_EXCEPTION_DEFAULT_CODE = 500


def exception_handler(request: Request, exc: MyBaseException) -> JSONResponse:
    for exc_type, err_code in _EXCEPTION_CONFIG.items():
        if isinstance(exc, exc_type):
            return JSONResponse(
                status_code=err_code,
                content={"msg": exc.error_description()},
            )
    return JSONResponse(
        status_code=_EXCEPTION_DEFAULT_CODE,
        content={"msg": exc.error_description()},
    )


def default_exception_handler(request: Request, exc: MyBaseException) -> JSONResponse:
    return JSONResponse(
        status_code=_EXCEPTION_DEFAULT_CODE,
        content={"msg": "general error, try later"},
    )
