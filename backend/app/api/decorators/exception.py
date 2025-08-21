from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from functools import wraps
from typing import Callable, Any
import inspect

class ErrorResponse(BaseModel):
    detail: str              
    error_type: str           

EXCEPTION_STATUS_CODES = {
    ValueError: status.HTTP_400_BAD_REQUEST,
    PermissionError: status.HTTP_403_FORBIDDEN,
    KeyError: status.HTTP_404_NOT_FOUND,
}

def handle_exceptions(func: Callable) -> Callable:
    """
    Decorator to catch and handle exceptions in functions.

    If the function is an asynchronous function, it wraps it with an asynchronous
    exception handler. If the function is a synchronous function, it wraps it with
    a synchronous exception handler.

    Exceptions are caught and a JSON response is returned with a status code and
    an `ErrorResponse` object. If the exception is an instance of `HTTPException`,
    it is re-raised.

    The exception type is used to determine the status code of the response, with
    a default of 422 if the exception type is not found in `EXCEPTION_STATUS_CODES`.
    """
    @wraps(func)
    async def async_wrapper(*args, **kwargs) -> Any:
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            raise
        except Exception as e:
            status_code = EXCEPTION_STATUS_CODES.get(type(e), status.HTTP_422_UNPROCESSABLE_ENTITY)
            
            error_response = ErrorResponse(
                detail=str(e),
                error_type=e.__class__.__name__,
            )
            return JSONResponse(
                status_code=status_code,
                content=error_response.model_dump(),
            )

    @wraps(func)
    def sync_wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except HTTPException:
            raise
        except Exception as e:
            status_code = EXCEPTION_STATUS_CODES.get(type(e), status.HTTP_422_UNPROCESSABLE_ENTITY)
            
            error_response = ErrorResponse(
                detail=str(e),
                error_type=e.__class__.__name__,
            )
            return JSONResponse(
                status_code=status_code,
                content=error_response.model_dump(),
            )

    return async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper