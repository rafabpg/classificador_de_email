    
from fastapi import Depends, APIRouter
from pydantic import BaseModel
from typing import Any, Callable, Optional, List, Type, TypeVar
from typing_extensions import ParamSpec
import functools
from .exception import handle_exceptions

P = ParamSpec('P')
T = TypeVar('T')
DataT = TypeVar('DataT')

def create(
    router: APIRouter, 
    api_func: Callable[P, T],
    rule: str,
    *,
    response_model: Optional[Type[BaseModel]] = None,
    dependencies: Optional[List[Depends]] = None,
    **options: Any
) -> Callable[P, T]:
    """
    Decorator to create a POST endpoint for the provided function.

    Args:
        router (APIRouter): The FastAPI router to add the endpoint to.
        api_func (Callable[P, T]): The asynchronous function that performs the create operation.
        rule (str): The URL path for the endpoint.
        response_model (Optional[Type[BaseModel]]): The Pydantic model used for the response. Defaults to None.
        dependencies (Optional[List[Depends]]): List of dependencies to be injected. Defaults to None.
        **options (Any): Additional options to pass to the route decorator.

    Returns:
        Callable[P, T]: The decorated function that becomes a POST endpoint.
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @router.post(rule, response_model=response_model, dependencies=dependencies, **options)
        @functools.wraps(func)
        @handle_exceptions
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            result = await api_func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def get(
    router: APIRouter,
    api_func: Callable[P, T],
    rule: str,
    *,
    response_model: Optional[Type[BaseModel]] = None,
    dependencies: Optional[List[Depends]] = None,
    **options: Any
) -> Callable[P, T]:
    """
    Decorator to create a GET endpoint for the provided function.

    Args:
        router (APIRouter): The FastAPI router to add the endpoint to.
        api_func (Callable[P, T]): The asynchronous function that performs the get operation.
        rule (str): The URL path for the endpoint.
        response_model (Optional[Type[BaseModel]]): The Pydantic model used for the response. Defaults to None.
        dependencies (Optional[List[Depends]]): List of dependencies to be injected. Defaults to None.
        **options (Any): Additional options to pass to the route decorator.

    Returns:
        Callable[P, T]: The decorated function that becomes a GET endpoint.
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @router.get(rule, response_model=response_model, dependencies=dependencies, **options)
        @functools.wraps(func)
        @handle_exceptions
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            result = await api_func(*args, **kwargs)
            return result
        return wrapper
    return decorator